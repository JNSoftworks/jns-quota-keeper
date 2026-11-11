"""Daily report: yesterday's Claude Code use on this PC, screenless sessions and a check against the account.

Part of JN's Quota Keeper, token-saving tactics by Jaber Felippe Neto (JN Softworks).
Copyright (c) 2026 Jaber Felippe Neto (JN Softworks). SPDX-License-Identifier: MIT (full text in the guide's LICENSE.md).

Usage:
    python daily_report.py [--date YYYY-MM-DD] [--max-hours H] [--top N]
    python daily_report.py --record-account <weekly % of the account now>
    python daily_report.py --once-a-day      (SessionStart hook, matcher startup: once a day, a short reminder)
    python daily_report.py --test

What it reads (only reads; no network):
- the local session records, <config folder>/projects/**/*.jsonl (the config folder is
  CLAUDE_CONFIG_DIR if set, otherwise ~/.claude); only token counts, model, time, folder and the
  "entrypoint" field. "entrypoint" is "sdk-cli" for `claude -p` and SDK runs (no screen),
  "cli" for the terminal and "claude-desktop" for the desktop app;
- <config folder>/quota_keeper/relay_log.jsonl, written by session_relay.py;
- measure_marks.csv from measure_point.py (next to this script or in <config folder>/tools), for
  how many weighted tokens 1% of the weekly limit is worth.

What it writes (only in <config folder>/quota_keeper/):
- account_marks.csv, one line per --record-account;
- daily_asked.txt, the date of the last --once-a-day reminder.

The report: weighted tokens of the day by session and by model (same weights as
usage_report.py); screenless sessions, which of them no relay_log run explains, which ran
without a recorded warning and which ran longer than --max-hours; relay runs still alive for
longer than that; and, when two account marks surround the day, whether the account's weekly %
rose much more than this PC's records explain.

Limits: this script sees only this PC. Use on other computers, claude.ai, the phone app, or by
someone holding your token is not in these records: a gap between the account and this PC is a
hint, not proof. The record format is internal to Claude Code and may change. A PID can be
reused by another program after the relay ends, so "alive" is a best guess.

--once-a-day prints nothing if it already ran today, nor inside screenless runs. Otherwise it
marks the day and prints one line telling Claude to ask the person whether they want the
report; if a cheap check (file headers only) finds a screenless session with no recorded
warning, or one running for too long, it adds one line saying so.
"""

import os
import sys
import time


def _quick_exit():
    # The hook runs at every new session: when today's reminder was already given (or this is a
    # screenless run), stop before loading anything else.
    if os.environ.get("QUOTA_KEEPER_RELAY") or os.environ.get("CLAUDE_CODE_ENTRYPOINT", "").startswith("sdk"):
        sys.exit(0)
    base = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")
    try:
        with open(os.path.join(base, "quota_keeper", "daily_asked.txt"), encoding="utf-8") as fh:
            if fh.read().strip() == time.strftime("%Y-%m-%d"):
                sys.exit(0)
    except OSError:
        pass


if __name__ == "__main__" and sys.argv[1:2] in (["--once-a-day"], ["--remind"]):
    _quick_exit()

import argparse
import csv
import datetime as dt
import glob
import json
import shutil
import tempfile
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SCREENLESS_PREFIX = "sdk"
MIN_GAP = 3


def config_dir():
    return os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")


def state_dir(cfg):
    return os.path.join(cfg, "quota_keeper")


def weight_fn():
    # Same weights as usage_report.py; imported from it when it sits next to this script.
    if HERE not in sys.path:
        sys.path.insert(0, HERE)
    try:
        from usage_report import weight
        return weight
    except ImportError:
        raise SystemExit("usage_report.py not found next to daily_report.py; copy both from scripts/.")


def parse_ts(text):
    return dt.datetime.fromisoformat(text.replace("Z", "+00:00"))


def local_time(text):
    # session_relay.py writes local times without a zone; astimezone() reads them as local.
    t = dt.datetime.fromisoformat(text)
    return t.astimezone() if t.tzinfo is None else t


def day_bounds(day):
    start = dt.datetime.combine(day, dt.time()).astimezone()
    end = dt.datetime.combine(day + dt.timedelta(days=1), dt.time()).astimezone()
    return start, end


def family(model):
    return next((f for f in ("opus", "sonnet", "haiku") if f in model), "other")


