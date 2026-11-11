"""Session relay: chains Claude Code rounds from the command line, each one with an empty conversation.

Part of JN's Quota Keeper, token-saving tactics by Jaber Felippe Neto (JN Softworks).
Copyright (c) 2026 Jaber Felippe Neto (JN Softworks). SPDX-License-Identifier: MIT (full text in the guide's LICENSE.md).

Each round is a new `claude -p` running inside the project folder. It reads the handoff file,
does only the "next exact step", updates the handoff file and answers in a few lines ending
with a STATUS line.

Stops when:
- the first line of the handoff file says STAGE DONE (or ETAPA CONCLUIDA);
- a round answers STATUS: QUESTION or STATUS: DONE;
- a round fails (error, STATUS: ERROR, no STATUS, timeout);
- the round limit is reached.

The token is read from a file (default ~/.claude/relay_token.txt) and goes only to the child
process, in CLAUDE_CODE_OAUTH_TOKEN. It is never printed or logged: every text that goes to
the screen or to the log passes through `_hide_token`.

Permissions: by default `--permission-mode dontAsk` (denies anything not on the list) with
`--permission-prompts none` and a short tool list (`--tools`). The user's hooks still apply.

Relay log: besides relay.log in the project, every run adds lines to
<config folder>/quota_keeper/relay_log.jsonl (start, each round's session id, end), with this
process's PID, the folder, the --reason and whether the person was told (--notified).
daily_report.py reads it to tell expected screenless sessions from unexpected ones.
The children also get QUOTA_KEEPER_RELAY=1, so daily_report.py --remind stays quiet inside them.

Usage:
    python session_relay.py --folder <project> --handoff PASSAGEM.md --model sonnet --rounds 3 --reason "finish the stage while I am away" --notified
"""

import argparse
import datetime as dt
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path

CONFIG_DIR = Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude")
DEFAULT_TOKEN_FILE = CONFIG_DIR / "relay_token.txt"
RELAY_LOG = CONFIG_DIR / "quota_keeper" / "relay_log.jsonl"
DEFAULT_TOOLS = "Read,Glob,Grep,Edit,Write"
DONE_MARKS = ("STAGE DONE", "ETAPA CONCLUIDA", "ETAPA CONCLUÍDA")
KEEP_ENV = {"CLAUDE_CONFIG_DIR", "CLAUDE_CODE_GIT_BASH_PATH"}

PROMPT = """You are one round of an automatic relay. Nobody is watching this conversation.

1. Read the handoff file: {handoff}
2. Do ONLY the "next exact step" written there. Nothing more.
3. Update the handoff file: what was done and how it was checked, the new "next exact step", new questions.
   - If the whole stage is finished, write STAGE DONE (or ETAPA CONCLUIDA, if the file is in Portuguese) on the first line of the handoff file.
   - If you need a decision from the person, write the question in the questions section of the handoff file and stop.
4. Allowed tools: {tools}. Any other tool is denied without asking; don't try.
   If the step can't be done with them, explain it in the handoff file and answer STATUS: ERROR.
5. Answer in at most 5 lines, in the language of the handoff file. The last line must be exactly one of:
   STATUS: CONTINUE
   STATUS: QUESTION
   STATUS: DONE
   STATUS: ERROR
"""

STATUS_RE = re.compile(r"STATUS:\s*(CONTINUE|QUESTION|DONE|ERROR)", re.IGNORECASE)

_TOKEN = ""


def _read_token(path: Path) -> str:
    if not path.is_file():
        raise SystemExit(f"Token file not found: {path} (see the guide: claude setup-token)")
    token = path.read_text(encoding="utf-8-sig").strip()
    if not token:
        raise SystemExit(f"Token file is empty: {path}")
    return token


def _hide_token(text: str) -> str:
    if _TOKEN and _TOKEN in text:
        text = text.replace(_TOKEN, "<token>")
    return text


def _find_claude(explicit):
    if explicit:
        exe = Path(explicit)
        if not exe.is_file():
            raise SystemExit(f"claude not found at {exe}")
        return exe
    for name in ("claude.exe", "claude"):
        found = shutil.which(name)
        if found:
            exe = Path(found)
            if exe.suffix.lower() in (".cmd", ".bat"):
                # cmd.exe mangles arguments with parentheses, asterisks and percent signs.
                print(f"warning: using {exe}; if a tool list with ( ) or * fails, pass --claude <path to claude.exe>",
                      flush=True)
            return exe
    raise SystemExit("claude not found in PATH; pass --claude <path>")


