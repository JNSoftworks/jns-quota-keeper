"""Measure how many weighted tokens make up 1% of your plan's weekly limit.

Part of JN's Quota Keeper, token-saving tactics by Jaber Neto (JN Softworks).
Copyright (c) 2026 Jaber Neto (JN Softworks). SPDX-License-Identifier: MIT (full text in the guide's LICENSE.md).

Usage:
    python measure_point.py <weekly % used now>

The config folder (where the transcripts are in "projects") is CLAUDE_CONFIG_DIR if that
variable is set, otherwise ~/.claude.

Each run records a mark (time and %) in measure_marks.csv, next to this script. From the second
mark on, it adds up the weighted tokens of every Claude Code session between consecutive marks
(from the transcripts in ~/.claude/projects) and divides by the change in %.

Caveats: a weekly reset between two marks makes that pair useless (it is skipped when the %
goes down); chats outside Claude Code are not in the transcripts, so heavy use of them between
two marks makes the result too low; integer % values need a gap of a few points to be precise,
so marks closer than MIN_GAP points are summed with the next ones.
"""

import csv
import datetime as dt
import glob
import json
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
MARKS = os.path.join(HERE, "measure_marks.csv")
MIN_GAP = 3


def projects_dir():
    base = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")
    return os.path.join(base, "projects")


def cache_write(u):
    # The 5-minute cache writes at 1.25x; the 1-hour cache writes at 2x.
    d = u.get("cache_creation") or {}
    h1 = d.get("ephemeral_1h_input_tokens") or 0
    total = u.get("cache_creation_input_tokens") or 0
    return 2.0 * h1 + 1.25 * max(total - h1, 0)


def weight(u):
    return ((u.get("input_tokens") or 0) + cache_write(u)
            + 0.1 * (u.get("cache_read_input_tokens") or 0) + 5 * (u.get("output_tokens") or 0))


def weighted_between(start, end):
    seen = set()
    by_family = defaultdict(float)
    for path in glob.glob(os.path.join(projects_dir(), "**", "*.jsonl"), recursive=True):
        if os.path.getmtime(path) < start.timestamp():
            continue
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if '"type":"assistant"' not in line:
                    continue
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                m = e.get("message") or {}
                mid = m.get("id")
                if e.get("type") != "assistant" or not mid or mid in seen or m.get("model") == "<synthetic>":
                    continue
                try:
                    ts = dt.datetime.fromisoformat(e["timestamp"].replace("Z", "+00:00"))
                except (KeyError, ValueError, AttributeError):
                    continue
                if not (start < ts <= end):
                    continue
                seen.add(mid)
                model = m.get("model", "?")
                family = next((f for f in ("opus", "sonnet", "haiku") if f in model), "other")
                by_family[family] += weight(m.get("usage") or {})
    return by_family


def read_marks():
    if not os.path.exists(MARKS):
        return []
    with open(MARKS, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main():
    if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    percent = float(sys.argv[1].replace(",", ".").rstrip("%"))
    now = dt.datetime.now(dt.timezone.utc)
    marks = read_marks()

    row = {"time_utc": now.isoformat(timespec="seconds"), "percent": percent, "weighted": "", "opus": "", "sonnet": "", "haiku": "", "other": ""}
    if marks:
        prev = marks[-1]
        start = dt.datetime.fromisoformat(prev["time_utc"])
        gap = percent - float(prev["percent"])
        if gap < 0:
            print("The % went down since the last mark: the weekly limit was reset. This mark starts a new pair.")
        else:
            fam = weighted_between(start, now)
            row["weighted"] = round(sum(fam.values()))
            for k in ("opus", "sonnet", "haiku", "other"):
                row[k] = round(fam[k])
            print(f"Since the last mark ({prev['time_utc']}, {prev['percent']}%): {sum(fam.values()) / 1e6:.1f} M weighted, "
                  f"+{gap:g} points (opus {fam['opus'] / 1e6:.1f} M, sonnet {fam['sonnet'] / 1e6:.1f} M, haiku {fam['haiku'] / 1e6:.1f} M)")
            if gap < MIN_GAP:
                print(f"Under {MIN_GAP} points since the last mark: it is added to the next marks until the gap reaches {MIN_GAP}.")

    new_file = not os.path.exists(MARKS)
    with open(MARKS, "a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(row))
        if new_file:
            w.writeheader()
        w.writerow(row)

    marks = read_marks()
    # Small gaps between consecutive marks are summed until they reach MIN_GAP; a reset starts over.
    total_weight = total_gap = 0.0
    run_weight = run_gap = 0.0
    for a, b in zip(marks, marks[1:]):
        gap = float(b["percent"]) - float(a["percent"])
        if gap < 0 or not b["weighted"]:
            run_weight = run_gap = 0.0
            continue
        run_weight += float(b["weighted"])
        run_gap += gap
        if run_gap >= MIN_GAP:
            total_weight += run_weight
            total_gap += run_gap
            run_weight = run_gap = 0.0
    if total_gap:
        print(f"Estimate: 1% of the weekly limit = ~{total_weight / total_gap / 1e6:.1f} M weighted tokens "
              f"(from {total_gap:g} points). Put POINT = {round(total_weight / total_gap):_} in spend_watch.py once it is stable.")
    else:
        print(f"Mark saved ({percent:g}%). Run again in a day or two, with the new %, to get an estimate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