def session_of(root, path):
    rel = os.path.relpath(path, root).split(os.sep)
    if len(rel) == 2 and rel[1].endswith(".jsonl"):
        return rel[1][:-6], True
    return (rel[1] if len(rel) > 1 else rel[0]), False


def read_header(path, max_lines=60):
    """Entrypoint, folder and first time of a session, from the first lines of its file."""
    info = {"entrypoint": None, "cwd": None, "first": None}
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for n, line in enumerate(fh):
                if n >= max_lines:
                    break
                if '"entrypoint"' not in line:
                    continue
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                info["entrypoint"] = e.get("entrypoint")
                info["cwd"] = e.get("cwd")
                if e.get("timestamp"):
                    info["first"] = parse_ts(e["timestamp"])
                break
    except OSError:
        pass
    return info


def is_screenless(entrypoint):
    return bool(entrypoint) and entrypoint.startswith(SCREENLESS_PREFIX)


# ---------------------------------------------------------------- relay log

def read_relay_runs(cfg):
    path = os.path.join(state_dir(cfg), "relay_log.jsonl")
    runs, current = [], {}
    if not os.path.isfile(path):
        return runs
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                e = json.loads(line)
                pid = e.get("pid")
                t = local_time(e["time"])
            except (ValueError, KeyError, TypeError):
                continue
            if e.get("event") == "start":
                run = {"pid": pid, "start": t, "end": None, "folder": e.get("folder") or "",
                       "reason": e.get("reason") or "", "notified": bool(e.get("notified")), "sessions": set()}
                runs.append(run)
                current[pid] = run
            elif pid in current:
                run = current[pid]
                if e.get("event") == "end":
                    run["end"] = t
                    del current[pid]
                elif e.get("session"):
                    run["sessions"].add(e["session"])
    return runs


def pid_alive(pid):
    if not isinstance(pid, int) or pid <= 0:
        return False
    if os.name == "nt":
        import ctypes
        k32 = ctypes.windll.kernel32
        handle = k32.OpenProcess(0x1000, False, pid)  # PROCESS_QUERY_LIMITED_INFORMATION
        if not handle:
            return False
        code = ctypes.c_ulong()
        ok = k32.GetExitCodeProcess(handle, ctypes.byref(code))
        k32.CloseHandle(handle)
        return bool(ok) and code.value == 259  # STILL_ACTIVE
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except OSError:
        return False
    return True


def same_folder(a, b):
    if not a or not b:
        return False
    return os.path.normcase(os.path.normpath(a)) == os.path.normcase(os.path.normpath(b))


def match_run(session_id, cwd, first, runs, now):
    """The relay run that explains a screenless session: by session id, else by folder and time."""
    for run in runs:
        if session_id in run["sessions"]:
            return run
    if first is None:
        return None
    slack = dt.timedelta(minutes=2)
    for run in runs:
        end = run["end"] or now
        if same_folder(cwd, run["folder"]) and run["start"] - slack <= first <= end + slack:
            return run
    return None


def alive_long_runs(runs, now, max_hours):
    return [r for r in runs if r["end"] is None and now - r["start"] > dt.timedelta(hours=max_hours)
            and pid_alive(r["pid"])]


# ---------------------------------------------------------------- local usage

def scan(root, start, end, weight):
    """Weighted tokens per session and per model between start and end (aware datetimes)."""
    seen = set()
    sessions = {}
    by_model = defaultdict(float)
    for path in glob.glob(os.path.join(root, "**", "*.jsonl"), recursive=True):
        try:
            if os.path.getmtime(path) < start.timestamp():
                continue
        except OSError:
            continue
        sid, top = session_of(root, path)
        s = sessions.setdefault(sid, {"weight": 0.0, "first": None, "last": None, "entrypoint": None, "cwd": None,
                                      "models": defaultdict(float)})
        if top:
            head = read_header(path)
            s["entrypoint"], s["cwd"] = head["entrypoint"], head["cwd"]
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if '"type":"assistant"' not in line:
                    continue
                try:
                    e = json.loads(line)
                    m = e.get("message") or {}
                    mid = m.get("id")
                    ts = parse_ts(e["timestamp"])
                except (ValueError, KeyError, AttributeError, TypeError):
                    continue
                if not mid or m.get("model") == "<synthetic>":
                    continue
                s["first"] = ts if s["first"] is None or ts < s["first"] else s["first"]
                s["last"] = ts if s["last"] is None or ts > s["last"] else s["last"]
                if mid in seen or not (start <= ts < end):
                    continue
                seen.add(mid)
                w = weight(m.get("usage") or {})
                model = m.get("model", "?")
                s["weight"] += w
                s["models"][model] += w
                by_model[model] += w
    active = {k: v for k, v in sessions.items() if v["weight"] > 0}
    return active, by_model