def _child_env(token: str) -> dict:
    # Drops the variables a Claude app session sets (proxy address, session ids) so the child
    # starts as an independent session, logged in only by the token.
    env = {k: v for k, v in os.environ.items()
           if k.upper() in KEEP_ENV or not k.upper().startswith(("CLAUDE", "ANTHROPIC"))}
    env["CLAUDE_CODE_OAUTH_TOKEN"] = token
    env["GCM_INTERACTIVE"] = "never"
    env["GIT_TERMINAL_PROMPT"] = "0"
    env["GH_PROMPT_DISABLED"] = "1"
    env["QUOTA_KEEPER_RELAY"] = "1"
    return env


def _log(log: Path, line: dict) -> None:
    with log.open("a", encoding="utf-8") as fh:
        fh.write(_hide_token(json.dumps(line, ensure_ascii=False)) + "\n")


def _registry(line: dict) -> None:
    # The shared relay log must never stop a relay: any error writing it is ignored.
    try:
        RELAY_LOG.parent.mkdir(parents=True, exist_ok=True)
        line = dict(line, pid=os.getpid())
        with RELAY_LOG.open("a", encoding="utf-8") as fh:
            fh.write(_hide_token(json.dumps(line, ensure_ascii=False)) + "\n")
    except OSError:
        pass


def _now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def _usage(result: dict) -> dict:
    u = result.get("usage") or {}
    return {
        "input": u.get("input_tokens", 0),
        "output": u.get("output_tokens", 0),
        "cache_read": u.get("cache_read_input_tokens", 0),
        "cache_write": u.get("cache_creation_input_tokens", 0),
        "cost_usd": result.get("total_cost_usd"),
        "turns": result.get("num_turns"),
    }


def _deny_token_rule(token_file: Path):
    # The rounds get the same "never read the token file" rule the guide puts in settings.json.
    try:
        rel = token_file.resolve().relative_to(Path.home().resolve())
    except ValueError:
        return None
    return f"Read(~/{rel.as_posix()})"


def _run_round(command, prompt, folder, env, timeout):
    # On a timeout, subprocess only kills the direct child, and the round's own tools could keep
    # the pipes open; the whole process tree started here is killed instead.
    extra = {} if os.name == "nt" else {"start_new_session": True}
    proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            cwd=folder, env=env, text=True, encoding="utf-8", errors="replace", **extra)
    try:
        out, err = proc.communicate(prompt, timeout=timeout)
    except subprocess.TimeoutExpired:
        if os.name == "nt":
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)], capture_output=True)
        else:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except OSError:
                proc.kill()
        try:
            proc.communicate(timeout=30)
        except subprocess.TimeoutExpired:
            pass
        return None
    return proc.returncode, out, err


def _stage_done(handoff: Path) -> bool:
    # Only the first non-empty line counts: the steps themselves often mention the mark.
    lines = [l for l in handoff.read_text(encoding="utf-8-sig", errors="replace").splitlines() if l.strip()]
    first = lines[0].upper() if lines else ""
    return any(mark in first for mark in DONE_MARKS)


