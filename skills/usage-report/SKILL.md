---
name: usage-report
description: Explain where the person's Claude Code usage went, by session and by model, and what 1% of their plan is worth. Use when they ask "how much did I spend", "where did my quota go", "why did my limit run out", "which session used the most", "is Opus costing me", "how much is 1% worth", or in Portuguese "quanto gastei", "onde foi minha cota", "por que acabou meu limite", "qual sessão gastou mais", "quanto vale 1%".
---

# Usage report (JN's Quota Keeper)

Answer in the person's language, in plain words, in a few lines. Everything here reads local records only and makes no network calls. The records contain the person's conversations; the scripts read only token counts, model and time. Do not quote conversation content.

Scripts live in `<config folder>/tools/` (the config folder is `CLAUDE_CONFIG_DIR` if set, otherwise `~/.claude`). If they are missing, copy `usage_report.py` and `measure_point.py` from the Quota Keeper `scripts/` folder.

## Where did it go (by session and by model)
Run `python <config folder>/tools/usage_report.py --days 7 --top 10`. It prints total weighted tokens, the share per model family (Opus, Sonnet, Haiku) and the heaviest sessions. Explain: weighted tokens count each reply's input, cache and output with the weights the plan limit roughly follows; the numbers are estimates, not the official bill. Point out the biggest session and whether Opus has a large share of agent work that a cheaper model could do.

## What is 1% worth
Read the weekly usage % (the `get_usage` tool in the desktop app, found with ToolSearch; otherwise ask the person for the number from the usage screen or `/usage`). Run `python <config folder>/tools/measure_point.py <%>`. The first run only records a mark; from the second one, a day or two later and with at least 3 points of difference, it prints how many weighted tokens 1% is worth. Warn that a weekly reset between marks voids the pair and that use of the regular chat outside Claude Code is not in the records.

## Rules
- Never run anything that changes settings; this skill only reads and reports.
- If a script prints nothing useful (record format changed, no sessions in the period), say so instead of guessing.
