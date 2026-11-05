"""Copy lock: a Claude Code hook (PreToolUse matcher "Bash|PowerShell|Edit|Write|NotebookEdit|MultiEdit|Agent|Task" + SubagentStop) that keeps agents of two sessions off the same working copy.

Part of JN's Quota Keeper, token-saving tactics by Jaber Felippe Neto (JN Softworks).
Copyright (c) 2026 Jaber Felippe Neto (JN Softworks). SPDX-License-Identifier: MIT (full text in the guide's LICENSE.md).

A working copy is the nearest folder (walking up) holding .git, .p4config or a *.uproject.
A sub-agent that writes in a copy (Bash/PowerShell that is not read-only, Edit, Write...) takes the lock of that copy
for its SESSION; other agents of the same session join in. Any other session that tries to write there, or to open
an agent whose prompt names a path inside the copy, is denied while the lock is alive. Reading and .md/.txt files pass.
The lock goes away when the last agent returns with nothing running in the background (SubagentStop), when the owner
Claude process is gone, or after 2 hours without any sign of the agents.

Usage: python copy_lock.py list | release <folder> | test
Locks live in <config folder>/locks, decisions go to <config folder>/hooks/copy_lock.log.
On any error the hook lets everything pass.
"""

import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

CONFIG = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")
LOCKS = os.path.join(CONFIG, "locks")
LOG_FILE = os.path.join(CONFIG, "hooks", "copy_lock.log")
STALE_AFTER = 2 * 3600
WINDOWS = os.name == "nt"
WRITE_TOOLS = {"Edit", "Write", "NotebookEdit", "MultiEdit"}
COMMAND_TOOLS = {"Bash", "PowerShell"}
NOTES = (".md", ".txt")
READ_ONLY = {"ls", "dir", "cat", "head", "tail", "grep", "rg", "find", "wc", "type", "echo", "pwd", "stat", "file", "du",
             "get-content", "get-childitem", "select-string", "test-path", "get-item", "measure-object", "sort", "uniq",
             "diff", "sleep", "start-sleep", "which", "where", "tree"}
GIT_READ_ONLY = {"status", "log", "diff", "show", "branch", "rev-parse", "ls-files", "blame", "remote", "describe", "config"}
P4_READ_ONLY = {"opened", "changes", "describe", "info", "where", "have", "fstat", "status", "files", "filelog", "clients",
                "client", "diff", "print", "dirs", "changelists", "workspaces"}

if WINDOWS:
    import ctypes
    from ctypes import wintypes

    class ProcessEntry(ctypes.Structure):
        _fields_ = [("dwSize", wintypes.DWORD), ("cntUsage", wintypes.DWORD), ("th32ProcessID", wintypes.DWORD),
                    ("th32DefaultHeapID", ctypes.c_void_p), ("th32ModuleID", wintypes.DWORD),
                    ("cntThreads", wintypes.DWORD), ("th32ParentProcessID", wintypes.DWORD),
                    ("pcPriClassBase", ctypes.c_long), ("dwFlags", wintypes.DWORD), ("szExeFile", ctypes.c_wchar * 260)]


def windows_processes():
    k = ctypes.windll.kernel32
    k.CreateToolhelp32Snapshot.restype = wintypes.HANDLE
    snap = k.CreateToolhelp32Snapshot(2, 0)
    entry = ProcessEntry()
    entry.dwSize = ctypes.sizeof(ProcessEntry)
    table = {}
    more = k.Process32FirstW(snap, ctypes.byref(entry))
    while more:
        table[entry.th32ProcessID] = (entry.th32ParentProcessID, entry.szExeFile.lower())
        more = k.Process32NextW(snap, ctypes.byref(entry))
    k.CloseHandle(snap)
    return table