def run(args) -> int:
    global _TOKEN
    folder = Path(args.folder).expanduser().resolve()
    handoff = Path(args.handoff).expanduser()
    if not handoff.is_absolute():
        handoff = folder / handoff
    if not folder.is_dir():
        raise SystemExit(f"Folder does not exist: {folder}")
    if not handoff.is_file():
        raise SystemExit(f"Handoff file does not exist: {handoff}")

    token_file = Path(args.token_file).expanduser()
    _TOKEN = _read_token(token_file)
    exe = _find_claude(args.claude)
    env = _child_env(_TOKEN)
    log = Path(args.log).expanduser() if args.log else folder / "relay.log"

    command = [
        str(exe), "-p",
        "--model", args.model,
        "--output-format", "json",
        "--permission-mode", args.mode,
        "--permission-prompts", "none",
        "--allowedTools", args.tools,
    ]
    deny = _deny_token_rule(token_file)
    extra_settings = None
    if deny:
        # Passed as a settings file, not as --disallowedTools: claude.cmd on Windows breaks on parentheses.
        fd, extra_settings = tempfile.mkstemp(prefix="relay_settings_", suffix=".json")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump({"permissions": {"deny": [deny]}}, fh)
        command += ["--settings", extra_settings]
    if args.effort:
        command += ["--effort", args.effort]
    for extra in args.add_dir or []:
        command += ["--add-dir", str(Path(extra).expanduser())]

    prompt = PROMPT.format(handoff=handoff, tools=args.tools)
    _log(log, {"time": _now(), "event": "start", "folder": str(folder), "handoff": str(handoff), "model": args.model,
               "mode": args.mode, "tools": args.tools, "rounds": args.rounds})
    _registry({"time": _now(), "event": "start", "folder": str(folder), "model": args.model, "rounds": args.rounds,
               "reason": args.reason, "notified": args.notified})

    reason = "round limit"
    for n in range(1, args.rounds + 1):
        if _stage_done(handoff):
            reason = "handoff file already said the stage is done"
            break

        start = time.time()
        finished = _run_round(command + ["-n", f"relay {folder.name} r{n}"], prompt, folder, env, args.timeout)
        if finished is None:
            _log(log, {"time": _now(), "round": n, "status": "TIMEOUT", "seconds": round(time.time() - start)})
            reason = f"round {n} took longer than {args.timeout} s"
            break
        returncode, stdout, stderr = finished

        seconds = round(time.time() - start)
        try:
            result = json.loads(stdout)
        except json.JSONDecodeError:
            result = {}
        summary = (result.get("result") or "").strip()
        found = STATUS_RE.findall(summary)
        status = found[-1].upper() if found else "NO_STATUS"
        denied = [d.get("tool_name") for d in (result.get("permission_denials") or [])]
        if returncode != 0 or result.get("is_error"):
            status = "ERROR"

        line = {"time": _now(), "round": n, "status": status, "seconds": seconds, "summary": summary,
                "usage": _usage(result), "session": result.get("session_id")}
        if denied:
            line["permission_denied"] = denied
        if status == "ERROR" and not result:
            line["raw_output"] = ((stdout or "")[-2000:] + "\n" + (stderr or "")[-2000:]).strip()
        _log(log, line)
        _registry({"time": _now(), "event": "round", "round": n, "status": status, "session": result.get("session_id")})
        print(_hide_token(f"[round {n}] {status} in {seconds} s\n{summary}\n"), flush=True)

        if status in ("ERROR", "NO_STATUS"):
            reason = f"round {n}: {status}"
            break
        if status == "DONE" or _stage_done(handoff):
            reason = f"round {n}: stage done"
            break
        if status == "QUESTION":
            reason = f"round {n}: question for the person (see the handoff file)"
            break
        if denied:
            # The round said it can go on without the tool; it only stays as a warning.
            print(f"  warning: permission denied for {', '.join(sorted(set(filter(None, denied))))}", flush=True)

    if extra_settings:
        try:
            os.remove(extra_settings)
        except OSError:
            pass
    _log(log, {"time": _now(), "event": "end", "reason": reason})
    _registry({"time": _now(), "event": "end", "reason": reason})
    print(f"Relay finished: {reason}. Log: {log}")
    return 0 if ("done" in reason or "limit" in reason or "question" in reason) else 1


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(description="Chains Claude Code rounds that read and update a handoff file.")
    p.add_argument("--folder", required=True, help="project folder (working directory of each round)")
    p.add_argument("--handoff", required=True, help="handoff file (absolute or relative to the folder)")
    p.add_argument("--model", default="sonnet", help="model of each round (sonnet, opus, haiku or a full name)")
    p.add_argument("--rounds", type=int, default=3, help="maximum number of rounds")
    p.add_argument("--tools", default=DEFAULT_TOOLS,
                   help='allowed tools, e.g. "Read,Glob,Grep,Edit,Write,Bash(git status:*)"')
    p.add_argument("--mode", default="dontAsk", choices=["dontAsk", "acceptEdits", "auto"],
                   help="permission mode (bypassPermissions is left out on purpose)")
    p.add_argument("--effort", choices=["low", "medium", "high", "xhigh", "max"], help="effort of each round")
    p.add_argument("--add-dir", action="append", help="extra folder the rounds may access (repeatable)")
    p.add_argument("--timeout", type=int, default=3600, help="maximum seconds per round")
    p.add_argument("--log", help="log file (default: relay.log in the project folder)")
    p.add_argument("--token-file", default=str(DEFAULT_TOKEN_FILE), help="file with the token from claude setup-token")
    p.add_argument("--claude", help="path to the claude executable (default: found in PATH)")
    p.add_argument("--reason", default="(no reason given)",
                   help="why this relay runs, in a few words; goes to the relay log read by daily_report.py")
    p.add_argument("--notified", action="store_true",
                   help="the person was told before this relay started (recorded in the relay log)")
    return run(p.parse_args())


if __name__ == "__main__":
    sys.exit(main())
