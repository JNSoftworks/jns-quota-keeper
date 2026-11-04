"""Spend watch: a Claude Code hook that warns Claude when a session is getting expensive.

Part of JN's Quota Keeper, token-saving tactics by Jaber Felippe Neto (JN Softworks).
Copyright (c) 2026 Jaber Felippe Neto (JN Softworks). SPDX-License-Identifier: MIT (full text in the guide's LICENSE.md).

Install it on UserPromptSubmit and PostToolUse. It reads the session transcript (and its
sub-agents' transcripts), keeps a small state file per session next to this script, and
injects a one-line warning into Claude's context the first time each limit is crossed.

The transcript format is internal to Claude Code and may change; on any error it stays silent.
"""

import glob
import json
import os
import re
import sys

PROMPTS = [40, 80, 150]
CONTEXT_START = 200_000
CONTEXT_STEP = 100_000
AGENT_CALLS = [100, 150]
AGENT_CONTEXT = 250_000

# Weighted tokens that make up 1% of the weekly limit on your plan (measure it with
# measure_point.py). While it is None, there are no warnings in % of the plan.
POINT = None
POINTS = [10, 25, 50]
AGENTS_MIN_WEIGHTED = 15e6
AGENTS_OPUS_SHARE = 0.7

TEST_MARK = b"SPEND-WATCH-TEST"
STATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spend_watch_state")
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)


def cache_write(u):
    # The 5-minute cache writes at 1.25x; the 1-hour cache writes at 2x.
    d = u.get("cache_creation") or {}
    h1 = d.get("ephemeral_1h_input_tokens") or 0
    total = u.get("cache_creation_input_tokens") or 0
    return 2.0 * h1 + 1.25 * max(total - h1, 0)


def weight(u):
    return ((u.get("input_tokens") or 0) + cache_write(u)
            + 0.1 * (u.get("cache_read_input_tokens") or 0) + 5 * (u.get("output_tokens") or 0))


