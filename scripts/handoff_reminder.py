"""Handoff reminder: a Claude Code SessionStart hook that reminds Claude to read the project's handoff file first.

Part of JN's Quota Keeper, token-saving tactics by Jaber Felippe Neto (JN Softworks).
Copyright (c) 2026 Jaber Felippe Neto (JN Softworks). SPDX-License-Identifier: MIT (full text in the guide's LICENSE.md).

If the folder the session opened in holds a handoff file (PASSAGEM*.md or HANDOFF*.md), it prints ONE line
naming it. Claude Code adds what a SessionStart hook prints to the start of the conversation.
It only lists the folder; it reads no file, writes nothing and uses no network. On any error it prints nothing.

Usage: python handoff_reminder.py [--help | --test | <folder>]
With no argument it reads the hook data from stdin (field "cwd").
"""

import glob
import json
import os
import sys
import tempfile

PATTERNS = ("PASSAGEM*.md", "HANDOFF*.md")
SKIP = ("MODELO", "TEMPLATE")


def find(folder):
    found = []
    for pattern in PATTERNS:
        for path in glob.glob(os.path.join(folder, pattern)):
            name = os.path.basename(path)
            if os.path.isfile(path) and not any(word in name.upper() for word in SKIP):
                found.append(name)
    return sorted(set(found))


def line(folder):
    names = find(folder)
    if not names:
        return ""
    return ("Handoff file found in this folder: " + ", ".join(names)
            + ". Read it first and do its exact next step before anything else (irreversible actions still need confirmation).")


def selftest():
    base = tempfile.mkdtemp(prefix="handoff_reminder_test_")
    ok = line(base) == ""
    print(f"{'ok  ' if ok else 'FAIL'} empty folder prints nothing")
    for name in ("HANDOFF.md", "PASSAGEM_X.md", "HANDOFF_TEMPLATE.md", "notes.md"):
        open(os.path.join(base, name), "w").close()
    text = line(base)
    good = "HANDOFF.md" in text and "PASSAGEM_X.md" in text and "TEMPLATE" not in text and "notes" not in text
    print(f"{'ok  ' if good else 'FAIL'} finds handoff files, ignores templates and other notes")
    ok = ok and good
    for name in os.listdir(base):
        os.remove(os.path.join(base, name))
    os.rmdir(base)
    print("ALL OK" if ok else "FAILED")
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if args and args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if args and args[0] == "--test":
        return selftest()
    try:
        if args:
            folder = args[0]
        else:
            data = json.loads(sys.stdin.buffer.read().decode("utf-8", errors="replace"))
            folder = data.get("cwd") or ""
        text = line(folder) if folder and os.path.isdir(folder) else ""
        if text:
            sys.stdout.reconfigure(encoding="utf-8")
            print(text)
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