def created_at(pid):
    try:
        if WINDOWS:
            k = ctypes.windll.kernel32
            k.OpenProcess.restype = wintypes.HANDLE
            handle = k.OpenProcess(0x1000, False, pid)
            if not handle:
                return None
            times = [wintypes.FILETIME() for _ in range(4)]
            ok = k.GetProcessTimes(handle, *[ctypes.byref(t) for t in times])
            k.CloseHandle(handle)
            return (times[0].dwHighDateTime << 32) | times[0].dwLowDateTime if ok else None
        try:
            with open(f"/proc/{pid}/stat", encoding="utf-8", errors="replace") as f:
                return f.read().rsplit(")", 1)[1].split()[19]
        except (OSError, IndexError):
            pass
        out = subprocess.run(["ps", "-o", "lstart=", "-p", str(pid)], capture_output=True, text=True, timeout=5).stdout
        return out.strip() or None
    except Exception:
        return None


def posix_parent(pid):
    out = subprocess.run(["ps", "-o", "ppid=,comm=", "-p", str(pid)], capture_output=True, text=True, timeout=5).stdout
    parts = out.strip().split(None, 1)
    if len(parts) < 2:
        return None, ""
    return int(parts[0]), os.path.basename(parts[1].strip()).lower()


def claude_process():
    """(pid, creation time) of the Claude process above this hook, or (None, None)."""
    try:
        pid = os.getpid()
        if WINDOWS:
            table = windows_processes()
            for _ in range(25):
                if pid not in table:
                    break
                parent, name = table[pid]
                if name.startswith("claude"):
                    return pid, created_at(pid)
                pid = parent
            return None, None
        for _ in range(25):
            parent, name = posix_parent(pid)
            if parent is None:
                break
            if name.startswith("claude"):
                created = created_at(pid)
                return (pid, created) if created else (None, None)
            pid = parent
    except Exception:
        pass
    return None, None


def normal(path):
    if WINDOWS:
        m = re.match(r"^/([a-zA-Z])(/.*)?$", path)
        if m:
            path = m.group(1) + ":" + (m.group(2) or "/")
    else:
        path = os.path.expanduser(path)
    path = os.path.normpath(path)
    return path[0].upper() + path[1:] if path[1:2] == ":" else path


def find_paths(text):
    if WINDOWS:
        found = re.findall(r"[\"']([A-Za-z]:[\\/][^\"']*)[\"']", text)
        found += re.findall(r"(?<![\w/])([A-Za-z]:[\\/][^\s\"'<>|;&*?`]*)", text)
        found += re.findall(r"(?<![\w.:/-])(/[a-zA-Z]/[^\s\"'<>|;&*?`]*)", text)
    else:
        found = re.findall(r"[\"']((?:/|~/)[^\"']*)[\"']", text)
        found += re.findall(r"(?<![\w.:/-])(/[^\s\"'<>|;&*?`]+)", text)
        found += re.findall(r"(?<![\w.:/~-])(~/[^\s\"'<>|;&*?`]*)", text)
    return [normal(p.rstrip(".,)")) for p in found]


def copy_root(path):
    config = os.path.normcase(os.path.normpath(CONFIG))
    here = os.path.normcase(path)
    if here == config or here.startswith(config + os.sep):
        return None
    current = path
    while current and not os.path.isdir(current):
        up = os.path.dirname(current)
        if up == current:
            return None
        current = up
    for _ in range(14):
        try:
            names = os.listdir(current)
        except OSError:
            return None
        if ".git" in names or ".p4config" in names or any(n.lower().endswith(".uproject") for n in names):
            return current
        up = os.path.dirname(current)
        if up == current:
            return None
        current = up
    return None


def lock_file(copy, folder=None):
    digest = hashlib.sha1(os.path.normcase(copy).encode("utf-8")).hexdigest()[:16]
    return os.path.join(folder or LOCKS, digest + ".json")