# ---------------------------------------------------------------- account marks

def account_file(cfg):
    return os.path.join(state_dir(cfg), "account_marks.csv")


def read_account_marks(cfg):
    path = account_file(cfg)
    if not os.path.isfile(path):
        return []
    with open(path, newline="", encoding="utf-8") as fh:
        rows = []
        for r in csv.DictReader(fh):
            try:
                rows.append((parse_ts(r["time_utc"]), float(r["percent"])))
            except (KeyError, ValueError):
                continue
    return rows


def record_account(cfg, percent, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    os.makedirs(state_dir(cfg), exist_ok=True)
    path = account_file(cfg)
    new = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["time_utc", "percent"])
        w.writerow([now.astimezone(dt.timezone.utc).isoformat(timespec="seconds"), percent])


def point_value(cfg):
    """Weighted tokens per 1% of the weekly limit, from measure_point.py's marks (same rule as there)."""
    for path in (os.path.join(HERE, "measure_marks.csv"), os.path.join(cfg, "tools", "measure_marks.csv")):
        if os.path.isfile(path):
            break
    else:
        return None
    with open(path, newline="", encoding="utf-8") as fh:
        marks = list(csv.DictReader(fh))
    total_w = total_g = run_w = run_g = 0.0
    for a, b in zip(marks, marks[1:]):
        try:
            gap = float(b["percent"]) - float(a["percent"])
            wb = float(b["weighted"]) if b.get("weighted") else None
        except (KeyError, ValueError):
            continue
        if gap < 0 or wb is None:
            run_w = run_g = 0.0
            continue
        run_w += wb
        run_g += gap
        if run_g >= MIN_GAP:
            total_w += run_w
            total_g += run_g
            run_w = run_g = 0.0
    return total_w / total_g if total_g else None


def account_check(cfg, root, start, end, weight, point, ratio, slack_points):
    """Compares the account's % rise between two marks around the day with what this PC explains."""
    marks = read_account_marks(cfg)
    pair = None
    for a, b in zip(marks, marks[1:]):
        if a[0] < end and b[0] > start:
            pair = (a, b)
    if not pair:
        return ["Account: no two marks around this day (record one a day with --record-account <%>)."], False
    (ta, pa), (tb, pb) = pair
    head = f"Account: {pa:g}% at {ta.astimezone():%m-%d %H:%M} -> {pb:g}% at {tb.astimezone():%m-%d %H:%M}"
    if pb < pa:
        return [head + ": the weekly limit was reset in between; no comparison."], False
    _, by_model = scan(root, ta, tb, weight)
    local = sum(by_model.values())
    rise = pb - pa
    if not point:
        return [head + f" (+{rise:g} points); this PC: {local / 1e6:.1f} M weighted. "
                "No 1% value measured yet (measure_point.py), so no comparison."], False
    explained = local / point
    lines = [head + f" (+{rise:g} points). This PC explains ~{explained:.1f} points "
             f"({local / 1e6:.1f} M weighted, 1% = ~{point / 1e6:.1f} M)."]
    odd = rise > explained * ratio + slack_points
    if odd:
        lines.append("  WARNING: the account used more than this PC explains: another computer, claude.ai, "
                     "the phone, or someone using your token. This script only sees this PC: a hint, not proof.")
    return lines, odd


# ---------------------------------------------------------------- report

def short(text, n=8):
    return (text or "?")[:n]


def folder_name(path):
    return os.path.basename(os.path.normpath(path)) if path else "?"


def hours(a, b):
    return (b - a).total_seconds() / 3600 if a and b else 0.0