def context_size(u):
    return (u.get("input_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0) + (u.get("cache_read_input_tokens") or 0)


def read_new(path, info, main):
    # Reads only the bytes added since the last run; a message is counted once per message id.
    offset = info.get("offset", 0)
    if os.path.getsize(path) < offset:
        offset = 0
        info.clear()
    with open(path, "rb") as fh:
        fh.seek(offset)
        for raw in fh:
            if not raw.endswith(b"\n"):
                break
            offset += len(raw)
            if b'"type":"assistant"' in raw:
                try:
                    e = json.loads(raw)
                except ValueError:
                    continue
                m = e.get("message") or {}
                mid = m.get("id")
                model = m.get("model") or "?"
                if not mid or mid == info.get("last_id") or model == "<synthetic>":
                    continue
                info["last_id"] = mid
                u = m.get("usage") or {}
                w = weight(u)
                info["weight"] = info.get("weight", 0) + w
                info["calls"] = info.get("calls", 0) + 1
                if "opus" in model:
                    info["weight_opus"] = info.get("weight_opus", 0) + w
                if not main or not e.get("isSidechain"):
                    info["context"] = context_size(u)
            elif main and b'"type":"user"' in raw and b'"tool_result"' not in raw:
                try:
                    e = json.loads(raw)
                except ValueError:
                    continue
                if e.get("type") != "user" or e.get("isSidechain") or e.get("isMeta") or e.get("isCompactSummary"):
                    continue
                c = (e.get("message") or {}).get("content")
                if isinstance(c, list):
                    c = "\n".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
                t = REMINDER.sub("", c or "").strip()
                if t and not t.startswith(("<", "[Request interrupted", "Caveat:", "This session is being continued")):
                    info["prompts"] = info.get("prompts", 0) + 1
    info["offset"] = offset


def main_warnings(state):
    m = state["main"]
    agents = state["agents"]
    a_weight = sum(i.get("weight", 0) for i in agents.values())
    a_opus = sum(i.get("weight_opus", 0) for i in agents.values())
    done = state.setdefault("warned", [])
    out = []

    n = m.get("prompts", 0)
    new = [lim for lim in PROMPTS if n >= lim and f"p{lim}" not in done]
    if new:
        done.extend(f"p{lim}" for lim in new)
        out.append(f"the user has sent {n} messages in this session; time to update the handoff file and move to a new session")

    ctx = m.get("context", 0)
    if ctx >= CONTEXT_START:
        level = CONTEXT_START + (ctx - CONTEXT_START) // CONTEXT_STEP * CONTEXT_STEP
        if f"c{level}" not in done:
            done.append(f"c{level}")
            out.append(f"every step of this conversation re-reads ~{ctx // 1000}k tokens; when the current part is done, "
                       "update the handoff file and open the successor session; heavy work goes to agents or scripts")

    if POINT:
        total = (m.get("weight", 0) + a_weight) / POINT
        new = [lim for lim in POINTS if total >= lim and f"t{lim}" not in done]
        if new:
            done.extend(f"t{lim}" for lim in new)
            out.append(f"this session (with its agents) has used ~{total:.0f}% of the weekly limit")

    min_weight = 2 * POINT if POINT else AGENTS_MIN_WEIGHTED
    if a_weight >= min_weight and a_opus / max(a_weight, 1) >= AGENTS_OPUS_SHARE and "opus" not in done:
        done.append("opus")
        out.append(f"{100 * a_opus / a_weight:.0f}% of this session's agent spending was on Opus; "
                   "use Sonnet for tests, simple reviews and summaries, and Haiku for logs")
    return out


def agent_warnings(data, transcript):
    agent = str(data.get("agent_id") or "")
    if not agent:
        return []
    path = os.path.join(transcript[:-6], "subagents", agent if agent.startswith("agent-") else f"agent-{agent}")
    path += "" if path.endswith(".jsonl") else ".jsonl"
    if not os.path.exists(path):
        return []
    os.makedirs(STATE, exist_ok=True)
    state_file = os.path.join(STATE, f"agent-{os.path.basename(path)[:-6]}.json")
    try:
        with open(state_file, encoding="utf-8") as fh:
            state = json.load(fh)
    except (OSError, ValueError):
        state = {}
    if "test" not in state:
        with open(path, "rb") as fh:
            state["test"] = TEST_MARK in fh.read(4000)
    limits = [3, 5] if state["test"] else AGENT_CALLS
    read_new(path, state, False)
    done = state.setdefault("warned", [])
    n = state.get("calls", 0)
    ctx = state.get("context", 0)
    out = []
    for lim in limits:
        if n >= lim and f"n{lim}" not in done:
            done.append(f"n{lim}")
            if lim == limits[0]:
                out.append(f"you have made {n} calls (your conversation is ~{ctx // 1000}k tokens and every step re-reads it). "
                           "Finish the item in progress, save the resume point where your brief says, and return the summary; "
                           "the coordinator opens another agent for the rest")
            else:
                out.append(f"{n} calls: stop now, save the resume point and return the summary with what is left")
    if ctx >= AGENT_CONTEXT and "ctx" not in done:
        done.append("ctx")
        out.append(f"your conversation is at ~{ctx // 1000}k tokens; wrap up soon with a resume point and a summary")
    save(state_file, state)
    return out


def save(path, state):
    tmp = f"{path}.{os.getpid()}.tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh)
    os.replace(tmp, path)


def main():
    try:
        data = json.loads(sys.stdin.buffer.read().decode("utf-8", errors="replace"))
        event = data.get("hook_event_name") or "UserPromptSubmit"
        transcript = data.get("transcript_path") or ""
        if not transcript or not os.path.exists(transcript):
            return
        if event == "PostToolUse" and data.get("agent_id"):
            said = agent_warnings(data, transcript)
            if said:
                print(json.dumps({"hookSpecificOutput": {"hookEventName": event,
                                                         "additionalContext": "SPEND WATCH: " + " | ".join(said)}}))
            return
        session = data.get("session_id") or os.path.basename(transcript)[:-6]
        os.makedirs(STATE, exist_ok=True)
        state_file = os.path.join(STATE, f"{session}.json")
        try:
            with open(state_file, encoding="utf-8") as fh:
                state = json.load(fh)
        except (OSError, ValueError):
            state = {}
        state.setdefault("main", {})
        state.setdefault("agents", {})
        read_new(transcript, state["main"], True)
        folder = transcript[:-6]
        for sub in glob.glob(os.path.join(folder, "**", "*.jsonl"), recursive=True):
            read_new(sub, state["agents"].setdefault(os.path.relpath(sub, folder), {}), False)
        said = main_warnings(state)
        save(state_file, state)
    except Exception:
        return
    if said:
        tail = (". Tell the user in one line, in their language, with the number, in your next message to them, and act "
                "(handoff file, successor session, cheaper agent)." if event == "PostToolUse" else
                ". Tell the user in one line, in their language, with the number, at the start of your reply, and propose what to do.")
        print(json.dumps({"hookSpecificOutput": {"hookEventName": event,
                                                 "additionalContext": "SPEND WATCH: " + " | ".join(said) + tail}}))


if __name__ == "__main__":
    main()
