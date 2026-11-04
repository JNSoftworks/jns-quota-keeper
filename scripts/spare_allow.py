"""Spare allow: a Claude Code PreToolUse hook (matcher "SendMessage|mcp__ccd_session_mgmt__.*") for spare sessions.

Part of JN's Quota Keeper, token-saving tactics by Jaber Felippe Neto (JN Softworks).
Copyright (c) 2026 Jaber Felippe Neto (JN Softworks). SPDX-License-Identifier: MIT (full text in the guide's LICENSE.md).

It approves, without the auto mode classifier, only the session actions used at a switch
(unarchive, title, model, effort, Remote Control, message) whose target is a spare listed in
<config folder>/spares.txt (one session id per line; text after "#" is ignored).
Any other target follows the normal path (rules, classifier, approval).
Each decision goes to <config folder>/hooks/spare_allow.log.
"""

import json
import os
import sys
from datetime import datetime

CONFIG = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")
LIST_FILE = os.path.join(CONFIG, "spares.txt")
LOG_FILE = os.path.join(CONFIG, "hooks", "spare_allow.log")

TARGET_FIELD = {
    "SendMessage": "to",
    "mcp__ccd_session_mgmt__unarchive_session": "session_id",
    "mcp__ccd_session_mgmt__set_session_title": "session_id",
    "mcp__ccd_session_mgmt__set_session_effort": "session_id",
    "mcp__ccd_session_mgmt__set_session_model": "session_id",
    "mcp__ccd_session_mgmt__set_remote_control": "session_id",
}


def read_spares():
    try:
        with open(LIST_FILE, encoding="utf-8") as f:
            return {line.split("#")[0].strip() for line in f if line.split("#")[0].strip()}
    except OSError:
        return set()


def log(text):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} {text}\n")
    except OSError:
        pass


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    tool = data.get("tool_name", "")
    field = TARGET_FIELD.get(tool)
    if not field:
        return
    target = str((data.get("tool_input") or {}).get(field, "")).strip().split(" ")[0]
    if target and target in read_spares():
        log(f"ALLOWED {tool} -> {target}")
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow",
                "permissionDecisionReason": "target is a spare listed in spares.txt",
            }
        }))
    else:
        log(f"normal {tool} -> {target or '?'}")


if __name__ == "__main__":
    main()