def build_report(cfg, day, max_hours=8.0, top=8, now=None, point=None, ratio=1.5, slack_points=2.0):
    now = now or dt.datetime.now().astimezone()
    weight = weight_fn()
    root = os.path.join(cfg, "projects")
    start, end = day_bounds(day)
    sessions, by_model = scan(root, start, end, weight)
    total = sum(by_model.values())
    out = [f"Daily report for {day.isoformat()} (records of this PC only; estimates, not the bill)"]
    if not sessions:
        out.append("No Claude Code replies recorded on this PC that day.")
    else:
        out.append(f"Weighted tokens: {total / 1e6:.1f} M in {len(sessions)} sessions")
        for model, w in sorted(by_model.items(), key=lambda x: -x[1]):
            out.append(f"  {model}: {w / 1e6:.1f} M ({100 * w / total:.0f}%)")
        out.append(f"Heaviest sessions (id, M, kind, folder):")
        for sid, s in sorted(sessions.items(), key=lambda x: -x[1]["weight"])[:top]:
            kind = "no screen" if is_screenless(s["entrypoint"]) else (s["entrypoint"] or "?")
            out.append(f"  {short(sid)}  {s['weight'] / 1e6:6.1f} M  {kind:14} {folder_name(s['cwd'])}")

    runs = read_relay_runs(cfg)
    odd = False
    screenless = {k: v for k, v in sessions.items() if is_screenless(v["entrypoint"])}
    out.append(f"Screenless sessions (entrypoint sdk-cli: claude -p or SDK): {len(screenless)}")
    for sid, s in sorted(screenless.items(), key=lambda x: x[1]["first"] or now):
        run = match_run(sid, s["cwd"], s["first"], runs, now)
        notes = []
        if run is None:
            notes.append("NOT in relay_log (opened by something else, or before the log existed)")
        elif not run["notified"]:
            notes.append(f"relay without a recorded warning (reason: {run['reason']})")
        if hours(s["first"], s["last"]) > max_hours:
            notes.append(f"ran {hours(s['first'], s['last']):.1f} h (> {max_hours:g} h)")
        if notes:
            odd = True
        label = "; ".join(notes) if notes else f"relay, warned (reason: {run['reason']})"
        first = s["first"].astimezone() if s["first"] else None
        first = "?" if first is None else first.strftime("%H:%M" if first.date() == day else "%m-%d %H:%M")
        out.append(f"  {short(sid)}  {first}  {s['weight'] / 1e6:5.1f} M  {folder_name(s['cwd'])}: {label}")
    for r in alive_long_runs(runs, now, max_hours):
        odd = True
        out.append(f"  Relay PID {r['pid']} started {r['start']:%m-%d %H:%M} and still looks alive "
                   f"({hours(r['start'], now):.1f} h; the PID may also belong to another program now).")

    lines, account_odd = account_check(cfg, root, start, end, weight, point or point_value(cfg), ratio, slack_points)
    out += lines
    out.append("Nothing odd." if not (odd or account_odd) else "Something above deserves a look.")
    return "\n".join(out), odd or account_odd


# ---------------------------------------------------------------- once-a-day reminder

def cheap_check(cfg, now, max_hours):
    """Only file headers and modification times: headless sessions since yesterday that look odd."""
    root = os.path.join(cfg, "projects")
    since = day_bounds(now.date() - dt.timedelta(days=1))[0]
    runs = read_relay_runs(cfg)
    unexplained = long_run = 0
    for path in glob.glob(os.path.join(root, "*", "*.jsonl")):
        try:
            mtime = os.path.getmtime(path)
        except OSError:
            continue
        if mtime < since.timestamp():
            continue
        head = read_header(path)
        if not is_screenless(head["entrypoint"]):
            continue
        sid = os.path.basename(path)[:-6]
        run = match_run(sid, head["cwd"], head["first"], runs, now)
        if run is None or not run["notified"]:
            unexplained += 1
        last = dt.datetime.fromtimestamp(mtime).astimezone()
        if head["first"] and hours(head["first"], last) > max_hours:
            long_run += 1
    long_run += len(alive_long_runs(runs, now, max_hours))
    return unexplained, long_run