def read_lock(copy):
    try:
        with open(lock_file(copy), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def write_lock(path, lock):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(lock, f, ensure_ascii=False)


def alive(lock):
    if not lock:
        return False
    pid = lock.get("pid")
    if pid and created_at(pid) != lock.get("pid_created"):
        return False
    last = lock.get("last", 0)
    for transcript in (lock.get("agents") or {}).values():
        try:
            last = max(last, os.path.getmtime(transcript))
        except OSError:
            pass
    return time.time() - last < STALE_AFTER


def root_agent(transcript, agent):
    if not agent or not transcript:
        return agent
    folder = os.path.join(transcript[:-6], "subagents")
    parents = {}
    for meta in glob.glob(os.path.join(folder, "*.meta.json")):
        try:
            with open(meta, encoding="utf-8") as f:
                m = json.load(f)
        except (OSError, ValueError):
            continue
        name = os.path.basename(meta)[:-10]
        name = name[6:] if name.startswith("agent-") else name
        parents[name] = str(m.get("parentAgentId") or "")
    current = agent
    for _ in range(10):
        parent = parents.get(current, "")
        if not parent:
            return current
        current = parent
    return current


def read_only(command):
    for part in re.split(r"&&|\|\||;|\||\n", command):
        words = [w for w in part.strip().split() if not re.match(r"^\w+=", w)]
        if not words:
            continue
        verb = os.path.basename(words[0].strip("\"'")).lower()
        verb = verb[:-4] if verb.endswith(".exe") else verb
        if "copy_lock.py" in part:
            continue
        if verb in ("git", "p4"):
            rest = [w for w in words[1:] if not w.startswith("-")]
            if verb == "git" and words[1:2] == ["-C"]:
                rest = [w for w in words[3:] if not w.startswith("-")]
            if not rest or rest[0].lower() not in (GIT_READ_ONLY if verb == "git" else P4_READ_ONLY):
                return False
        elif verb == "cd" or verb == "set-location":
            continue
        elif verb not in READ_ONLY:
            return False
        if re.search(r"(?<![0-9&])>", part):
            return False
    return True


def log(text):
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S ") + text + "\n")
    except OSError:
        pass


def deny(reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                             "permissionDecisionReason": reason}}))


def before(data):
    tool = data.get("tool_name") or ""
    tool_input = data.get("tool_input") or {}
    session = data.get("session_id") or ""
    agent = str(data.get("agent_id") or "")
    transcript = data.get("transcript_path") or ""
    if tool in COMMAND_TOOLS:
        text = str(tool_input.get("command") or "")
        paths = find_paths(text)
        if data.get("cwd"):
            paths.append(normal(data["cwd"]))
        writes = not read_only(text)
    elif tool in WRITE_TOOLS:
        target = str(tool_input.get("file_path") or tool_input.get("notebook_path") or "")
        paths = [normal(target)] if target else []
        writes = not target.lower().endswith(NOTES)
    elif tool in ("Agent", "Task"):
        paths = find_paths(str(tool_input.get("prompt") or "") + " " + str(tool_input.get("description") or ""))
        writes = True
    else:
        return
    if not writes:
        return
    copies = {}
    for p in paths:
        root = copy_root(p)
        if root:
            copies[os.path.normcase(root)] = root
    if not copies:
        return
    root_id = root_agent(transcript, agent)
    for copy in copies.values():
        lock = read_lock(copy)
        if alive(lock):
            if lock.get("session") == session:
                continue
            since = time.strftime("%H:%M", time.localtime(lock.get("since", 0)))
            agents = ", ".join(lock.get("agents") or {})
            reason = (f"Copy lock on {copy}: agent(s) of session {lock.get('session')} ({agents}) have been working "
                      f"on it since {since}. Agents of two sessions on the same copy at the same time is not allowed. "
                      "Do not relaunch the work on top of it: wait for the lock to go away (it goes when the agent "
                      "returns or when the owner session is closed or archived) or ask the owner session to stop its "
                      "agent. Reading and editing .md/.txt files is still allowed. If you are sure the agent already "
                      f"finished: python \"{os.path.abspath(__file__)}\" release \"{copy}\".")
            log(f"DENIED {tool} session={session} agent={agent or '-'} copy={copy} owner={lock.get('session')}/{agents}")
            deny(reason)
            return
    if not agent or tool in ("Agent", "Task"):
        return
    pid, created = claude_process()
    os.makedirs(LOCKS, exist_ok=True)
    for copy in copies.values():
        lock = read_lock(copy)
        if not alive(lock):
            lock = {"copy": copy, "session": session, "agents": {}, "pid": pid, "pid_created": created,
                    "since": time.time()}
        if root_id not in lock["agents"]:
            lock["agents"][root_id] = os.path.join(transcript[:-6], "subagents", f"agent-{root_id}.jsonl")
            log(f"TOOK {copy} session={session} agent={root_id} pid={pid}")
        lock["last"] = time.time()
        write_lock(lock_file(copy), lock)


