# JN's Quota Keeper — token saving for Claude Code

> **Made by Jaber Felippe Neto (JN Softworks).** License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may copy, adapt and share it, as long as you keep the author's name and the license link. The scripts are under the MIT license, which also asks you to keep the credit. Version 1.0, November 2026.

This file is for Claude. If you are the person: you don't need to read it. Claude will show one question box per tactic and will change only what you accept.

## How to run the setup (Claude, read this before anything else)

1. **Nothing changes without a yes.** Show a tactic's box, wait for the answer, do only the steps for that answer, check them, and only then go to the next box.
2. **Show each box with AskUserQuestion**, one call per box, with the questions, headers and options exactly as written here (the tool adds "Other" by itself). Without it, ask the same questions in a short numbered list and wait.
3. **Summary first, details only on request.** Before each box, show in short, simple text what the tactic does ("What this does") and each question's summary: the `> **Summary** — ...` line right below the question. It is NOT an option of the box; it is text to show before it. Say the details are in `en/DETAILS.md` (the box's section, subtitle `Box N · Header`) and that the person can ask for "details" through "Other". Read and explain the details only when they ask, or for every question if in `Mode` they chose "Box by box, checking"; in the other modes don't read them on your own (it costs at every step), except where a box tells you to. The person may not be technical: no acronym or jargon without a plain explanation in the same sentence. Each option shows its consequence in one line; don't hide risk and don't exaggerate it.
4. **Follow the order of the boxes.** If one doesn't apply (for example, the person doesn't use agents), say so in one line and go to the next.
5. **Write the rules with the ready-made text** of each box ("Rule text"), without rewriting or decorating: every extra line in CLAUDE.md is paid for in every session. Of the parts between `< >`, fill in only the ones that belong to the setup:
   - a chosen number, like `<200>`: the number from the person's answer;
   - `<config folder>`: its full path (defined just below), with `/` slashes, e.g. `C:/Users/jane/.claude`;
   - `<path>`: only in the Box 7 tests, the full path of the test folder;
   - `<list>`: the tools chosen in Box 7;
   - `<reminder date>`: only in Box 10, today + 7 days, `YYYY-MM-DD`;
   - a choice `<a | b>`: keep only the option that matches the answer.

   These stay literal in the saved rule, for the session to fill in later: `<file>`, `<handoff>`, `<project>`, `<id>`, `<n>`, `<session title>`, `<date>`, `<session id>`.

   **Where the rule lines go:** in the `## Quota Keeper ...` section of the chosen CLAUDE.md, under `### Rules`, before `### Declined`. Box 1 creates the section and both subtitles (at the end of the file if the section doesn't exist). If the section exists without `### Rules`, create that subtitle before `### Declined`. Declines go under `### Declined`. Labels in square brackets (like "[Number]") only say which version to pick: they are not saved.
6. **Never ask for a token, password or key in the chat**, nor run a command that shows one on screen. Box 7 teaches the person to save the token by themselves.
7. **Talk little between steps.** The full summary comes in the final box.
8. **When in doubt, stop and ask.** If something here doesn't match the person's computer (a tool with another name, an option that doesn't exist, an error), say what you found and ask. Don't make things up.
9. **Tool and option names change.** The ones here are from November 2026. Look for them by name with ToolSearch; if you can't find one, say so and go on without that part.

**The three modes of the `Mode` question (Box 1, question 4).** They apply from Box 2 on:
- **Quick:** follow the "Recommended bundle (Quick mode)" section, in three groups. (1) Show, in a single message, the three tables, summarized in plain words. (2) One AskUserQuestion call with two questions: header `Bundle`, options `Install group 1` / `See box by box` / `Cancel` (each with its consequence in one line, as in that section), and Box 2's `Long waits` question, unchanged, which decides the 1-hour cache. (3) On "Install group 1": do the boxes' steps only for the Group 1 parts, without more questions. (4) One call with the Group 2 questions (pick several); install what is checked, what is unchecked goes to "Declined". (5) Say in one line that Group 3 exists and is turned on later, through Box 7, box by box; it is not installed, not asked and does not go to "Declined". (6) Run Box 10 as it is and finish with the final box. "See box by box" switches to the second mode; "Cancel" stops without changing anything else (the Box 1 backup already exists).
- **Box by box:** one question box per tactic, in order. Save what the person accepts without asking again.
- **Box by box, checking:** like the one above and, before each write (a line in `settings.json`, a hook, a script copy, a rule in CLAUDE.md), show the exact piece and ask, with options `Write` / `Don't write`. "Don't write" is a decline of that part (it goes to "Declined").

**What counts as "sensitive"** (in both box-by-box modes, always asked one by one, with the risk summary; in Quick mode, neither installed nor asked, because all of it is in Group 3): anything that changes permissions or the default permission mode; approves actions by itself (an approving hook, an allow rule); opens sessions by itself; turns on Remote Control; or saves a token. It is marked "(sensitive)" in the boxes.

**How the questions depend on each other.** Before each box (and in the Group 2 box, in Quick mode), skip the questions whose condition doesn't hold: the condition is written next to the header, as "(only if ...)", and the table below gathers the others. Say in one line what you skipped and why (for example: "I skipped the spares because you didn't choose the automatic successor"). A skipped question counts as the answer that installs nothing and does not go to "Declined": if the person changes their mind, they just ask for the box again.

| If... | Skip | What the person loses |
|---|---|---|
| There is no Python (Box 1, step 3) | `Brake`, `Copy lock`, `Reminder`, `Token`, `Spare hook`, `Spend watch`, `Measure plan`, `Usage skill`, `Daily report` | Scripts and hooks; only the text rules remain |
| `Where used` = "Terminal", or there is no `start_session` | In Box 7, everything except `Token` and `Permissions` | A successor visible in the app; Path B or the "[I open it]" rule remains |
| `Where used` = "Desktop app" or "Both" | `Token`, `Permissions` | Nothing: in the app, the token isn't needed |
| `Plan` = "API key" | `Before/after`, `Measure plan`, `Token` | Counting in % of the quota (that plan doesn't have it) |
| 200k window (or unknown) | `Compaction`; `Switching` uses ~100k | Nothing: lowering compaction only helps in the 1-million window |
| The person doesn't use agents | `Long waits` and Box 5 | Nothing now; if they start using agents, they can ask |
| `Handoff` = "No" | `Switching`, `Reminder` and all of Box 7 | Without a handoff, switching and the automatic successor lose their point |
| `Successor` isn't "Claude, on its own" | `Close old`, `Scheduled`, `Refused`, `Spares`, `Remote`, `Auto default`, `Spare hook` | The chain doesn't go on by itself; the switch depends on you |
| `Refused` isn't "Spare session" | `Spares`, `Spare hook` | Without you at the screen, the switch waits for your message or uses the fallback |
| `Scheduled` = "Don't allow" | `Auto default` | The scheduled-task fallback |
| `Token` isn't "Yes, guide me" | `Permissions` | The screenless rounds |
| Quick mode | All of Box 7 (Group 3) | Nothing now: it is turned on later |

Combinations that only half work (if the person picks one, say in one line what they lose):
- Session switching without `Spend watch`: it depends on Claude noticing the conversation size; in the author's use, 14 of 36 switches went past the mark before the watch.
- `Long waits` "Yes" without agents that wait more than 5 minutes: writing costs 2 times and nothing is gained.
- "Experimental: Opus coordinates" without `Brake`: only the text rule keeps Sonnet from opening agents.
- `Close old` "No": the previous session may reread its conversation at every turn of the new one, spending quota, until it is archived.
- Spares without `Spare hook`: in auto mode, the switch through a spare may be blocked and fall back to "Notify and carry on".
- `Scheduled` allowed with `Auto default` "Don't change": the task's successor stops at the first command, waiting for approval.
- "Notify and carry on" with `Remote` "Don't use": the warning only shows on the computer.
- `Copy lock` "No" with "Claude, on its own": when switching with an agent running, the successor checks the handoff instead of the lock guaranteeing it.
- `Measure plan` "No": the spend watch warns only in tokens, not in % of the quota.
- `Token` "Yes, guide me" (or screenless rounds) without `Daily report`: nobody checks daily whether the account rose from another source or whether there is a hidden session. Recommend `Daily report` (Box 8, Group 2); it only needs Python, but without `Measure plan` it gives no verdict on the account.

**What is never skimped on** (always applies): a backup before changing settings, confirmation before anything irreversible, building and testing what changed, and reading the exact piece of code that is about to be edited.

**Files in this package** (paths start from the folder where `START_HERE.md` is):
- `en/GUIDE.md` (this one), `en/DETAILS.md` (details of each question, read only when the person asks), `en/HANDOFF_TEMPLATE.md` and `en/SUMMARIES_TEMPLATE.md` (templates for the handoff and summaries files)
- `scripts/`: `spend_watch.py` (spend watch), `agent_limit.py` (agent brake), `session_relay.py` (screenless rounds), `measure_point.py` (measure how much 1% of the plan is worth), `check_settings.py` (check `settings.json`), `spare_allow.py` (approves only the actions on spares), `copy_lock.py` (copy lock: keeps agents of two sessions off the same working copy), `handoff_reminder.py` (session-start reminder to read the handoff), `usage_report.py` (report of where the tokens went; only reads and prints), `daily_report.py` (daily report of yesterday and a once-a-day reminder; only reads the local records and writes its own markers)
- `skills/usage-report/SKILL.md` (skill that runs the usage report) and `LICENSE.md`

**Config folder:** the folder named by the environment variable `CLAUDE_CONFIG_DIR`, if set (check: PowerShell `$env:CLAUDE_CONFIG_DIR`; Mac and Linux `echo $CLAUDE_CONFIG_DIR`); otherwise the `.claude` folder inside the user's home folder (Windows: `C:\Users\<name>\.claude`; Mac: `/Users/<name>/.claude`; Linux: `/home/<name>/.claude`). "Config folder" and `<config folder>` always mean this folder. In hook commands and in rules, use the full path with `/` slashes, on Windows too. Before copying the first file into `hooks`, `tools` or `templates` inside it, create the subfolder if it doesn't exist. `check_settings.py` and `measure_point.py` already read `CLAUDE_CONFIG_DIR` by themselves.

**Context window** (how many tokens fit in a conversation: 200k or 1 million): in the app, the context indicator next to the message box; in the terminal, the `/context` command (shows something like "x / 200k" or "x / 1M"). If you can't see it, assume 200k: it is the safe default, since limits made for 200k also work in the 1-million window, and the reverse is not true. If the person says it is 1 million, redo only the answers that depend on it (Boxes 2, 6 and 8).

**How to edit `settings.json` without breaking it:** read the whole file, add without deleting what is already there (inside `"env"` and `"hooks"`, which may already have items), and at the end check that it is still valid:

```text
python <package folder>/scripts/check_settings.py
```

The script accepts a file with a BOM, warns if a key appears twice (two `"hooks"` or two `"env"`, for example) and prints `ok` when everything is fine. On Mac and Linux, replace `python` with `python3` here and in the hook commands.

## Why it works

Explain this to the person in up to 3 sentences before Box 1.

At every step (each time Claude uses a tool and reads the result), it rereads the whole conversation. Almost all of the cost comes from this rereading, not from writing or thinking. What saves tokens is: a short conversation, fewer steps in the main conversation, and heavy work outside it (in an agent, with its own conversation, or in a script, which costs no tokens).

The author's numbers (September to November 2026, measured in the session records on the author's machine; your results may differ):
- Rereading the conversation was 73% of the cost; storing the conversation to reread it later (the cache) was 19%; writing and thinking, 8%.
- With the handoff and session-switch rules (Box 6), the main conversation fell from ~12.7 to ~3.2 points of the quota per day of use (75% less; a before-and-after comparison, not a controlled test).
- Agents that went past 100 calls were 74% of the agents' cost (Box 5).
- Agents waiting for a build or a test, with the default 5-minute cache, rewrote the whole conversation when they came back: ~26% of all the cost in 8 days, until the 1-hour cache was turned on (Box 2).

The yardstick used to compare (it is not an official price):

```text
weight = input × 1 + cache write × 1.25 (5-minute cache) or × 2 (1-hour cache) + cache read × 0.1 + output × 5
```

How much 1% of the quota is worth depends on the plan. On the author's plan, 1% of the week was ~8.5 million weight (measured on the author's machine; may differ). Don't use this number for another plan: Box 8 measures the person's own.

## Words to explain to the person

Use these short explanations when a word comes up. Don't read the whole list to them.

- **Token:** a piece of text, roughly one word; the unit Claude reads, writes and is billed in.
- **Conversation (or context):** everything said and read in the session. Claude rereads it at every step.
- **Agent:** a helper Claude opens for one task, with its own conversation that starts empty; it returns only a summary.
- **Haiku, Sonnet, Opus:** the three Claude models: the cheapest and fastest, the middle one, and the strongest and most expensive.
- **CLAUDE.md:** a file of rules that Claude reads at the start of every session.
- **Hook:** a small script that Claude Code runs by itself at a fixed moment (every message, before opening an agent).
- **Cache:** the conversation stored so it can be reread more cheaply. It lasts 5 minutes by default; after that, storing it again costs again.
- **`/clear` and `/compact`:** `/clear` erases the conversation; `/compact` replaces it with a summary. Only the person can type them.

---

## General risks and undoing everything

Tell the person this, briefly, before Box 1. Each question carries a summary of its risks; this is what holds for the whole bundle.

- **What the bundle changes:** CLAUDE.md (a "Quota Keeper" section), `settings.json` (variables in `"env"`, hooks and, only in Box 7, permissions) and scripts, templates and one skill copied into the config folder. Nothing else, and only what the person accepts.
- **Network:** no script in the bundle makes a network call. `copy_lock.py` only runs `ps` (Mac and Linux) and itself. `session_relay.py` runs the `claude` command (which, like all Claude use, sends the conversation to Anthropic) and, on Windows, `taskkill` only on the process it opened itself. `daily_report.py` only reads the local records and writes its own markers in `quota_keeper/`.
- **Permissions:** a hook runs with the user's permissions, like any program of theirs. Nothing here bypasses Claude Code's approvals, except what each box marked "(sensitive)" says in plain words.
- **If Python is missing or a hook errors:** Claude Code shows the error and goes on. A hook blocks an action only when it exits with code 2 (at session start, not even that: it only shows the error) or when it answers "deny" on purpose, with a message, as this bundle's brake and lock do. An error with any other code doesn't block. Python missing = the script-based parts don't work, nothing else breaks. (Check the hooks documentation in case the person's version changed this.)
- **Can it cost more?** Some tactics can cost MORE in some uses: the 1-hour cache (writing costs 2 times), new sessions (they reread everything they load at the start) and spares (reserve sessions: one short turn when created, then archived). Each box says when.
- **Undo everything:** (1) put the Box 1 backups (`settings.json.before-quota-keeper-<date>` and `CLAUDE.md.before-quota-keeper-<date>`) back over the current files, or (2) delete the "Quota Keeper" section from CLAUDE.md, remove from `settings.json` the `"env"`, `"hooks"` and `"permissions"` lines the bundle added, and delete what was copied into the config folder (scripts in `hooks` and `tools`, templates in `templates`, the `skills/usage-report` folder and, if they exist, `quota_keeper/`, `spares.txt` and `relay_token.txt`). Applies from the next session.