def reminder(cfg, now=None, max_hours=8.0, env=None):
    """Text for the SessionStart hook, or "" when it must stay quiet."""
    env = os.environ if env is None else env
    if env.get("QUOTA_KEEPER_RELAY") or (env.get("CLAUDE_CODE_ENTRYPOINT") or "").startswith(SCREENLESS_PREFIX):
        return ""
    if env.get("CLAUDE_CODE_SESSION_ATTENDED") == "0":
        return ""
    now = now or dt.datetime.now().astimezone()
    mark = os.path.join(state_dir(cfg), "daily_asked.txt")
    today = now.date().isoformat()
    try:
        with open(mark, encoding="utf-8") as fh:
            if fh.read().strip() == today:
                return ""
    except OSError:
        pass
    script = os.path.abspath(__file__).replace("\\", "/")
    lines = []
    try:
        unexplained, long_run = cheap_check(cfg, now, max_hours)
    except Exception:
        unexplained = long_run = 0
    if unexplained or long_run:
        found = []
        if unexplained:
            found.append(f"{unexplained} screenless session(s) since yesterday with no warning recorded in the relay log")
        if long_run:
            found.append(f"{long_run} running more than {max_hours:g} h")
        lines.append("Quota Keeper cheap check found: " + "; ".join(found) + ". Mention this when you ask.")
    lines.append("Quota Keeper (once a day): at the person's first message, before their request, ask them in an AskUserQuestion box, in their "
                 "language, whether they want yesterday's usage report (options: See it now / Not today). Only if they "
                 f'accept, run: python "{script}" and show its output; then carry on with their request.')
    os.makedirs(state_dir(cfg), exist_ok=True)
    with open(mark, "w", encoding="utf-8") as fh:
        fh.write(today + "\n")
    return "\n".join(lines)


# ---------------------------------------------------------------- self test

def _write_session(root, project, sid, entrypoint, cwd, start, minutes, model="claude-sonnet-x", out_tokens=1000):
    os.makedirs(os.path.join(root, project), exist_ok=True)
    path = os.path.join(root, project, sid + ".jsonl")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(json.dumps({"type": "user", "entrypoint": entrypoint, "cwd": cwd, "sessionId": sid,
                             "timestamp": start.astimezone(dt.timezone.utc).isoformat()}) + "\n")
        for i, t in enumerate((start, start + dt.timedelta(minutes=minutes))):
            fh.write(json.dumps({"type": "assistant", "timestamp": t.astimezone(dt.timezone.utc).isoformat(),
                                 "message": {"id": f"{sid}-{i}", "model": model,
                                             "usage": {"input_tokens": 0, "output_tokens": out_tokens}}},
                                separators=(",", ":")) + "\n")
    end = start + dt.timedelta(minutes=minutes)
    os.utime(path, (end.timestamp(), end.timestamp()))


def _relay(cfg, pid, start, end, folder, notified, session=None):
    os.makedirs(state_dir(cfg), exist_ok=True)
    with open(os.path.join(state_dir(cfg), "relay_log.jsonl"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"time": start.replace(tzinfo=None).isoformat(timespec="seconds"), "event": "start",
                             "pid": pid, "folder": folder, "reason": "test", "notified": notified}) + "\n")
        if session:
            fh.write(json.dumps({"time": start.replace(tzinfo=None).isoformat(timespec="seconds"), "event": "round",
                                 "pid": pid, "round": 1, "session": session}) + "\n")
        if end:
            fh.write(json.dumps({"time": end.replace(tzinfo=None).isoformat(timespec="seconds"), "event": "end",
                                 "pid": pid, "reason": "done"}) + "\n")