def stopped(data):
    session = data.get("session_id") or ""
    agent = str(data.get("agent_id") or "")
    if not agent:
        return
    running = [t for t in data.get("background_tasks") or [] if str(t.get("status")) in ("running", "pending")]
    for path in glob.glob(os.path.join(LOCKS, "*.json")):
        try:
            with open(path, encoding="utf-8") as f:
                lock = json.load(f)
        except (OSError, ValueError):
            continue
        if lock.get("session") == session and agent in (lock.get("agents") or {}):
            if running:
                lock["last"] = time.time()
                write_lock(path, lock)
                log(f"KEPT {lock.get('copy')} agent={agent}: stopped while {len(running)} background task(s) run")
                continue
            del lock["agents"][agent]
            if lock["agents"]:
                write_lock(path, lock)
                log(f"LEFT {lock.get('copy')} agent={agent}; still there: {', '.join(lock['agents'])}")
                continue
            os.remove(path)
            log(f"RELEASED {lock.get('copy')} session={session} agent={agent} (agent returned with nothing running)")


def cli(args):
    if args[0] == "list":
        found = False
        for path in glob.glob(os.path.join(LOCKS, "*.json")):
            try:
                with open(path, encoding="utf-8") as f:
                    lock = json.load(f)
            except (OSError, ValueError):
                continue
            found = True
            since = time.strftime("%Y-%m-%d %H:%M", time.localtime(lock.get("since", 0)))
            print(f"{'ALIVE' if alive(lock) else 'dead '} {lock.get('copy')} | session {lock.get('session')} | "
                  f"agents {', '.join(lock.get('agents') or {})} | since {since}")
        if not found:
            print("no locks")
    elif args[0] == "release" and len(args) > 1:
        root = copy_root(normal(args[1])) or normal(args[1])
        try:
            os.remove(lock_file(root))
            log(f"RELEASED {root} (manual)")
            print(f"lock on {root} released")
        except OSError:
            print(f"no lock on {root}")
    elif args[0] == "test" and len(args) == 1:
        return selftest()
    else:
        print(__doc__)
    return 0


