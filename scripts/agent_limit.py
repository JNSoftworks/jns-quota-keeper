"""Agent limit: a Claude Code PreToolUse hook (matcher "Agent|Task") that stops endless agent chains.

Part of JN's Quota Keeper, token-saving tactics by Jaber Neto (JN Softworks).
Copyright (c) 2026 Jaber Neto (JN Softworks). SPDX-License-Identifier: MIT (full text in the guide's LICENSE.md).

Main conversation = level 0, an agent it opens = level 1, an agent opened by an agent = level 2.
Level 2 opens nobody, and each agent opens at most MAX_CHILDREN agents.

It reads the sub-agents' *.meta.json files, which are internal to Claude Code and may change;
if they do, it stops braking but never blocks anything by mistake.
"""

import glob
import json
import os
import sys

MAX_LEVEL = 2
MAX_CHILDREN = 6


def main():
    try:
        data = json.loads(sys.stdin.buffer.read().decode("utf-8", errors="replace"))
        me = str(data.get("agent_id") or "")
        transcript = data.get("transcript_path") or ""
        if not me or not transcript:
            return
        folder = os.path.join(transcript[:-6], "subagents")
        level = 1
        children = 0
        for meta in glob.glob(os.path.join(folder, "*.meta.json")):
            try:
                with open(meta, encoding="utf-8") as fh:
                    m = json.load(fh)
            except (OSError, ValueError):
                continue
            name = os.path.basename(meta)[:-10]
            if name in (f"agent-{me}", me):
                level = int(m.get("spawnDepth") or 1)
            if str(m.get("parentAgentId") or "") == me:
                children += 1
        reason = None
        if level >= MAX_LEVEL:
            reason = (f"Agent limit: you are a level {level} agent, and agents at this level don't open other agents "
                      "(brake against endless chains). Do the work yourself or return what is left to your coordinator.")
        elif children >= MAX_CHILDREN:
            reason = (f"Agent limit: you have already opened {children} agents (maximum {MAX_CHILDREN}). "
                      "Finish with what you have and return the summary.")
    except Exception:
        return
    if reason:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                                 "permissionDecisionReason": reason}}))


if __name__ == "__main__":
    main()