def selftest():
    ok = True

    def check(name, cond):
        nonlocal ok
        ok = ok and bool(cond)
        print(f"{'ok  ' if cond else 'FAIL'} {name}")

    base = tempfile.mkdtemp(prefix="daily_report_test_")
    try:
        cfg = os.path.join(base, "cfg")
        root = os.path.join(cfg, "projects")
        os.makedirs(root)
        now = dt.datetime.now().astimezone().replace(hour=12, minute=0, second=0, microsecond=0)
        day = now.date() - dt.timedelta(days=1)
        y = dt.datetime.combine(day, dt.time(9, 0)).astimezone()
        quiet = {}

        text, odd = build_report(cfg, day, now=now)
        check("no data: report says so and nothing odd", "No Claude Code replies" in text and not odd)
        check("no data: reminder is one line", reminder(cfg, now=now, env=quiet).count("\n") == 0)
        check("reminder only once a day", reminder(cfg, now=now, env=quiet) == "")
        check("reminder quiet inside a relay round",
              reminder(cfg, now=now + dt.timedelta(days=1), env={"QUOTA_KEEPER_RELAY": "1"}) == "")

        proj_a, proj_b = os.path.join(base, "work_a"), os.path.join(base, "work_b")
        _write_session(root, "p1", "aaaa0001", "claude-desktop", proj_a, y, 30)
        _write_session(root, "p2", "bbbb0002", "sdk-cli", proj_b, y + dt.timedelta(hours=1), 20)
        _relay(cfg, 999991, y + dt.timedelta(minutes=59), y + dt.timedelta(hours=2), proj_b, True, "bbbb0002")
        text, odd = build_report(cfg, day, now=now)
        check("relay with warning in relay_log: matched, nothing odd", "relay, warned" in text and not odd)
        check("report sums by model", "claude-sonnet-x" in text and "2 sessions" in text)

        _write_session(root, "p2", "cccc0003", "sdk-cli", proj_b, y + dt.timedelta(hours=5), 10)
        text, odd = build_report(cfg, day, now=now)
        check("relay_log absent for a screenless session: flagged", "NOT in relay_log" in text and odd)

        _write_session(root, "p3", "dddd0004", "sdk-cli", proj_a, y - dt.timedelta(hours=8), 12 * 60)
        _relay(cfg, 999992, y - dt.timedelta(hours=8, minutes=1), None, proj_a, False)
        text, odd = build_report(cfg, day, now=now)
        check("relay without --notified: flagged", "without a recorded warning" in text)
        check("long session: flagged", "ran 12.0 h" in text)

        _relay(cfg, os.getpid(), now - dt.timedelta(hours=10), None, proj_a, True)
        text, odd = build_report(cfg, day, now=now)
        check("relay PID alive for too long: flagged", f"Relay PID {os.getpid()}" in text)

        os.remove(os.path.join(state_dir(cfg), "daily_asked.txt"))
        hint = reminder(cfg, now=now, env=quiet)
        check("reminder names the odd sessions in one extra line",
              hint.startswith("Quota Keeper cheap check found") and hint.count("\n") == 1)

        text, _ = build_report(cfg, day, now=now, point=1e6)
        check("no account marks: says how to record", "--record-account" in text)
        record_account(cfg, 10, y - dt.timedelta(hours=10))
        record_account(cfg, 40, y + dt.timedelta(hours=14))
        text, odd = build_report(cfg, day, now=now, point=1e6)
        check("account rises more than this PC explains: warns", "WARNING: the account used more" in text and odd)
        text, _ = build_report(cfg, day, now=now, point=1000)
        check("account rise explained by this PC: no warning", "WARNING" not in text)
        record_account(cfg, 5, y + dt.timedelta(hours=15))
        text, _ = build_report(cfg, day, now=now, point=1e6)
        check("weekly reset between marks: no comparison", "reset in between" in text)
    finally:
        shutil.rmtree(base, ignore_errors=True)
    print("ALL OK" if ok else "FAILED")
    return 0 if ok else 1


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Yesterday's Claude Code use on this PC, screenless sessions and a "
                                             "check against the account's weekly %. Only reads local files.")
    ap.add_argument("--date", help="day to report, YYYY-MM-DD (default: yesterday)")
    ap.add_argument("--max-hours", type=float, default=8.0, help="flag screenless sessions longer than this (default 8)")
    ap.add_argument("--top", type=int, default=8, help="heaviest sessions to list (default 8)")
    ap.add_argument("--point", type=float, help="weighted tokens per 1%% of the weekly limit "
                                                "(default: from measure_point.py's marks)")
    ap.add_argument("--record-account", metavar="PCT", help="record the account's weekly %% now and stop")
    ap.add_argument("--once-a-day", "--remind", dest="once", action="store_true",
                    help="hook mode: once a day, a short reminder to ask the person about the report")
    ap.add_argument("--test", action="store_true", help="run the self test on made-up data")
    args = ap.parse_args()
    cfg = config_dir()
    if args.test:
        return selftest()
    if args.once:
        try:
            if not sys.stdin.isatty():
                sys.stdin.read()
            text = reminder(cfg, max_hours=args.max_hours)
            if text:
                print(text)
        except Exception:
            pass
        return 0
    if args.record_account:
        percent = float(args.record_account.replace(",", ".").rstrip("%"))
        record_account(cfg, percent)
        print(f"Account mark saved ({percent:g}%) in {account_file(cfg)}")
        return 0
    day = dt.date.fromisoformat(args.date) if args.date else dt.date.today() - dt.timedelta(days=1)
    text, _ = build_report(cfg, day, max_hours=args.max_hours, top=args.top, point=args.point)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
