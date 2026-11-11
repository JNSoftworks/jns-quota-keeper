"""Usage report: where did your Claude Code tokens go, by session and by model.

Part of JN's Quota Keeper, token-saving tactics by Jaber Felippe Neto (JN Softworks).
Copyright (c) 2026 Jaber Felippe Neto (JN Softworks). SPDX-License-Identifier: MIT (full text in the guide's LICENSE.md).

Usage:
    python usage_report.py [--days N] [--top N]

Reads the local session records (the .jsonl files in "projects" inside the config folder:
CLAUDE_CONFIG_DIR if that variable is set, otherwise ~/.claude). Those files contain your
conversations, but this script only reads the token counts, the model and the time of each
reply. It prints a summary and writes nothing. It makes no network calls.

Weighted tokens use the same weights as measure_point.py (input 1x, cache write 1.25x or 2x for
the 1-hour cache, cache read 0.1x, output 5x). Sub-agents count in their parent session.
The record format is internal to Claude Code and may change; unreadable lines are skipped.
"""

import argparse
import datetime as dt
import glob
import json
import os
from collections import defaultdict


def projects_dir():
    base = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")
    return os.path.join(base, "projects")


def weight(u):
    d = u.get("cache_creation") or {}
    h1 = d.get("ephemeral_1h_input_tokens") or 0
    total = u.get("cache_creation_input_tokens") or 0
    cw = 2.0 * h1 + 1.25 * max(total - h1, 0)
    return ((u.get("input_tokens") or 0) + cw + 0.1 * (u.get("cache_read_input_tokens") or 0)
            + 5 * (u.get("output_tokens") or 0))


def main():
    ap = argparse.ArgumentParser(description="Sum weighted tokens by session and by model from local Claude Code records.")
    ap.add_argument("--days", type=float, default=7, help="look back this many days (default 7)")
    ap.add_argument("--top", type=int, default=10, help="show this many sessions (default 10)")
    args = ap.parse_args()
    since = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=args.days)
    root = projects_dir()
    seen = set()
    by_session = defaultdict(float)
    by_family = defaultdict(float)
    last_seen = {}
    for path in glob.glob(os.path.join(root, "**", "*.jsonl"), recursive=True):
        if os.path.getmtime(path) < since.timestamp():
            continue
        rel = os.path.relpath(path, root).split(os.sep)
        session = rel[1][:-6] if len(rel) == 2 and rel[1].endswith(".jsonl") else (rel[1] if len(rel) > 1 else rel[0])
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if '"type":"assistant"' not in line:
                    continue
                try:
                    e = json.loads(line)
                    m = e.get("message") or {}
                    mid = m.get("id")
                    if not mid or mid in seen or m.get("model") == "<synthetic>":
                        continue
                    ts = dt.datetime.fromisoformat(e["timestamp"].replace("Z", "+00:00"))
                except (ValueError, KeyError, AttributeError):
                    continue
                if ts < since:
                    continue
                seen.add(mid)
                w = weight(m.get("usage") or {})
                model = m.get("model", "?")
                by_family[next((f for f in ("opus", "sonnet", "haiku") if f in model), "other")] += w
                by_session[session] += w
                if session not in last_seen or ts > last_seen[session]:
                    last_seen[session] = ts
    total = sum(by_session.values())
    print(f"Last {args.days:g} days: {total / 1e6:.1f} M weighted tokens in {len(by_session)} sessions")
    for fam in ("opus", "sonnet", "haiku", "other"):
        if by_family[fam]:
            print(f"  {fam}: {by_family[fam] / 1e6:.1f} M ({100 * by_family[fam] / total:.0f}%)")
    print(f"Top {args.top} sessions:")
    for s, w in sorted(by_session.items(), key=lambda x: -x[1])[:args.top]:
        print(f"  {s[:8]}  {w / 1e6:6.1f} M  last reply {last_seen[s].astimezone():%Y-%m-%d %H:%M}")


if __name__ == "__main__":
    main()