---

## Recommended bundle (Quick mode)

What Quick mode shows before installing, in three groups. Paths are in the config folder; "rule" is a line in CLAUDE.md. Everything applies from the next session. Each part's steps are those of its box, with the "(Recommended)" answer unless said otherwise here. Each row names the box and the question's header; the details, if the person asks, are in `en/DETAILS.md` (for example, "Box 2 · Agents").

**Group 1 — Adopt (installed with one OK).** Only rules, two file templates and `"env"` settings. Nothing approves, blocks or changes permissions.

| Part (box) | What it installs | Risk | How to undo |
|---|---|---|---|
| Lean CLAUDE.md and short memory (3: `CLAUDE.md`, `Memory`) | Rules; Claude proposes cuts and moves only with a yes | A moved detail may be missed (a pointer stays) | Delete the lines; put the text back |
| Short chat, long text in a file (3: `Chat style`, `Long text`) | Rules | You see less detail along the way | Delete the lines |
| Reading habits (4: all four) | Rules | May miss what was outside the piece read | Delete the lines |
| Agents on Sonnet (2: `Agents`) | `CLAUDE_CODE_SUBAGENT_MODEL` | Sonnet errs more than Opus on hard tasks; Claude asks for Opus | Delete the line in `"env"` |
| Right model per task, short and batched agents (5: `Short agent`, `Models` "By role", `Batching`) | Rules | More agents per task; Haiku errs more on what looked simple | Delete the lines |
| High effort (2: `Effort`) | Rule | Nothing relevant | Delete the line |
| 1-hour cache (2: `Long waits`), only if agents wait more than 5 minutes | `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` | Writing costs 2 times; without long waits, it costs more | Delete the line in `"env"` |
| Handoff and summaries, session switch, one task per session (6: `Handoff`, `Switching`, `One task`) | Rules and the two templates in `templates/`; switch at ~250k (~100k with the 200k window) | New files in projects, without asking; a stale handoff sends the new session to the wrong spot | Delete the lines and templates; files already created stay |
| Usage before and after a big task (8: `Before/after`), not with "API key" | Rule | Nothing relevant | Delete the line |
| Checking for less and end of turn (9: "Cheap proof", "Tests in parts", "Don't pay twice" and the three in `Turn end`) | Rules | A purely visual defect may slip by; the final message is a bit longer | Delete the lines |

Left out of Quick mode, without going to "Declined", because they need the person's choice: "Two reviews, sensitive only" (Box 9) and "Experimental: Opus coordinates" (Box 5). They can ask for them later.

Options of the `Bundle` question:
- **Install group 1** — I install Group 1 now, without more questions; then I show Group 2 in a single box.
- **See box by box** — Nothing is installed now; I switch to one question box per tactic, with the risks of each.
- **Cancel** — I stop here; only the Box 1 backup was made.

**Group 2 — Try and watch (the person checks them in a single box).** Scripts that run by themselves (hooks) or change the conversation. None approves an action; the brake and the lock can only deny. Worth watching the first few days. Each has a test in its box (only with a yes).