def selftest():
    base = tempfile.mkdtemp(prefix="copy_lock_test_")
    config = os.path.join(base, "config")
    copy = os.path.join(base, "copy")
    other = os.path.join(base, "other")
    for folder in (config, os.path.join(copy, ".git"), os.path.join(copy, "src"), other,
                   os.path.join(base, "sessionA", "subagents")):
        os.makedirs(folder, exist_ok=True)
    subagents = os.path.join(base, "sessionA", "subagents")
    for name, meta in (("coord1", {"spawnDepth": 1}), ("other1", {"spawnDepth": 1}),
                       ("sonnet1", {"spawnDepth": 2, "parentAgentId": "coord1"})):
        with open(os.path.join(subagents, f"agent-{name}.meta.json"), "w", encoding="utf-8") as f:
            json.dump(meta, f)
    ta = os.path.join(base, "sessionA.jsonl")
    tb = os.path.join(base, "sessionB.jsonl")
    env = dict(os.environ, CLAUDE_CONFIG_DIR=config)
    src_a, src_b, src_c = (os.path.join(copy, "src", n) for n in ("a.cpp", "b.cpp", "c.cpp"))
    if WINDOWS:
        drive, rest = os.path.splitdrive(copy)
        bash_copy = "/" + drive[0].lower() + rest.replace("\\", "/")
    else:
        bash_copy = copy
    state = {"ok": True}

    def run(data):
        r = subprocess.run([sys.executable, os.path.abspath(__file__)], input=json.dumps(data).encode(),
                           capture_output=True, env=env)
        return "denied" if b"deny" in r.stdout else "passes"

    def pre(session, transcript, agent, tool, tool_input, cwd=base):
        data = {"hook_event_name": "PreToolUse", "session_id": session, "transcript_path": transcript,
                "tool_name": tool, "tool_input": tool_input, "cwd": cwd}
        if agent:
            data["agent_id"] = agent
        return run(data)

    def stop(agent, running=False):
        tasks = [{"id": "b1", "type": "shell", "status": "running" if running else "completed"}]
        run({"hook_event_name": "SubagentStop", "session_id": "A", "transcript_path": ta, "agent_id": agent,
             "background_tasks": tasks})

    def edit_b():
        return pre("B", tb, "", "Edit", {"file_path": src_a})

    def case(name, got, expected):
        passed = got == expected
        state["ok"] = state["ok"] and passed
        print(f"{'ok  ' if passed else 'FAIL'} {name}: {got} (expected {expected})")

    try:
        subprocess.run([sys.executable, os.path.abspath(__file__), "release", copy], capture_output=True, env=env)
        case("1 agent of session A writes (takes the lock)",
             pre("A", ta, "coord1", "Bash", {"command": f'echo x > "{src_a}"'}), "passes")
        case("2 sub-agent child of the coordinator writes", pre("A", ta, "sonnet1", "Edit", {"file_path": src_b}), "passes")
        case("3 another agent of session A joins in", pre("A", ta, "other1", "Write", {"file_path": src_c}), "passes")
        case("4 session A main conversation opens one more agent",
             pre("A", ta, "", "Agent", {"prompt": f"Continue in {copy}"}), "passes")
        case("5 session B main conversation edits a source file", edit_b(), "denied")
        case("6 session B opens an agent with the path in the prompt",
             pre("B", tb, "", "Agent", {"prompt": f"Run the test in {copy}"}), "denied")
        case("7 agent of session B runs a script in the copy",
             pre("B", tb, "x9", "Bash", {"command": bash_copy + "/run.sh --all"}), "denied")
        case("8 session B only reads (git status, cat)",
             pre("B", tb, "", "Bash", {"command": f'git -C "{copy}" status && cat {src_a}'}), "passes")
        case("9 session B edits a .md in the copy",
             pre("B", tb, "", "Write", {"file_path": os.path.join(copy, "NOTES.md")}), "passes")
        case("10 session B writes in another folder",
             pre("B", tb, "", "Bash", {"command": "echo y > " + os.path.join(other, "z.txt")}), "passes")
        case("11 session B with cwd inside the copy, relative command",
             pre("B", tb, "", "Bash", {"command": "make all"}, cwd=os.path.join(copy, "src")), "denied")
        case("12 session B calls this hook's own CLI",
             pre("B", tb, "", "Bash", {"command": f'python "{os.path.abspath(__file__)}" list'}), "passes")
        stop("sonnet1")
        case("13 child returns: lock stays (coordinator alive)", edit_b(), "denied")
        stop("other1")
        case("14 other agent returns: lock stays (coordinator alive)", edit_b(), "denied")
        stop("coord1", running=True)
        case("15 coordinator stops waiting on a background task: lock stays", edit_b(), "denied")
        stop("coord1")
        case("16 coordinator returns with nothing running: lock goes away", edit_b(), "passes")
        pre("A", ta, "coord1", "Bash", {"command": f'echo x > "{src_a}"'})
        path = lock_file(copy, os.path.join(config, "locks"))
        with open(path, encoding="utf-8") as f:
            lock = json.load(f)
        lock["pid"] = 2 ** 30 + 7
        lock["pid_created"] = 1
        write_lock(path, lock)
        case("17 owner process gone: lock goes away", edit_b(), "passes")
    except Exception as error:
        state["ok"] = False
        print(f"FAIL test error: {error!r}")
    finally:
        shutil.rmtree(base, ignore_errors=True)
    print("ALL OK" if state["ok"] else "FAILED")
    return 0 if state["ok"] else 1


def main():
    if len(sys.argv) > 1:
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
        sys.exit(cli(sys.argv[1:]))
    try:
        data = json.loads(sys.stdin.buffer.read().decode("utf-8", errors="replace"))
        event = data.get("hook_event_name")
        if event == "PreToolUse":
            before(data)
        elif event == "SubagentStop":
            stopped(data)
    except Exception as error:
        log(f"ERROR {error!r}")


if __name__ == "__main__":
    main()