| Part (box) | What it installs | Risk | How to undo |
|---|---|---|---|
| Spend watch (8: `Spend watch`, author's limits) | `hooks/spend_watch.py` under `"UserPromptSubmit"` and `"PostToolUse"`, and a rule | Reads the local records (counts only); one warning line when a limit is crossed | Remove both entries; delete script and rule |
| Agent brake (5: `Brake`) | `hooks/agent_limit.py` under `"PreToolUse"` | May deny an agent you wanted (the message says why) | Remove the entry; delete the script |
| Copy lock (5: `Copy lock`) | `hooks/copy_lock.py` under `"PreToolUse"` and `"SubagentStop"` | A stuck lock keeps another session from writing in that folder for up to 2 hours | Remove the entries; delete the script; `copy_lock.py release <folder>` frees it now |
| Handoff reminder (6: `Reminder`) | `hooks/handoff_reminder.py` under `"SessionStart"` | One more line at session start in folders with a handoff | Remove the entry; delete the script |
| Compact at 50% (2: `Compaction`), only with the 1-million window | `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | The automatic summary loses detail | Delete the line in `"env"` |
| Usage report (8: `Usage skill`) | `skills/usage-report/`, `tools/usage_report.py` and `tools/measure_point.py` | Reads the local records (counts only); nothing leaves the computer | Delete the skill folder and both scripts |
| Measure the plan (8: `Measure plan`), only with a weekly % limit | `tools/measure_point.py`, a rule and the first mark | It is an estimate; needs the % on two different days | Delete the line, the script and `tools/measure_marks.csv` |
| Daily report (8: `Daily report`), only if the person wants it | `tools/daily_report.py` and `tools/usage_report.py`; a hook under `"SessionStart"` (matcher `startup`) that, once a day, only reminds Claude to ask "Want yesterday's report?" (See it now / Not today) | Reads only the local records; a hint, not proof (it cannot see another computer, claude.ai or a phone); one more line in the first session of the day | Remove the entry; delete both scripts and the `quota_keeper/` folder |

How to ask (one call, `multiSelect: true` on both questions, each option with the table's risk in one line; `Daily report` only if Python exists):
- **Which of these hooks should we try?** — header `Hooks` — options `Spend watch` / `Agent brake` / `Copy lock` / `Handoff reminder`.
- **And these?** — header `Others` — options `Compact at 50%` (drop it with the 200k window) / `Usage report` / `Measure the plan` (drop it with "API key") / `Daily report` (four options is the box's maximum). If only one option is left, ask it without `multiSelect`, with `Yes` / `No`.
- Without Python, drop every option except `Compact at 50%` (the `Hooks` question is not asked) and say so in one line.
- Before the box, show each option's summary (You gain / You risk / If you skip it / Undo), taken from the table (item 3 of "How to run the setup" applies).

**Group 3 — Advanced, not at the start (Quick mode neither installs nor asks).** All of it is Box 7. Say it exists and is turned on later, box by box (just ask "run Box 7 of the Quota Keeper guide"), ideally after a week or two with the rest. Whoever turns on the token or the screenless rounds should also turn on the `Daily report` (Group 2): it shows, once a day, hidden sessions and an account rising without explanation. Details of each part: `en/DETAILS.md`, Box 7.

| Part (Box 7) | What it would install | Why it waits | How to undo, if turned on |
|---|---|---|---|
| Automatic succession with archiving of the previous session (`Successor`, `Close old`, `Refused`, `Spares`) | Rules that open the new session and spares by themselves and archive the previous one | Opens and archives sessions without you looking; can cost more. Only pays off once the handoff already works | Delete the lines; unarchive from the list |
| Long-lived token in a file (`Token`, `Permissions`) | `relay_token.txt` | A key to the account, valid for a year, in a file: whoever gets it spends your quota. Only useful if you use only the terminal | Delete the file; revoke as Box 7 says |
| Screenless rounds (Path B) | `tools/session_relay.py` and a rule | Hidden work, no approval: a mistake can edit files without you seeing | Delete the script and the rule |
| Automatic Remote Control (`Remote`) | Rule that turns Remote Control on in successors | Whoever gets into your claude.ai account or picks up your unlocked phone can send orders to the computer | Delete the line; turn it off in each session and in the app |
| Automatic approval: spare hook, allow rules, auto mode as default (`Spare hook`, `Scheduled`, `Auto default`) | `hooks/spare_allow.py`; lines in `"permissions"` | Actions go through without you seeing, in all sessions and projects; auto mode's filter can be wrong | Remove the lines; delete the script |

---

## Box 1 — Before you start

**What this does:** decide where the rules go, how the person uses Claude Code and how the setup goes on. Nothing changes yet: the change comes in the steps (backup and the CLAUDE.md section).

Questions:

1. **Where should the rules you accept be saved?** — header `Save rules`
   > **Summary** — **You gain:** rules in every project (or only this one). **You risk:** almost nothing; "all projects" makes every line be read in every session; "only this project" in a shared file shows the lines to others. **If you skip it:** there is no "no": without this answer the rules have nowhere to go. **Undo:** delete the "Quota Keeper" section or restore the backup.
   - **In all projects (Recommended)** — They go to the `CLAUDE.md` of Claude Code's config folder (usually `~/.claude/CLAUDE.md`) and apply in any folder.
   - **Only in this project** — They go to the `CLAUDE.md` of the folder open now; if the file is shared, others will see them.

2. **Where do you use Claude Code?** — header `Where used`
   > **Summary** — **You gain:** the guide only offers what works the way you use Claude Code. **You risk:** nothing, it only keeps the answer. **If you skip it:** with "Terminal", the parts that depend on the app (visible successor, Remote Control) are skipped; the rest works the same. **Undo:** nothing; ask the question again.
   - **Desktop app** — The Claude app on the computer, in the Code tab. Unlocks the parts that use the app's tools.
   - **Terminal** — The `claude` command in a terminal window or in the code editor. The app-only parts are skipped.
   - **Both** — Offers the parts of both; nothing is installed unless you accept.

3. **How do you pay for Claude?** — header `Plan`
   > **Summary** — **You gain:** the parts that measure the quota in % only appear if your plan has that limit. **You risk:** nothing; "I don't know" is safe. **If you skip it:** with "API key", `Before/after`, `Measure plan` and `Token` are left out; the rest works. **Undo:** nothing.
   - **Pro, Max or Ultra** — Personal subscription, with a weekly limit; the parts that measure the quota in % are available.
   - **Team or Enterprise** — Company plan; the company may set the limits, so the quota-measuring parts are only suggestions.
   - **API key** — Pay per token, no weekly limit in %; the parts that measure the quota in % are skipped.
   - **I don't know** — That's fine: the guide stays general and says, in each box, what depends on the plan.

4. **How should I install what you accept?** — header `Mode`
   > **Summary** — **You gain:** Quick = few clicks; "checking" = you see the exact lines before each write. **You risk:** in Quick, one ok installs Group 1 (rules and settings without permissions). **If you skip it:** there is no "no": it only changes how I ask. **Undo:** as in "General risks and undoing everything".
   - **Quick (Recommended)** — One screen with the recommended bundle, the risk of each part and how to undo it. One ok installs the basics (rules and settings without permissions); you check the hooks in a single box; the advanced part (sessions opened by themselves, automatic approval, token) is not installed now.
   - **Box by box** — One question box per tactic, with the risks of each. I save what you accept without asking again.
   - **Box by box, checking** — Like the previous one and, before each write (settings.json, hook, rule), I show the exact lines and wait for your ok. Maximum control, more clicks.

Don't put "(Recommended)" on any option in question 3: it is a fact about the person. Question 4 runs the setup: see "The three modes of the `Mode` question" at the start of the guide.

Steps:
1. Make a backup of each file that exists, next to the original, with today's date (computer's clock) in the name: `<config folder>/settings.json` → `settings.json.before-quota-keeper-<YYYY-MM-DD>`, and the chosen CLAUDE.md → `CLAUDE.md.before-quota-keeper-<YYYY-MM-DD>`. Tell the person where they are.
2. At the end of the chosen CLAUDE.md (create it if it doesn't exist), add the section below. The next boxes put rules under "Rules" and declines under "Declined".

   ```markdown
   ## Quota Keeper (tactics by Jaber Felippe Neto, JN Softworks)

   ### Rules

   ### Declined (don't offer again)
   ```

   If the answer was "Only in this project" and that CLAUDE.md is shared (in a repository, for example), warn the person before saving. Settings, hooks and scripts always belong to the whole user (`<config folder>/settings.json`), even with "Only in this project": that answer applies only to the rule lines. Tell the person this.

   If the "Quota Keeper" section (or "Token saving", its old name) already exists, update the existing one, never create another. The same goes for the settings and hooks in the next boxes: if they are already in `settings.json`, update them, never duplicate.
3. Check that Python 3 is installed (`python --version` or `python3 --version`). The scripts in Boxes 5, 6, 7 and 8 need it. If it isn't, warn that those parts need Python (https://www.python.org/downloads/) and go on with the rest.
4. Keep the answer to "Where used": Box 7 depends on it.
5. Keep the answer to "Mode": it decides how Boxes 2 onward go (the three modes, at the start of the guide). With "Quick", after the steps of this box follow the Quick script (the "Recommended bundle (Quick mode)" tables, the `Bundle` question, the Group 2 box) instead of opening Box 2. With the other two, go box by box.
6. Keep the answer to "Plan": Boxes 7 and 8 depend on it. Never assume the plan, not even from what a tool shows. With "I don't know", speak in general terms ("if your plan has a weekly limit in %...") and let the person decide. If they want to find out, show what the usage screen says (in the app, the `get_usage` tool; in the terminal, `/usage`) and ask them to confirm; without confirmation, it stays "I don't know".

**Declines, in all boxes:** every tactic answered "No" (or unchecked) becomes a line under "Declined", with its name, so that no session asks again.

---

## Box 2 — Settings

**What this does:** three adjustments in `<config folder>/settings.json` and one effort rule. Nothing approves an action, changes a permission or sends data; everything applies from the next session.
**Note:** compacting at 50% assumes the 1-million window (rule "Context window", at the start of the guide). With the 200k window, skip question 3 and leave the default.

Questions:

1. **Should agents start on Sonnet?** — header `Agents`
   > **Summary** — **You gain:** agents cheaper than Opus. **You risk:** Sonnet errs more on hard tasks; Claude asks for Opus there. **If you skip it:** agents use the conversation's model; may cost more. **Undo:** delete `CLAUDE_CODE_SUBAGENT_MODEL` in `"env"`.
   - **Yes (Recommended)** — Every agent starts on Sonnet. When needed, Claude asks for Opus or Haiku for a specific agent.
   - **No** — Agents use the conversation's model; they may cost more if it is on Opus.

2. **Do your agents often wait more than 5 minutes for something (builds, tests, downloads, renders)?** — header `Long waits` (only if the person uses agents)
   > **Summary** — **You gain:** an agent that waits more than 5 minutes doesn't pay for the whole conversation again (on the author's machine, ~26% of the cost; Sep-Nov 2026). **You risk:** writing costs 2 times (not 1.25): without long waits, it costs more. **If you skip it:** the 5-minute cache stays. **Undo:** delete `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` in `"env"`.
   - **Yes, 1-hour cache** — An agent that waits doesn't pay for the whole conversation again when it comes back. Only pays off with waits over 5 minutes; without them, it costs more.
   - **No, leave as is** — Nothing changes: the 5-minute cache is enough for quick tasks.

3. **When should the conversation be summarized automatically?** — header `Compaction` (only with the 1-million window)
   > **Summary** — **You gain:** the conversation is summarized before every step gets expensive. **You risk:** the automatic summary loses detail; at 25%, more. **If you skip it:** the default stays, near the end of the space; steps cost more, nothing breaks. **Undo:** delete `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` in `"env"`.
   - **At 50% (Recommended)** — Summarizes when the conversation reaches half of the space; loses some detail.
   - **At 25%** — For long production in a single session. Summarizes more often and loses more detail.
   - **Leave it** — Nothing changes: stays at the default, near the end of the space.

4. **Make a rule: High effort, no agent-fleet mode?** — header `Effort`
   > **Summary** — **You gain:** Claude recommends High effort and avoids modes that open many agents at once. **You risk:** almost nothing: it is just one line of text; the effort selector stays with you. **If you skip it:** Claude may suggest more expensive effort or modes. **Undo:** delete the rule's line in `CLAUDE.md`.
   - **Yes (Recommended)** — Claude recommends High effort; Max only for a very hard problem; no mode that opens many agents unless you ask. You change the effort itself in the selector.
   - **No** — Nothing changes; Claude may suggest more expensive effort or modes.

Steps (each one only if the answer asked for it):
1. In `settings.json`, inside `"env"` (create it if it doesn't exist), add without deleting what is already there:
   - question 1 "Yes": `"CLAUDE_CODE_SUBAGENT_MODEL": "sonnet"`. Tell the person: in old versions of Claude Code, this setting overrode the model requested for a specific agent; if an agent requested on Opus or Haiku doesn't change model, update (`claude update`).
   - question 2 "Yes": `"CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL": "1h"`
   - question 3: `"CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"` (or `"25"`)

   Example with all three:

   ```json
   {
     "env": {
       "CLAUDE_CODE_SUBAGENT_MODEL": "sonnet",
       "CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL": "1h",
       "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"
     }
   }
   ```
2. Question 4 "Yes": save the rule.
3. Tell the person: the settings apply from the next session; to undo, delete the line (or restore the Box 1 backup). Only they can change the conversation's effort, in the selector of the app or the terminal.

Rule text:
> - Effort: recommend High; Max only for a very hard problem (preferably in an agent with max effort, not in the whole conversation). Never open an agent-fleet mode unless the person asks.

Check: `settings.json` is still valid (command at the start of the guide). Show the person only the new lines.

---

## Box 3 — What Claude reads every time

**What this does:** CLAUDE.md and the memory index come into every session and are reread at every step; writing costs 5 times more than reading, and what is written stays in the conversation. Only rules (text) are saved here; no script and no permission. Applies from the next session.

Questions:

1. **Keep CLAUDE.md short (rules and pointers; details go to other files)?** — header `CLAUDE.md`
   > **Summary** — **You gain:** less text paid for in every session. **You risk:** a moved detail may be missed (a pointer stays in place); nothing moves without your yes, and the Box 1 backup keeps the file. **If you skip it:** CLAUDE.md keeps growing and costing more. **Undo:** delete the rule's line; put the moved piece back.
   - **Yes, and suggest cuts (Recommended)** — It becomes a rule, and Claude proposes now what to move to another file. Nothing leaves without your yes.
   - **Rule only** — Applies from now on; the current file stays as it is.
   - **No** — Nothing changes; CLAUDE.md may keep growing and costing more.

2. **Memory with a short index (one line per note; a big project gets a summary note)?** — header `Memory`
   > **Summary** — **You gain:** only the first 200 index lines enter; a short line fits more. **You risk:** shortening may erase a useful detail (only with your yes); the Box 1 backup does NOT cover memory, ask for a copy. **If you skip it:** a long index is cut at line 200. **Undo:** delete the rule; put back the text from the copy.
   - **Yes (Recommended)** — A short line fits more and costs less; shortening existing lines only with your yes.
   - **I don't use memory** — Nothing to do; this part is skipped.
   - **No** — Nothing changes; a long index is cut after line 200.

3. **Short messages in the middle of the work, everything together at the end?** — header `Chat style`
   > **Summary** — **You gain:** the conversation grows more slowly. **You risk:** you follow less of what Claude does in the middle of the work; warnings and results only come together at the end. **If you skip it:** you see more detail along the way and the conversation costs more. **Undo:** delete the rule's line.
   - **Yes (Recommended)** — Between steps, just one line about what it is doing. Answers, results and warnings come together in the final message.
   - **No** — Nothing changes; you see more detail, and the conversation grows faster.

4. **Long things go to a file, not to the chat?** — header `Long text`
   > **Summary** — **You gain:** a big text or log doesn't stay in the conversation being reread at every step. **You risk:** almost nothing: one extra step for you (save it in a file in the folder and give the name). **If you skip it:** pasting in the chat stays handy, and costs at every following step. **Undo:** delete the rule's line.
   - **Yes (Recommended)** — To show a big text or log, you save it in a file in the folder and give the name; Claude reads only the part it needs.
   - **No** — Nothing changes; pasting in the chat is handier, but costs at every following step.

Steps:
1. Question 1 "Yes, and suggest cuts": measure CLAUDE.md (lines and size). If it is over ~200 lines or ~10 KB, propose a list of blocks to move to a reference file (for example, in `docs/`), each with the pointer line that stays in its place. Show the list and move only with a yes.
2. Question 2 "Yes": if the person uses automatic memory (a `memory` folder with a `MEMORY.md`), show how many lines and KB the index has. Only the first 200 lines enter the session. Propose shortening the long lines (over ~150 characters), only with a yes.
3. Save the accepted rules.

Rule text:
> - Short CLAUDE.md: only rules and pointers; explanation and detail go to another file, cited in one line.
> - Memory: index with one short line per note (under 200 lines); a project with many notes gets a summary note, and its new notes go there, not in the index.
> - Between tools, only short text about what is being done; answers, results and warnings go together in the final message.
> - Long text or log: ask the person to save it in a file in the folder instead of pasting it in the chat; read only the part needed.

---

## Box 4 — Reading

**What this does:** everything Claude reads stays in the conversation and is reread at every following step. Only rules (text) about how to read are saved here; no script and no permission. Applies from the next session.

Question (just one, with several answers: `multiSelect: true`):

1. **Which of these reading habits become rules?** — header `Reading`
   > **Summary** — **You gain:** a 50k-token file read at the start weighs ~560k over 100 steps (guide's yardstick, not an official price). **You risk:** missing what was outside the part read; an agent's summary omitting something; a stale note; an unmarked log error not showing up. **If you skip it:** everything read in full, costlier. **Undo:** delete the habit's line.
   - **Search instead of reading** — Look for the name or title and read only about 50 lines around it. Never read a big document, log or generated file in full.
   - **Big reads go to agents** — An agent reads and returns only the summary; the volume doesn't enter the conversation. Haiku to find and filter; Sonnet to understand.
   - **Extract once** — When several tasks use the same big source, an agent writes a short note and the next ones read the note.
   - **Filter logs at source** — Mark the log's own lines and search only for the mark; never load a whole build or test log.

If the person checks none: nothing changes.

Steps: save one line per checked item; the unchecked ones go to "Declined".

Rule text:
> - Search before reading: look for the name and read only the part around it; big documents, logs and generated files are never read in full.
> - Big reads (logs, several files, long documents) go to an agent that returns only the summary (Haiku to find, filter and count; Sonnet to understand). Read in full only what I am going to edit.
> - Big source used by several tasks: extract once into a short note in the project and reuse the note.
> - Logs: mark my own lines and search for the mark; never load a whole build or test log.

---

## Box 5 — Agents

**What this does:** limits how long each agent works, picks the model for each kind of work and, with two optional scripts, brakes chains of agents and protects a folder from two sessions at once. In the author's use, agents with 100 or more calls were 74% of the agents' cost (measured on the author's machine, Sep-Nov 2026; your results may differ).

Questions (there are 5; the question box takes 4 per call: ask in 2 calls, 1 to 3 and then 4 and 5):

1. **Short agents: stop at ~100 calls and hand over?** — header `Short agent`
   > **Summary** — **You gain:** agents don't get expensive from rereading their own conversation. **You risk:** a task split across more agents. **If you skip it:** agents have no size limit; the ~50-minute wait rule and "Opus coordinates" lose their basis. **Undo:** delete the line from CLAUDE.md.
   - **Yes, at ~100 (Recommended)** — The agent finishes the item, writes where it stopped in a file and returns the summary; if work is left, the main conversation opens another from that file.
   - **No** — Nothing changes; agents have no size limit.
2. **Which model for each kind of work?** — header `Models`
   > **Summary** — **You gain:** mechanical work runs on a cheaper model. **You risk:** the cheap model errs more; "Opus coordinates" is a test, not a proven saving. **If you skip it:** you pick each agent's model by hand. **Undo:** delete the line from CLAUDE.md.
   - **By role (Recommended)** — Sonnet by default; Haiku for the mechanical; Opus only for delicate code (security, accounts, money, cryptography).
   - **Experimental: Opus coordinates** — An Opus agent splits the work and reviews it; Sonnet agents, one at a time, do it. Being tested, no proven saving.
   - **Don't change** — Nothing changes; you pick each agent's model by hand.
3. **Agents in batches and with short answers?** — header `Batching`
   > **Summary** — **You gain:** fewer agents and short answers the main conversation rereads less. **You risk:** the detail sits in a file, not in the answer. **If you skip it:** agents return long answers. **Undo:** delete the line from CLAUDE.md.
   - **Yes (Recommended)** — One agent per task; several in the same message; each one writes the detail in a file and returns 5 to 10 lines.
   - **No** — Nothing changes; long answers, reread at every step.
4. **Install the agent brake?** — header `Brake` (only with Python)
   > **Summary** — **You gain:** stops endless chains of agents opening agents. **You risk:** it may deny an agent you wanted (the message says why); it only DENIES, never approves. **If you skip it:** endless chains stay possible; "Opus coordinates" has only the text rule. **Undo:** delete the `agent_limit.py` entry under `"PreToolUse"` in `settings.json`.
   - **Yes (Recommended)** — An agent opened by another agent opens no more agents, and each agent has at most 6 children.
   - **No** — Nothing changes; endless chains stay possible.
5. **Install the copy lock?** — header `Copy lock` (only with Python)
   > **Summary** — **You gain:** two sessions don't write in the same folder at once. **You risk:** a stuck lock blocks the other session (goes away in 2 h, or with `release`); it only DENIES, never approves. **If you skip it:** two sessions can get in each other's way; the switch with an agent still running (Box 7) relies on a manual check. **Undo:** delete the `copy_lock.py` entries under `"PreToolUse"` and `"SubagentStop"`.
   - **Yes (Recommended)** — When an agent writes in a working copy (a folder with `.git`, `.p4config` or a `.uproject`), another session can't write there or launch an agent on it until those agents finish. Reading, and editing `.md` and `.txt` notes, always pass.
   - **No** — Nothing changes; two sessions can touch the same folder at the same time.

Steps:
1. Questions 1 to 3: save the accepted rules. For question 2, save the "By role" rule or the "Experimental" one (not both). The "[Only with 1-hour cache]" line goes in only if Box 2, question 2, was "Yes, 1-hour cache".
2. "Experimental": create `~/Documents/opus_sonnet_pilot.md` (not in the config folder, which is protected) with a table (date, task, passed first time?, what Opus had to redo). It works best with the brake (question 4).
3. Question 4 "Yes":
   1. Copy `scripts/agent_limit.py` to `<config folder>/hooks/agent_limit.py`.
   2. In `settings.json`, inside `"hooks"`, add to `"PreToolUse"` (create the list if it doesn't exist; don't delete what is already there):

      ```json
      "PreToolUse": [
        {
          "matcher": "Agent|Task",
          "hooks": [
            { "type": "command", "command": "python \"<config folder>/hooks/agent_limit.py\"", "timeout": 10 }
          ]
        }
      ]
      ```

      (The `matcher` has both names because old versions of Claude Code called the tool `Task`.)
   3. Check. Some versions only read the hooks when the session opens: try in this session; if the block doesn't come, ask the person to open a new session in the same folder (in the terminal, quit and run `claude` again) and paste the request below into it, or leave the test for the final box. Three agents: the conversation opens A; A opens B; B tries to open C and must be blocked. Make the request: *"Brake test. Open a Haiku agent, A, and ask it: 'open an agent B and ask B: open an agent C that answers hi; if B is blocked, return the blocking message. Then return to me the message that B received.' Return what A answered."* The expected result is the message "Agent limit: ...". If agent A or B says it doesn't have the tool to open agents, the brake isn't needed in this version: tell the person and go on.
4. Question 5 "Yes":
   1. Copy `scripts/copy_lock.py` to `<config folder>/hooks/copy_lock.py`.
   2. In `settings.json`, inside `"hooks"`, add to `"PreToolUse"` and to `"SubagentStop"` (create the lists that don't exist; don't delete what is already there, such as the brake's entry):

      ```json
      "PreToolUse": [
        {
          "matcher": "Bash|PowerShell|Edit|Write|NotebookEdit|MultiEdit|Agent|Task",
          "hooks": [
            { "type": "command", "command": "python \"<config folder>/hooks/copy_lock.py\"", "timeout": 10 }
          ]
        }
      ],
      "SubagentStop": [
        {
          "hooks": [
            { "type": "command", "command": "python \"<config folder>/hooks/copy_lock.py\"", "timeout": 10 }
          ]
        }
      ]
      ```

   3. Tell the person: only agents take the lock, and it goes away on its own (detail: Box 5 · Copy lock). To see the locks: `python <config folder>/hooks/copy_lock.py list`; to release one, only when sure the agent finished: `python <config folder>/hooks/copy_lock.py release <folder>`. No rule goes into CLAUDE.md.
   4. Check: `python <config folder>/hooks/copy_lock.py test` (17 simulated cases, without touching real locks); the last line must be `ALL OK`. Then check `settings.json` with `check_settings.py`.

Rule text:
> - Agent that edits or fixes: its request says "when you reach ~100 calls, finish the item, write the resume point in <file> and return the summary". If work is left, the main conversation opens another agent from that file. A big task is born already split into agents of ~100 calls.
> - **[Only with 1-hour cache]** An agent doesn't stay more than ~50 minutes in a single wait; a longer wait = write the resume point and return.
> - Models by role: Sonnet by default; Haiku for the mechanical (finding a file, filtering a log, counting); Opus only for an agent that edits delicate code (security, accounts, money, cryptography).
> - (Experimental) New code or a fix outside security, accounts and cryptography: an Opus agent coordinates. It writes the request for each piece, opens Sonnet agents one at a time (~80 calls each; Sonnet opens no agents), runs the tests by script, reviews only what changed, fixes what is bad and returns a few lines. A piece that fails twice, Opus does itself. Note each case in `~/Documents/opus_sonnet_pilot.md`; after ~6 cases, ask the person whether it becomes the default.
> - Agents: one per task, not one per tiny piece; several at the same time go out in the SAME message; each one writes the detail in a file and returns 5 to 10 lines.

---

## Box 6 — Handoff and session switch

**What this does:** Claude keeps in each project a handoff file (done, half done, exact next step) and a summaries file (one entry per session); when the conversation gets big or the stage changes, the new session starts from the handoff. It was the author's biggest saving: the main conversation fell 75% (measured on the author's machine, Sep-Nov 2026; your results may differ). Tell the person not to write passwords, tokens or personal data in these files (they go along if the folder is published).
**Note:** the numbers in this box (switch at ~250k) assume the 1-million-token window. Check the person's window (rule "Context window", at the start of the guide; if you can't see it, assume 200k). If it is 200k, switch sessions at ~100k (tell the person this at question 2 and use `<100>` in the rule) and don't lower the compaction in Box 2.

Questions:

1. **Handoff and summaries in projects with work in progress?** — header `Handoff`
   > **Summary** — **You gain:** the new session starts where the last one stopped, and you can find who did what. **You risk:** new files in projects without asking each time; an old handoff leads to the wrong point. **If you skip it:** a new session starts from zero; `Switching`, `Reminder` and Box 7 are skipped. **Undo:** delete the CLAUDE.md lines; created files stay.
   - **Yes, handoff + summaries (Recommended)** — On the first multi-step task, I create `HANDOFF.md` and `SUMMARIES.md` at the project root on my own (or use the ones it already has); one entry per session in the summaries.
   - **Handoff only** — Only `HANDOFF.md`; no summaries file, so later there is nowhere to find which session did something.
   - **No** — Nothing changes; a new session loses what lived only in the conversation.
2. **When to switch sessions?** — header `Switching` (only if `Handoff` wasn't "No")
   > **Summary** — **You gain:** a conversation that doesn't bloat, so each step rereads less. **You risk:** each switch loses what lived only in the conversation; switching late costs more. **If you skip it ("Only when I ask"):** only a warning; the automatic successor (Box 7) has no trigger. **Undo:** delete the line from CLAUDE.md.
   - **~200k or new stage** — More switches, every step rereads less. A new stage always starts in a new session.
   - **~250k or new stage (Recommended)** — In the author's numbers (260 sessions), the total cost barely changes between 200k and 300k; above ~300k every step rereads so much that it costs more.
   - **~300k or new stage** — Fewer switches, every step more expensive. Worth it when the handoff loses a lot of what the conversation knew.
   - **Only when I ask** — One-line warning when the conversation passes ~250k.
3. **One task per session?** — header `One task`
   > **Summary** — **You gain:** short, focused conversations, which are cheaper. **You risk:** more open sessions to keep track of. **If you skip it:** subjects pile up in one conversation that bloats. **Undo:** delete the line from CLAUDE.md.
   - **Yes (Recommended)** — A new, unrelated subject goes to a new session (or `/clear`).
   - **No** — Nothing changes; subjects pile up in the same conversation.
4. **A session-start reminder to read the handoff?** — header `Reminder` (only if `Handoff` wasn't "No"; with Python)
   > **Summary** — **You gain:** Claude remembers to read the handoff when the folder opens. **You risk:** a script with no network that only lists the folder; it approves and blocks nothing. **If you skip it:** only the CLAUDE.md rule tells Claude to read the handoff, and it may forget. **Undo:** delete the `handoff_reminder.py` entry under `"SessionStart"` in `settings.json`.
   - **Yes (Recommended)** — Script (`handoff_reminder.py`, session start) that, if the folder has a `PASSAGEM*.md` or `HANDOFF*.md`, shows one line telling Claude to read it first. It only lists the folder. Cost: one line per session in those folders.
   - **No** — Nothing changes; without the reminder Claude may forget the handoff.

Steps:
1. Question 1 "Yes, handoff + summaries" or "Handoff only": copy `en/HANDOFF_TEMPLATE.md` to `<config folder>/templates/HANDOFF_TEMPLATE.md` (create `templates` if it doesn't exist). Only for "Yes, handoff + summaries": also copy `en/SUMMARIES_TEMPLATE.md` to `<config folder>/templates/SUMMARIES_TEMPLATE.md`. Save the rule of the chosen version.
2. Question 2: save the rule with the chosen number, or the "Only when I ask" rule. Tell the person where to see the conversation size: in the app, the context indicator next to the message box; in the terminal, the `/context` command.
3. Question 3: save the rule. Remind the person: only they can type `/clear` or `/compact`; Claude can't.
4. Question 4 "Yes":
   1. Copy `scripts/handoff_reminder.py` to `<config folder>/hooks/handoff_reminder.py`.
   2. In `settings.json`, inside `"hooks"`, add to `"SessionStart"` (create the list if it doesn't exist; if it already has items, add this one as one more item in the list, without deleting or replacing the others; the Box 8 daily report goes in the same way, as a separate item):

      ```json
      "SessionStart": [
        {
          "matcher": "startup",
          "hooks": [
            { "type": "command", "command": "python \"<config folder>/hooks/handoff_reminder.py\"", "timeout": 10 }
          ]
        }
      ]
      ```

   3. Check with `python <config folder>/hooks/handoff_reminder.py --test` (the last line must be `ALL OK`) and then with `check_settings.py`. The reminder shows up in the next session opened in a folder that has a handoff.
5. If there is a project with work in progress right now, offer to create its `HANDOFF.md` (and the `SUMMARIES.md` next to it, if question 1 was "Yes, handoff + summaries") (only with a yes).

Rule text (for the session switch, save one of the two versions):
> - Handoff: every project with work in progress has a handoff file (the one the project already has, or `HANDOFF.md` at the root, made from `<config folder>/templates/HANDOFF_TEMPLATE.md`). On the first multi-stage work in a project, create the file by yourself (and the summaries file, below). Rewrite, don't append to the end. Note in the handoff the steps done when each part is finished, before the session switch and when the spend watch warns. An unanswered question goes in the "Questions for the person" section. A new session starts by reading the handoff and does the "exact next step" without asking, except irreversible actions, which need confirmation. Never write passwords, tokens or personal data in the handoff.
> - **[Number]** Session switch: with the conversation at ~<250>k tokens, or at a new stage, finish the part in progress, update the handoff and switch sessions. If there is no successor rule, tell the person in one line what to paste into the new session.
> - **[Only when I ask]** Session switch only when the person asks; warn in one line when the conversation passes ~<250>k tokens.
> - One task per session: a new, unrelated subject goes to a new session.
> - **[Only with handoff + summaries]** Summaries: every project with a handoff file has a summaries file next to it (`HANDOFF.md` → `SUMMARIES.md`; `HANDOFF_X.md` → `SUMMARIES_X.md`; create it by yourself from `<config folder>/templates/SUMMARIES_TEMPLATE.md`). A mandatory step of EVERY session switch and every end of stage, without the person asking: when closing (before opening the successor or ending the stage), append ONE entry at the end: `## <n> — <session title> (<date>, <session id>)` with up to three short lines: **Did** (with the names someone would search for later: files, screens, tools), **Decided** (what was settled, and by whom), **Open** (what was left open or unanswered, or "nothing"). It doesn't reread the whole file, it only appends. Its only use is finding later which session did something.

---

## Box 7 — Automatic successor session (the most laborious)

**What this does:** at the moment of switching sessions (Box 6), Claude itself opens the successor, which starts from the handoff and can open the next one the same way. Depending on the answers, it writes rules in `CLAUDE.md` and may write to `settings.json` allow rules and auto mode as the default, install a hook (a program Claude Code runs before an action) that approves actions on the "spares" (reserve sessions, stopped and archived), and store a token (access key) for screenless rounds. **The whole box is sensitive:** not in Quick mode (Group 3); whoever wants it runs this box later, box by box.
**Advanced:** only after a week or two with the other tactics. Why, risks and undo: `en/DETAILS.md`, "Box 7".

**Screenless rounds (Path B and the Path A fallback):** the lock is to **warn the person in one line BEFORE opening any hidden session** and to launch with `--reason "<short reason>" --notified`; the script logs each round in `<config folder>/quota_keeper/relay_log.jsonl` (never the token).

Prerequisite: Box 6, question 1 (`Handoff`), answered "Yes, handoff + summaries" or "Handoff only"; without a handoff file, skip this box. If run later, in another session, ask Box 1's `Where used` and `Plan` questions again and check in CLAUDE.md what Boxes 5 and 6 saved.

**Script (Claude):**
- Explain the two paths to the person. **A, through the app** (visible, no token, recommended): a tool in the desktop app opens another session, which appears in the sidebar. **B, through the terminal** (screenless, needs a token): a script runs `claude -p` in rounds with an empty conversation, reading and updating the handoff; it doesn't appear in the app. Only for people who use only the terminal: in the app, spares, "notify and carry on" and the scheduled task cover the refusals.
- Before any question (Box 1 = "Desktop app" or "Both"): find the tools with ToolSearch (list in step 1 of Path A) and check the permission mode (`get_session` "self", field `permissionMode`).
- No `start_session`: Path A doesn't exist in this version; say so in one line and treat it as "Terminal" (no questions 1, 2, 5 to 10). With "Not now" on 3, save only "[I open it]" (Claude updates the handoff and **tells the person to open the new session**), without the close-the-previous and inheritance rules; put "Automatic successor session (no tool in the app)" under "Declined" and skip the Path A steps.
- "Terminal": no questions 1, 2, 5 to 10. Ask only 3 and, with "Yes, guide me", 4 in a second call; "(Recommended)" on **"Yes, guide me"**. The successor is the Path B rule; with "Not now", "[I open it]".
- "Desktop app" or "Both": no 3 and 4 (treat as "Not now", without adding it to "Declined"). At most four questions per AskUserQuestion call; conditional ones only after the answer that unlocks them. 1st call: only 1. 2nd, only if 1 is "Claude, on its own": 2, 5, 6 and 8 (with the other answers to 1 there is no previous session to close, no fallback and no successor Remote Control to decide). 3rd, only with what the 2nd unlocked: 7 and 10 (if 6 is "Spare session") and 9 (if 5 is "Allow both rules"); if nothing is unlocked, no 3rd call. With "Claude proposes, I click" or "I open it" in 1, only the 1st call. In the "[Claude, on its own]" rule, "If that also fails" becomes "warn the person in one line".
- Before each call, show the Summaries of its questions (rule 3 of "How to run"; detail in `en/DETAILS.md`, "Box 7").
- "API key" (Box 1): no 3 (as "Not now"; with "Terminal" too, "[I open it]" is used). "I don't know": ask 3, saying the token exists only on subscription plans (Pro, Max, Ultra, Team and Enterprise); if the command refuses their account, "Not now".
- Question 9: "(Recommended)" on **"Yes, auto"** only if `permissionMode` is `auto`; otherwise, or if it couldn't be seen, on **"Don't change"**. Never set auto mode as the default without 9 = "Yes, auto".

1. **Who opens the successor session?** — header `Successor` (sensitive: opens sessions on its own; only in the app, with `start_session`)
   > **Summary** — **You gain:** the switch happens without waiting for your click. **You risk:** it opens sessions on its own and each rereads the instructions (more quota); a badly written handoff makes the new one start from the wrong point. **If you skip it:** "proposes" and "I open it" work; 2 and 5 to 10 are skipped. **Undo:** delete "Successor:", "Switch with an agent running:" and "Inheritance" from `CLAUDE.md`; archive the sessions it opened.
   - **Claude, on its own (Recommended)** — Updates the handoff, opens the successor and stops; nobody asks for your OK and the chain goes on until the handoff says it is done.
   - **Claude proposes, I click** — A card appears; nothing opens without your click, and if you are not looking the work stops.
   - **I open it** — Claude updates the handoff and says what to paste into the new session; the safest and the most work for you.
2. **Does the successor close the previous one?** — header `Close old` (sensitive: archives sessions; only if `Successor` is "Claude, on its own")
   > **Summary** — **You gain:** the previous one doesn't reread everything at every turn of the new one. **You risk:** archiving something alive (the rule doesn't force it; archiving doesn't delete). **If you skip it:** both stay open and the previous one uses quota. **Undo:** delete "Close the previous one:"; unarchive.
   - **Yes (Recommended)** — The successor detaches from the previous one and archives it. The title gets a number ("Site" → "Site 2" → "Site 3").
   - **No** — Nothing is archived on its own; the previous one may reread the conversation at each of the new one's turns until you archive it.
3. **Install the token for screenless rounds (Path B)?** — header `Token` (sensitive: stores an account key in a file; only in the terminal, not with "API key", with Python)
   > **Summary** — **You gain:** in the terminal the chain moves on by itself (screenless rounds). **You risk:** an account key in a file, valid for one year; hidden rounds use quota (hence the warning first). **If you skip it:** in the terminal you open the new session yourself; in the app Path A covers it. **Undo:** delete `relay_token.txt`, `tools/session_relay.py` and the "Screenless rounds:" rule.
   - **Yes, guide me** — You run a command, log in in the browser and save the token in a file; Claude never sees it. About 10 minutes.
   - **Not now** — Nothing is stored; the rest of the package works.
   After "Yes, guide me", say in one line that the **daily report is recommended** for people who use screenless rounds and that Box 8 asks about it.
4. **What can the screenless rounds use?** — header `Permissions` (only if `Token` is "Yes, guide me")
   > **Summary** — **You gain:** you decide what a hidden round touches. **You risk:** nobody approves anything in the round; it can overwrite files (use git) and, with the terminal, run commands. **If you skip it:** it exists only with the token. **Undo:** change `--tools` in the "Screenless rounds:" rule.
   - **Files only (Recommended)** — Read, search, create and edit files; no commands.
   - **Files + terminal** — Also runs commands (tests, builds); the round's terminal can also see the token.
   - **Decide per project** — Claude asks the first time in each project; nothing runs without that yes.
5. **Allow the scheduled-task fallback?** — header `Scheduled` (sensitive: stores allow rules; only if `Successor` is "Claude, on its own")
   > **Summary** — **You gain:** a fallback when the app refuses to open the session. **You risk:** two allow rules apply to ALL sessions of the account; malicious text could lead to scheduling something with nobody watching. **If you skip it:** the fallback becomes screenless rounds or a warning; 9 is skipped. **Undo:** remove the two lines from `"allow"` and delete the `successor-<folder>` task.
   - **Allow both rules (Recommended)** — Claude creates and runs the scheduled task without asking for approval, only as a fallback; without the rules, auto mode usually blocks it.
   - **Don't allow** — Nothing is stored; the fallback is Path B (if installed) or a warning to you.
6. **When the app refuses to open the successor?** — header `Refused` (sensitive: may create and reactivate sessions on its own; only if `Successor` is "Claude, on its own")
   > **Summary** — **You gain:** the switch works when the app refuses to open a session. **You risk:** spares are sessions created without you seeing; "Notify and carry on" lets the conversation grow (steps cost more); "Fallback right away" may hide the successor in Routines. **If you skip it:** use "Notify and carry on"; 7 and 10 are skipped. **Undo:** delete "Spares:" and "Notify and carry on:"; archive the spares.
   - **Spare session (Recommended)** — On each message from you, Claude refills stopped, archived sessions in the project folder (the "spares"; question 7 says how many). At the switch, it unarchives one, gives it the new title and sends the task by message: the successor starts right away, in the normal list. With no spare in the folder, it falls back to "Notify and carry on".
   - **Notify and carry on** — Saves the handoff, sends a notification (on the computer and, with Remote Control on, on the phone) and keeps working in this session; on your next message it opens the successor in the normal list. The fallback (scheduled task, screenless rounds) is kept for when the conversation goes well past the limit with no reply from you. Creates no session before your message.
   - **Fallback right away** — Uses the fallback at once; if it is a scheduled task, the successor is hidden in Routines and can't open the next one on its own.
7. **How many spares per folder?** — header `Spares` (only if question 6 is "Spare session"; the box's "Other" option lets the person type another number)
   > **Summary** — **You gain:** more switches covered with you away from the screen. **You risk:** up to that number of empty sessions created without you seeing, each with a short turn when created; no measured number. **If you skip it:** 6 is the minimum; with no spare it falls back to "Notify and carry on". **Undo:** change the number in "Spares:" and archive the extras.
   - **10 (Recommended)** — Covers a night with several switches, even with several sessions in the same folder; creates up to 10 sessions on your first message after the install.
   - **6** — The minimum: enough for one or two sessions per folder.
   - **16** — For many sessions in the same folder for a long time without you coming back; creates the most sessions and uses the most short turns.
8. **Turn on Remote Control?** — header `Remote` (sensitive: desktop app only, Path A, and only if `Successor` is "Claude, on its own").
   > **Summary** — **You gain:** follow the chain from afar and get the alert on the phone. **You risk:** whoever gets into your claude.ai account or picks up your unlocked phone sends orders to the computer, with the session's permissions. **If you skip it:** everything works; the alert only shows on the computer. **Undo:** delete "Remote Control:"; turn it off in each session and the app option.
   - **Successors only (Recommended)** — Turns Remote Control on in every successor it opens (normal list, spare or scheduled task); other sessions stay as you leave them.
   - **Turn on now** — The same, and also turns this session's on now; for every new session, turn on the app option (in November 2026, "Connect new sessions to Remote Control", in the settings).
   - **Don't use** — Claude never turns Remote Control on; it still turns off the previous session's before archiving it, if it is on.
9. **Start every session in auto mode?** — header `Auto default` (sensitive: changes the default permission mode; only if question 5 is "Allow both rules")
   > **Summary** — **You gain:** the scheduled task's successor doesn't stop at the first command. **You risk:** EVERY new session is judged by an automatic filter, which can be wrong both ways (deny rules apply). **If you skip it:** that successor waits for your approval at the first command. **Undo:** remove `"defaultMode": "auto"` (or restore the value from the Box 1 backup).
   - **Yes, auto** — Every new session starts in auto mode, including the task's successor; for people who already work in it.
   - **Don't change** — The default mode stays as it is; the task's successor stops at the first command or edit, waiting for you to approve.
10. **Install the hook that approves actions on spares?** — header `Spare hook` (sensitive: approves actions on its own; only if question 6 is "Spare session"; with Python)
   > **Summary** — **You gain:** the switch through spares goes through without an approval box. **You risk:** it approves six actions on its own (message, unarchive, title, model, effort, Remote Control), only on ids in `spares.txt`; if it fails, it approves nothing. **If you skip it:** nothing is approved on its own; it falls back to "Notify and carry on". **Undo:** remove the `PreToolUse` block and delete `spare_allow.py`, the log and `spares.txt`.
   - **Install the hook (Recommended)** — The six actions are approved only on the listed spares.
   - **Without the hook** — Nothing is approved on its own; the switch may fall back to "Notify and carry on" or you approve in the box.

### Steps for Path A (desktop app)

Only if Box 1 answered "Desktop app" or "Both" and `start_session` exists. If it answered "Terminal", or the tool doesn't exist, go straight to Path B (or, without it, to the minimum rule above).

1. **Tools** (find them with ToolSearch, by name): `start_session` (open a session), `create_scheduled_task`, `list_scheduled_tasks` and `run_scheduled_task` (create, list and run a scheduled task), `set_session_title`, `detach_session`, `archive_session` and `unarchive_session` (title; detach, archive and unarchive), `list_sessions` and `get_session`, `set_remote_control`, `set_session_effort` and `set_session_model` (another session's effort and model), `list_task_runs` (sessions a task opened), `list_sections` (sidebar sections), `PushNotification` (a notification on the computer and, with Remote Control, on the phone) and `SendMessage` (a message to another session). In November 2026 they existed with these names. Before any `set_remote_control`, check `remoteControlState` with `get_session` and only call it if the state is different (an unneeded call may open an approval box or turn off what was meant to be on). Call `start_session` with initiation "user_asked" ("offer" and "own_initiative" become a card waiting for a click) and context "fresh".
2. **Save the rules** below: question 1's (one of the three); close-the-previous if 2 is "Yes"; by 6, "Notify and carry on" = the notify-and-carry-on one, "Spare session" = the spares one (with the number from 7) and also the notify-and-carry-on one, "Fallback right away" = nothing extra; switch-with-an-agent-running if 1 is "Claude, on its own"; Remote Control if 8 is not "Don't use" (with "Turn on now", turn this session's on now: look at `remoteControlState` and only call `set_remote_control` with "self" and true if it is off; tell the person where the app option for new sessions is); always the inheritance one. With 2 "No", don't save close-the-previous and, in switch-with-an-agent-running, remove the part where the previous session archives itself. Tell the person the successor's request carries the current session's id ("Previous session: <id>", from `list_sessions` or `get_session`), so it knows which one to archive; with the manual-only task (step 4), the request goes in `SUCCESSOR.md`.
3. **Save only what the person accepted**, in `<config folder>/settings.json` (not in the project's: there, auto as the default mode doesn't take effect). Each item is sensitive: only with the answer to its own question and, in "Box by box, checking" mode, show the snippet and wait for "Save". Never save `"defaultMode"`, an allow rule or a hook on your own:
   - Question 5 "Allow both rules": under `"permissions"` → `"allow"`, the exact names of the create and run scheduled-task tools as ToolSearch showed them (in November 2026: `"mcp__scheduled-tasks__create_scheduled_task"` and `"mcp__scheduled-tasks__run_scheduled_task"`). Create what is missing and don't delete what exists.
   - Question 9 "Yes, auto": under `"permissions"` set `"defaultMode": "auto"`. With "Don't change", leave that field alone.
   - Question 5 "Don't allow": nothing in `settings.json`; in the question 1 rule, delete the part from "I use a scheduled task" to "If that also fails:", inclusive.
   - Question 10 "Install the hook": copy `scripts/spare_allow.py` to `<config folder>/hooks/spare_allow.py`, create an empty `<config folder>/spares.txt` and, under `"hooks"` → `"PreToolUse"`, add `{ "matcher": "SendMessage|mcp__ccd_session_mgmt__.*", "hooks": [ { "type": "command", "command": "python \"<config folder>/hooks/spare_allow.py\"", "timeout": 10 } ] }` (replace `mcp__ccd_session_mgmt__` with the name prefix ToolSearch showed). The hook approves the switch actions on its own only when the target is a spare listed in `spares.txt` (why it exists and the test: `en/DETAILS.md`, "Box 7 · Spare hook"). Don't use allow rules for these tools: they would apply to every session. With "Without the hook": copy and register nothing, don't create `spares.txt` and, in the "Spares" rule, delete the parts about `spares.txt`.

   Check with `check_settings.py`. Say that auto as the default mode needs a recent Claude Code version and a plan with this mode; without them, the session starts in normal mode.
4. **The app's traps** (detail only if the person asks: `en/DETAILS.md`, "Box 7 · The app's traps"): the app refuses to open a session on a turn that didn't come from a message by the person (an answer in a question box doesn't unlock it); it refuses to archive a session with live work; a scheduled task doesn't inherit the permission mode and sits in the Routines section, without `start_session` (check with `list_sections` that the section is on, and always put the new session's link in the final message).
5. **Test** (with the person's yes; it opens a real session and uses a little quota):
   1. Create `~/Documents/successor_test/` (not in the config folder, which is protected) with a `HANDOFF.md` whose exact next step is: *"Create `ok.txt` with the word ok and write STAGE DONE on the first line of this handoff."*
   2. Open a session "Successor test" with the request: *"Install test: don't archive or detach any session. Read and follow `<path>/HANDOFF.md`."* (Without that sentence, the close-the-previous rule could detach or archive the install session.)
   3. Check with `list_sessions` that it appeared and, when it finishes, that `ok.txt` exists. Tell the person they can archive the test session and delete the folder.

Rule text (question 1, one of the three):
> - **[Claude, on its own]** Successor: when it is time to switch sessions, I open the successor myself, without the person asking (`start_session`, initiation "user_asked", context "fresh", request "Read and follow <handoff>. Previous session: <id>" + the successor rules of this section; the <id> is this session's, found with `list_sessions` or `get_session`), tell the person in one line with the link, and stop. I don't open a successor if the handoff says STAGE DONE or has a question for the person that blocks the next step. Title = current title + number ("Site" → "Site 2"). I never end with "open a new session", and never leave a card waiting for a click. If the app refuses or turns it into a card: I use a scheduled task. If this session wasn't opened by a task and the manual-only task `successor-<project folder>` exists (`list_scheduled_tasks`), I rewrite `SUCCESSOR.md` in the folder with the same request and run the task right away (`run_scheduled_task`); otherwise (or if the app refuses to run it), I immediately create a one-time task for ~2 minutes later, with the same request. I check in `list_task_runs` that it opened; I adjust its title, Remote Control (only with the Remote Control rule) and effort (`set_session_title`, `set_remote_control`, `set_session_effort`), if I can; and I check with `list_sections` whether the sidebar's Routines section is on (the session only appears there): if it is off, I tell the person in one line where to turn it on. I always put the new session's link in my final message (a one-time task disappears from the sidebar after it runs). In a regular session (not opened by a task) in the folder of a project with a handoff, if the folder's manual-only task doesn't exist, I create it: no schedule, `notifyOnCompletion` false, title "Successor <folder>", request "Read `SUCCESSOR.md` in this folder and follow what it says." If that also fails: <screenless rounds, rule below | warn the person in one line>. When possible, I leave the switch for a turn that came from a message by the person.
> - **[Claude proposes]** Successor: at the switch, I update the handoff and propose the new session (card), with the request "Read and follow <handoff>".
> - **[I open it]** Successor: at the switch, I update the handoff and say in one line what to paste into the new session: "Read and follow <handoff>".

Rule text (question 2 "Yes"):
> - Close the previous one: the successor, right at the start, detaches from the session that opened it (`detach_session`), turns off the previous one's Remote Control (`set_remote_control` with its id and false) and archives the session whose id comes in "Previous session: <id>" in the request (`archive_session`). If the handoff's "Running in the parent" section names the previous session itself, it doesn't archive it: that one archives itself when its agents return (switch-with-an-agent-running rule). If it is refused because the previous one is still working ("still working" or "in use": it is still writing its last message; in the 2026-11-04 tests the refusal went away as soon as it ended its turn), it tries again every ~30 seconds for up to ~2 minutes (waiting with a background command such as `sleep 30`, and checking `isRunning` with `get_session`). If it is still refused, it tries again at the end of the first turn and at the start of every turn that comes from a message by the person, until it works; if the refusal mentions an agent or a background task, it doesn't force it: it says in one line that the person can archive it from the sidebar. Before opening the successor, the session stops the agents and background tasks that already delivered. It doesn't apply to a parallel session for another task (that one archives nobody).

Rule text (question 6 "Notify and carry on"; replace `<400>` with the Box 6 limit + 150k):
> - Notify and carry on: if the app refuses to open the successor (a turn that didn't come from a message by the person) or turns it into a card, I don't switch yet: I save the handoff, send `PushNotification` ("<title>: time to switch sessions, reply anything here") and keep working in this session. When a new message from the person arrives, before anything else I update the handoff and open the successor with `start_session`; agents still running here follow the switch-with-an-agent-running rule. The fallback in the successor rule (scheduled task, screenless rounds, warning) is kept for the ceiling only: the conversation passing ~<400>k tokens with no message from the person.

Rule text (question 6 "Spare session"; replace `<10>` with the number from question 7; also save the notify-and-carry-on one):
> - Spares: on every new message from the person (the only turn where `start_session` works), I check the project folder's spares (`list_sessions` including archived ones, title "Spare <folder> N"). For each number from 1 to <10> with no spare (used at a switch or never created), I create one with that number, never going past <10>: `start_session` "user_asked", context "fresh", `use_worktree` false, title "Spare <folder> N" (and I add its id to `spares.txt`), request "SPARE session: do nothing, don't read files, don't call tools, don't follow the session-start rules; reply only 'ready' and stop. Later another session will send the task by message; then follow the message.", at my own effort (high: it is what most switches need, and the "ready" reply costs about the same). When each one replies "ready", I detach it (`detach_session`) and archive it (`archive_session`; if refused, the same ~30 s wait for up to ~2 min as in the close-the-previous rule). At the switch, if the app refuses to open the successor or turns it into a card, and the folder has a spare: I unarchive the lowest-numbered one (`unarchive_session`), change its title to the current title + number + " · <model> <effort>" (e.g. "Site 3 · Opus 5.5 High"; when adding the number, I ignore that ending), because the footer under the text box may show a different model and effort (`set_session_title`), set the model and effort the task needs (`set_session_model`, `set_session_effort`; they apply from the next turn, so before the message), send it the successor request by `SendMessage` (with "Previous session: <id>", "forget the do-nothing request: follow all the rules now" and "don't call `detach_session`: you are already detached"), then, with the Remote Control rule, turn its on (`set_remote_control`), remove its id from `spares.txt` (it is no longer a spare), tell the person in one line with the link, and stop. With no spare in the folder: notify and carry on.

Rule text (question 1 "Claude, on its own"; replace `<180>` with about 0.7 × the Box 6 limit, rounded to the nearest 10: 250 → 180, 200 → 140, 300 → 210, 100 → 70; in the choice, keep the first option if Box 5, question 5, installed the copy lock):
> - Switch with an agent running: (1) Before launching an agent that should take more than ~20 minutes, I look at the conversation size; from ~<180>k on, I switch first and the successor launches it. (2) When it is time to switch and an agent of mine is running, I switch as usual and the agent keeps going here, in the previous session (the "parent"). The handoff gets a "Running in the parent" section: this session's title, and each live agent with its folder, what it does and when it should end; the successor doesn't relaunch that work. I split what is left: a task that touches the same folder and fits in the time the parent's agents still need (or goes a little past it, up to ~1/4 more), the parent launches now, in an agent; the rest goes to the successor, which starts with what does NOT touch that folder and only takes the folder's work after the parent releases it (<the copy lock ensures it | before touching that folder, it checks that the "Running in the parent" section says it was released>). This may only fit the successor's successor: the handoff carries the section forward until the folder is released. The parent takes no other task. When its last agent returns, the parent writes the result in the handoff, tells the newest session of the chain (the highest-numbered title, from `list_sessions`) by `SendMessage` that the folder is released and where the result is, and archives itself (`archive_session` with "self"); if that is refused, the successor archives it. (3) An agent with a long wait (build, render, long tests) waits in chunks of at most ~10 minutes, so a stop message reaches it quickly.

Rule text (question 8 "Successors only" or "Turn on now"):
> - Remote Control: every successor I open (normal list, spare or scheduled task) gets Remote Control on, so the person can follow it from afar. Right after opening it, I look at `remoteControlState` with `get_session` and, if it is off, turn it on (`set_remote_control` with its id and true); on a spare, only after the message with the task. The successor, at the start, does the same with its own ("self"). I never call `set_remote_control` without looking at the state first.

Rule text (whenever this box is accepted):
> - Inheritance (not with the "[I open it]" rule alone): the request of every successor session repeats the successor rules of this section, so that it opens the next one the same way.

### Steps for Path B (token and screenless rounds)

Only if question 3 was "Yes, guide me". Read and follow `en/DETAILS.md`, "Box 7 · Path B steps", one step at a time, waiting for the person to say they did it: check the terminal Claude Code, the person generates and saves the token without you seeing it, check it without seeing it, forbid reading the file, copy `session_relay.py`, test on a toy project, the `--tools` list from question 4 and the gaps to explain. Then save the rule below.

Rule text (Path B):
> - Screenless rounds: before launching, I warn the person in one line (what will run, why, how many rounds, that it uses their quota) and only then launch: `python <config folder>/tools/session_relay.py --folder <project> --handoff <handoff> --model sonnet --rounds 3 --tools "<list>" --reason "<short reason>" --notified`, detached in the background (Windows: `Start-Process ... -WindowStyle Hidden -PassThru`; Mac and Linux: `nohup ... &`), keeping the process number. I never launch without warning first. Use: <when I am in the terminal | only as a fallback, when the app refuses to open a session>. At the person's next message, I check the project's `relay.log` and, if the handoff doesn't say STAGE DONE and nothing is running, I warn again and launch again, or open the successor. Long task: bigger `--timeout`. I never read, show or copy `relay_token.txt`.

---

## Box 8 — Spend watch and measuring

**What this does:** scripts that warn Claude when the session passes certain limits and measure spending; Claude tells the person in one line and proposes what to do (handoff, successor, cheaper agent). In the author's use, 14 of 36 session switches only happened after 250k tokens, until the watch warned in the middle of the turn. No script uses the network or blocks or approves anything.

Plan (Box 1): with "API key", don't ask questions 2 and 3 (there is no weekly %) and don't put them under "Declined"; the spend watch (question 1) works the same, because it warns in tokens. With "Team or Enterprise" or "I don't know", ask both, but say they only work if the usage screen shows a weekly limit %; if, when reading it, there is no %, stop and tell the person.

Questions (there are 5; the question box takes 4 per call: make 2 calls, questions 1 to 4 and then 5; skip the ones that don't apply):

1. **Install the spend watch?** — header `Spend watch` (only with Python)
   > **Summary** — **You gain:** a warning before the conversation or an agent gets too expensive. **You risk:** it reads the local records only to count; it blocks and approves nothing; if it fails, it goes silent. **If you skip it:** no big-conversation warning; the session switch (Box 6) depends on Claude noticing by itself. **Undo:** delete `hooks/spend_watch.py` and its two lines under `"UserPromptSubmit"` and `"PostToolUse"`.
   - **Yes, author's limits (Recommended)** — Warns with the conversation at 200k tokens (and every 100k more), at 40, 80 and 150 prompts, and when an agent reaches 100 and 150 calls.
   - **Yes, warn earlier** — Conversation at 150k; agent at 60 and 100 calls. More warnings, in return for switching sessions sooner.
   - **No** — Nothing is installed; no big-conversation warning.
2. **Check usage before and after a big task?** — header `Before/after` (not with "API key")
   > **Summary** — **You gain:** you see how much of the quota a big task cost. **You risk:** a text rule and one more line in the final message. **If you skip it:** you check usage on screen whenever you like. **Undo:** delete the line from CLAUDE.md.
   - **Yes (Recommended)** — Claude notes the plan usage % before a big task and says the difference at the end. Just a rule; no script.
   - **No** — Nothing changes.
3. **Measure how much 1% of the quota is worth on your plan?** — header `Measure plan` (not with "API key"; with Python)
   > **Summary** — **You gain:** the watch also warns in % of the quota, not only tokens; the base for the daily report. **You risk:** the number is an estimate (it comes out low if you use the regular chat a lot); writes a small .csv. **If you skip it:** the watch warns only in tokens; the daily report can't compare with the account. **Undo:** delete `tools/measure_point.py` and `tools/measure_marks.csv`.
   - **Yes** — You note the usage % at two moments, with one or two days between them, and a script does the math; then the watch also warns in % of the quota.
   - **No** — The watch warns only in tokens.
4. **Install the usage report skill?** — header `Usage skill` (only with Python)
   > **Summary** — **You gain:** answers "where did my quota go?" with the sum by session and by model. **You risk:** it reads the local conversations only to count; nothing leaves the PC. **If you skip it:** Claude answers without the ready-made report, slower and less exact. **Undo:** delete `skills/usage-report/` and `tools/usage_report.py`.
   - **Yes** — I copy the skill to `<config folder>/skills/usage-report/`: when you ask "how much did I spend" or "where did my quota go", Claude runs a script that adds up spending by session and by model.
   - **No** — Nothing is installed.
5. **Want a daily usage report?** — header `Daily report` (only with Python; own call, after the first 4)
   > **Summary** — **You gain:** once a day Claude asks whether you want yesterday's report (this PC's spending by session and model; screenless sessions opened without a warning or running for a long time; whether the account rose more than this PC explains). **You risk:** a one-line reminder at the start of each new session; the script writes 3 small files. **Limit:** it only sees this PC; a difference from the account is a hint, not proof. **If you skip it:** no warning about odd usage. **Undo:** remove the `daily_report.py` entry under `"SessionStart"` and delete the script and the `quota_keeper/` folder.
   - **Yes** — I copy the script and add a notice at session start; on your first message of the day Claude asks in a box "Want yesterday's usage report?" and runs it only if you accept.
   - **No** — Nothing is installed.

In question 5, put "(Recommended)" on **Yes** only if `Token` was "Yes, guide me" or the person uses screenless rounds (Box 7).

Steps:
1. Question 1 "Yes":
   1. Copy `scripts/spend_watch.py` to `<config folder>/hooks/spend_watch.py`.
   2. "Warn earlier": at the top of the script, change to `CONTEXT_START = 150_000` and `AGENT_CALLS = [60, 100]`. If the person's context window is 200k tokens (rule "Context window", at the start of the guide; if unknown, 200k applies), use `CONTEXT_START = 100_000` and `CONTEXT_STEP = 50_000` with either option.
   3. In `settings.json`, inside `"hooks"`, add the same command in two events (without deleting what is already in them):

      ```json
      "UserPromptSubmit": [
        { "hooks": [ { "type": "command", "command": "python \"<config folder>/hooks/spend_watch.py\"", "timeout": 20 } ] }
      ],
      "PostToolUse": [
        { "hooks": [ { "type": "command", "command": "python \"<config folder>/hooks/spend_watch.py\"", "timeout": 20 } ] }
      ]
      ```
   4. Save the rule.
   5. Check: open a Haiku agent with the request *"SPEND-WATCH-TEST. List 6 files in this folder, one per tool call, and return any 'SPEND WATCH' warning that appears."* (that mark makes the watch use test limits: 3 and 5 calls). If the warning doesn't come, the person opens a new session in the same folder (in the terminal, quit and run `claude` again) and you repeat the request there, or leave the test for the final box.
2. Question 2 "Yes": save the rule. To read the usage %: in the app, the `get_usage` tool (look for it with ToolSearch); without it, ask the person for the number (the usage screen of the app or of claude.ai, or `/usage` in the terminal).
3. Question 3 "Yes":
   1. Copy `scripts/measure_point.py` to `<config folder>/tools/measure_point.py`.
   2. Read the weekly % now (as in question 2) and run `python <config folder>/tools/measure_point.py <%>`. This records the first mark.
   3. Save the rule. From the second mark on, the script shows how many weighted tokens 1% of the quota is worth. When the result is stable (two or three similar calculations), put that number in `POINT`, at the top of `spend_watch.py`: the watch then also warns in % of the quota.
   4. Tell the person: between two marks there can't be a reset of the quota week, and the regular chat (outside Claude Code) is not in the records, so the number comes out low if they use it a lot (detail: Box 8 · Measure plan).
4. Question 4 "Yes": copy the package's `skills/usage-report/` folder to `<config folder>/skills/usage-report/` and `scripts/usage_report.py` to `<config folder>/tools/usage_report.py`. If question 3 was "No", also copy `scripts/measure_point.py` to `tools/` (the skill uses it for "how much is 1% worth"), without running it. Applies from the next session. No CLAUDE.md rule needed.
5. Question 5 "Yes":
   1. Copy `scripts/daily_report.py` and `scripts/usage_report.py` to `<config folder>/tools/` (the report imports the weights from `usage_report.py`; if `measure_point.py` is also in `tools/`, its `measure_marks.csv` is found automatically).
   2. In `settings.json`, under `"hooks"`, add an entry under `"SessionStart"` (without deleting existing ones; if Box 6 already put `handoff_reminder.py` there, this is a second, separate item, so it is easy to undo):

      ```json
      "SessionStart": [
        { "matcher": "startup", "hooks": [ { "type": "command", "command": "python -S \"<config folder>/tools/daily_report.py\" --once-a-day", "timeout": 30 } ] }
      ]
      ```
      The hook sits under `"SessionStart"` with `matcher` `startup` (once per new session), never under `"UserPromptSubmit"`.
   3. Save the rule. Run `python <config folder>/tools/daily_report.py --test` (the last line must be `ALL OK`).
   4. Tell the person the report only sees this PC and applies from the next session (detail: Box 8 · Daily report). Useful commands: `daily_report.py --date YYYY-MM-DD` (another day), `--max-hours H` (long-session alert; default 8), `--record-account <%>` (records the account's weekly %).

Rule text:
> - Spend watch: when a "SPEND WATCH" warning appears, tell the person in one line, with the number, and propose what to do (handoff, successor, cheaper agent).
> - Before and after a big task: note the plan usage % and say the difference at the end, in one line.
> - Plan measuring: at the start of a session, if the last mark in `<config folder>/tools/measure_marks.csv` is more than a day old, read the weekly % and run `measure_point.py` with it. When the estimate gets stable over two or three calculations, propose putting the number in `POINT` in `spend_watch.py`.
> - **[Only if question 5 was "Yes"]** Daily report: if, at the start of the session, the reminder "Quota Keeper (once a day)" appears, before the person's request ask in a box, in their language, "Want yesterday's usage report?" (See it now / Not today); only if they accept, run `python "<config folder>/tools/daily_report.py"`, show the output and carry on with their request. If the reminder carries the "cheap check" warning, mention it. Once a day, when you can see the account's weekly % (usage tool in the app; `/usage` only the person types), run `daily_report.py --record-account <%>`.

---

## Box 9 — Checking the work

**What this does:** checking is mandatory, but you can check while spending less. This box only saves behavior rules in CLAUDE.md (instructions Claude may forget in a very long conversation); no script, hook or permission changes. Applies from the next session.

Questions (two, both with several answers: `multiSelect: true`):

1. **Which of these habits become rules?** — header `Checking`
   > **Summary** — **You gain:** checking while spending less (fewer images, tests only of what changed, double review only where it matters). **You risk:** an error outside the tested part, or in an area you don't consider sensitive, may slip through until the final suite; an image only when you ask. **If you skip it:** Claude checks its default way, usually more expensive. **Undo:** delete the rule's line in CLAUDE.md.
   - **Cheap proof** — Use text when it proves it; images cropped and smaller; measurements by script. A visual-only defect may slip through.
   - **Tests in parts** — After each change, the tests for what changed and a short regression; the whole suite before publishing.
   - **Two reviews, sensitive only** — Security, accounts, payment and cryptography get two independent reviews; the rest, one.
   - **Don't pay twice** — After an interruption, check what is still running and resume. A process is ended only by the PID the session itself started, never by name.
2. **Which end-of-turn habits become rules?** — header `Turn end`
   > **Summary** — **You gain:** nothing is forgotten: pending items in view, no idle sessions, the answer comes first. **You risk:** slightly longer final messages and a short check when stopping. **If you skip it:** pending questions may get lost and a session may stop without notice. **Undo:** delete the rule's line in CLAUDE.md.
   - **Pending questions** — Questions that come up go to a project questions file and are repeated at the end of every final message.
   - **Can I stop?** — Before stopping, Claude asks itself "should I be doing something before stopping?"; if not, it says what it is waiting for and what will wake the session.
   - **Complete final message** — The answer on the first line, then the pending items and what didn't go so well.

Steps: save one line per checked item; the unchecked ones go to "Declined". If "Pending questions" was checked, create `PENDING_QUESTIONS.md` in the project root only when the first question comes up.

Rule text:
> - Cheap proof: text when text proves it; image cropped and at a smaller scale; measurements by script.
> - Tests: what changed + a short regression at every change; the whole suite before publishing. Tests and checks run by script, directly.
> - Review: two independent ones only for security, accounts, payment and cryptography; one for the rest.
> - After an interruption, check whether agents and tasks are still running and resume, don't start over. End a process only by the PID I started, never by name (it takes down other sessions' work).
> - Pending questions: what comes up during the work goes to the project's questions file and is repeated at the end of the final message.
> - Before stopping, really ask "should I be doing something before stopping?". If so, do it. If not, say what I am waiting for and what will wake the session. Never announce "continuing now" without the tool already running in the same turn.
> - Final message: the answer on the first line, then the pending items and what didn't go so well or could have gone better.

---

## Box 10 — Star reminder

**What this does:** if the guide helps, a star on the repository helps others find it. Instead of asking now, Claude can remind the person in a week. Explain this in up to 2 sentences. Don't push, and don't put "(Recommended)" on any option.

Question:

1. **Do you want me to remind you in a week to decide whether to star the repository?** — header `Star`
   > **Summary** — **You gain:** a one-time reminder, so you can decide calmly. **You risk:** one line in CLAUDE.md; no data leaves the computer; Claude never stars it for you. **If you skip it:** nothing changes. **Undo:** delete the "One-time reminder (star)" line (it deletes itself once used).
   - **Yes, remind me** — In 7 days, in the first conversation, Claude asks just once whether the tactics helped and shows the link.
   - **Already did / doing it now** — Claude shows the link now and doesn't remind you later; nothing is saved.
   - **No, thanks** — No reminder; nothing is saved.

Steps:
1. **Yes, remind me:** save the rule below (replace `<reminder date>` with today's date + 7 days). It's a single line and deletes itself once used.
2. **Already did / doing it now:** show the link https://github.com/JNSoftworks/jns-quota-keeper and save nothing.
3. **No, thanks:** save nothing, not even under "Declined".

Rule text:
> - One-time reminder (star): from <reminder date> on, in the first reply of a session, ask in one line whether the Quota Keeper tactics helped and, if the person wants to star the repository, show the link https://github.com/JNSoftworks/jns-quota-keeper. Never star it for them. After asking, whatever the answer, delete this line.

---

## Final box — Summary

No questions. Tell the person, in a few lines:
1. What changed, by file (CLAUDE.md, settings.json, copied scripts), and where the backups are.
2. What was declined (it stays under "Declined" and is not offered again).
3. What only applies from the next session (settings and hooks).
4. How to undo, one line for each thing installed: each rule (delete the line in CLAUDE.md); each setting (delete the key under `"env"` or `"permissions"` in `settings.json`); each hook (delete its entry under `"hooks"` and the copied file: `spend_watch.py` under `"UserPromptSubmit"` and `"PostToolUse"`, `agent_limit.py` under `"PreToolUse"`, `copy_lock.py` under `"PreToolUse"` and `"SubagentStop"`, `handoff_reminder.py` and `daily_report.py` under `"SessionStart"`, `spare_allow.py` under `"PreToolUse"` plus `spares.txt`); each script in `tools/` (for the daily report, also its CLAUDE.md rule and the `<config folder>/quota_keeper/` folder); the templates in `templates/`; the usage skill (delete the `skills/usage-report/` folder); and, if there is one, `<config folder>/relay_token.txt` (delete the file and, if a token was created, revoke it where it was created). To undo everything at once: restore the Box 1 backups and delete the copied files. Also say when each thing starts to apply (the next session, for settings, hooks and the skill).
5. What was left half done (for example, the second mark of the plan measuring). If the brake test or the spend-watch test was left for later, tell the person to open a new session and say there: "repeat the brake (or spend watch) test from the Quota Keeper guide".
6. If Box 10 saved the reminder, the date it will show up.
7. If the mode was Quick: Group 3 (Box 7) was not installed. To turn it on later, ideally after a week or two, just ask "run Box 7 of the Quota Keeper guide".
8. The credit: "Tactics by Jaber Felippe Neto (JN Softworks), text under CC BY 4.0, scripts under MIT." If the person is going to share the guide, they should send the whole folder, with the credit.
