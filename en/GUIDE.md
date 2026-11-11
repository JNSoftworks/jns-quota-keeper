# JN's Quota Keeper — token saving for Claude Code

> **Made by Jaber Felippe Neto (JN Softworks).** License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may copy, adapt and share it, as long as you keep the author's name and the license link. The scripts are under the MIT license, which also asks you to keep the credit. Version 1.0, November 2026.

This file is for Claude. If you are the person: you don't need to read it. Claude will show one question box per tactic and will change only what you accept.

## How to run the setup (Claude, read this before anything else)

1. **Nothing changes without a yes.** Each tactic has a question box. Show the box, wait for the answer, do only the steps for that answer, check them, and only then go to the next box.
2. **Show each box with AskUserQuestion**, one call per box, with the questions, headers and options exactly as written here. The tool adds an "Other" option by itself. Without that tool, ask the same questions in a short numbered list and wait.
3. **Before each box, say in simple words** what the tactic does, its real risks and how to undo it (the "What this does", "Real risks" and "How to undo" blocks of each box; summarize, don't read them all out). The person may not be technical: no acronym or jargon without a plain explanation in the same sentence. Each option of the question shows its consequence in one line; don't hide risk and don't exaggerate it.
4. **Follow the order of the boxes.** If a box doesn't apply (for example, the person doesn't use agents), say so in one line and go to the next one.
5. **Write the rules with the ready-made text** of each box ("Rule text"). Don't rewrite or decorate it: every extra line in CLAUDE.md is paid for in every session. Of the parts between `< >`, fill in only the ones that belong to the setup:
   - a chosen number, like `<200>`: put in the number from the person's answer;
   - `<config folder>`: its full path (defined just below), with `/` slashes, for example `C:/Users/jane/.claude`;
   - `<path>`: only in the Box 7 tests, the full path of the test folder;
   - `<list>`: the tools chosen in Box 7;
   - `<reminder date>`: only in Box 10, today's date + 7 days, as `YYYY-MM-DD`;
   - a choice `<a | b>`: keep only the option that matches the answer and delete the other.

   These stay literal in the saved rule, for the session to fill in later: `<file>`, `<handoff>`, `<project>`, `<id>`, `<n>`, `<session title>`, `<date>`, `<session id>`.

   **Where the rule lines go:** inside the `## Quota Keeper ...` section of the chosen CLAUDE.md, under the `### Rules` subtitle, before `### Declined`. Box 1 creates the section and both subtitles (at the end of the file if the section doesn't exist). If the section already exists without `### Rules`, create that subtitle before `### Declined`. Decline lines go under `### Declined`. The labels in square brackets (like "[Number]") only say which version to pick: they are not saved.
6. **Never ask for a token, password or key in the chat**, and never run a command that shows one on screen. Box 7 teaches the person to save the token by themselves.
7. **Talk little between steps.** The full summary comes in the final box.
8. **When in doubt, stop and ask.** If something here doesn't match what you see on the person's computer (a tool with another name, an option that doesn't exist, an error), say what you found and ask. Don't make things up.
9. **Tool and option names change.** The ones named here are from November 2026. Look for them by name with ToolSearch; if you can't find one, say so and go on without that part.

**The three modes of the `Mode` question (Box 1, question 4).** They apply from Box 2 on:
- **Quick:** follow the "Recommended bundle (Quick mode)" section, which splits everything into three groups. (1) Show, in a single message, the three tables, summarized in plain words. (2) One AskUserQuestion call with two questions: header `Bundle`, options `Install group 1` / `See box by box` / `Cancel` (each with its consequence in one line, as in that section), and Box 2's `Long waits` question, unchanged, which decides the 1-hour cache. (3) On "Install group 1": do the boxes' steps only for the Group 1 parts, without more questions. (4) One call with the Group 2 questions (pick several). Install what is checked; what is left unchecked goes to "Declined". (5) Say in one line that Group 3 exists and is turned on later, through Box 7, box by box; it is not installed, not asked and does not go to "Declined". (6) Run Box 10 as it is and finish with the final box. "See box by box" switches to the second mode; "Cancel" stops without changing anything else (the Box 1 backup already exists).
- **Box by box:** one question box per tactic, in order, as described above. Save what the person accepts without asking again.
- **Box by box, checking:** like the one above and, before each write (a line in `settings.json`, a hook, a script copy, a rule in CLAUDE.md), show the exact piece and ask, with options `Write` / `Don't write`. "Don't write" is a decline of that part (it goes to "Declined").

**What counts as "sensitive"** (in both box-by-box modes, always asked one by one, with the risk block; in Quick mode, neither installed nor asked, because all of it is in Group 3): anything that changes permissions or the default permission mode; approves actions by itself (an approving hook, an allow rule); opens sessions by itself; turns on Remote Control; or saves a token. What this includes is marked "(sensitive)" in the boxes.

**How the questions depend on each other.** Before each box (and in the Group 2 box, in Quick mode), skip the questions whose condition doesn't hold; the condition is written next to the header, as "(only if ...)". Say in one line what you skipped and why (for example: "I skipped the spares because you didn't choose the automatic successor"). A skipped question counts as the answer that installs nothing and does not go to "Declined": if the person changes their mind, they just ask for the box again.

| If... | Skip | What the person loses |
|---|---|---|
| There is no Python (Box 1, step 3) | `Brake`, `Copy lock`, `Reminder`, `Token`, `Spare hook`, `Spend watch`, `Measure plan`, `Usage skill` | All scripts and hooks; only the text rules remain |
| `Where used` = "Terminal", or there is no `start_session` | In Box 7, everything except `Token` and `Permissions` | A successor visible in the app; Path B or the "[I open it]" rule remains |
| `Where used` = "Desktop app" or "Both" | `Token`, `Permissions` | Nothing: in the app, the token isn't needed |
| `Plan` = "API key" | `Before/after`, `Measure plan`, `Token` | Counting in % of the quota (that plan doesn't have it) |
| 200k window (or unknown) | `Compaction`; `Switching` uses ~100k | Nothing: lowering compaction only helps in the 1-million window |
| The person doesn't use agents | `Long waits` and Box 5 | Nothing now; if they start using agents, they can ask for both |
| `Handoff` = "No" | `Switching`, `Reminder` and all of Box 7 | The new session starts from scratch, so switching and the automatic successor lose their point |
| `Successor` isn't "Claude, on its own" | `Close old`, `Scheduled`, `Refused`, `Spares`, `Remote`, `Auto default`, `Spare hook` | The chain doesn't go on by itself; the switch depends on you |
| `Refused` isn't "Spare session" | `Spares`, `Spare hook` | A switch without you at the screen waits for your next message or uses the fallback |
| `Scheduled` = "Don't allow" | `Auto default` | The scheduled-task fallback |
| `Token` isn't "Yes, guide me" | `Permissions` | The screenless rounds |
| Quick mode | All of Box 7 (Group 3) | Nothing now: it is turned on later |

Combinations that only half work (when the person picks one, say in one line what they lose):
- Session switching without `Spend watch`: the switch depends on Claude noticing the conversation size; in the author's use, 14 of 36 switches went past the mark before the watch.
- `Long waits` "Yes" without agents that wait more than 5 minutes: each write costs 2 times and nothing is gained.
- "Experimental: Opus coordinates" without `Brake`: only the text rule keeps Sonnet from opening agents.
- `Close old` "No": the previous session may reread its conversation at every turn of the new one, spending quota, until it is archived.
- Spares without `Spare hook`: in auto mode, the switch through a spare may be blocked and fall back to "Notify and carry on".
- `Scheduled` allowed with `Auto default` "Don't change": the successor opened by the task stops at the first command, waiting for approval.
- "Notify and carry on" with `Remote` "Don't use": the warning only shows on the computer.
- `Copy lock` "No" with "Claude, on its own": when switching with an agent running, the successor checks the handoff instead of the lock guaranteeing it.
- `Measure plan` "No": the spend watch warns only in tokens, not in % of the quota.

**What is never skimped on** (always applies, no box): a backup before changing settings, confirmation before anything irreversible, building and testing what changed, and reading the exact piece of code that is about to be edited.

**Files in this package** (paths start from the folder where `START_HERE.md` is):
- `en/GUIDE.md` (this one) and `en/HANDOFF_TEMPLATE.md` (template for the handoff file) and `en/SUMMARIES_TEMPLATE.md` (template for the summaries file)
- `scripts/spend_watch.py` (spend watch), `scripts/agent_limit.py` (agent brake), `scripts/session_relay.py` (screenless rounds), `scripts/measure_point.py` (measure how much 1% of the plan is worth), `scripts/check_settings.py` (check `settings.json`), `scripts/spare_allow.py` (approves only the actions on spares), `scripts/copy_lock.py` (copy lock: keeps agents of two sessions off the same working copy), `scripts/handoff_reminder.py` (session-start reminder to read the handoff), `scripts/usage_report.py` (report of where the tokens went; only reads and prints)
- `skills/usage-report/SKILL.md` (skill that runs the usage report)
- `LICENSE.md`

**Config folder:** the folder named by the environment variable `CLAUDE_CONFIG_DIR`, if it is set (check: PowerShell `$env:CLAUDE_CONFIG_DIR`; Mac and Linux `echo $CLAUDE_CONFIG_DIR`). If it isn't, it is the `.claude` folder inside the user's home folder (Windows: `C:\Users\<name>\.claude`; Mac: `/Users/<name>/.claude`; Linux: `/home/<name>/.claude`). In this guide, "config folder" and `<config folder>` always mean this folder. In hook commands and in rules, use the full path with `/` slashes, on Windows too. Before copying the first file into `hooks`, `tools` or `templates` inside it, create the subfolder if it doesn't exist. The scripts `check_settings.py` and `measure_point.py` already read `CLAUDE_CONFIG_DIR` by themselves.

**Context window** (how many tokens fit in a conversation: 200k or 1 million): in the app, the context indicator next to the message box; in the terminal, the `/context` command. If you can't see it (no indicator, no command), assume 200k. It is the safe default: limits made for 200k also work in the 1-million window, and the reverse is not true. Tell the person how to check (the indicator or `/context` shows something like "x / 200k" or "x / 1M"). If they say it is 1 million, redo only the answers that depend on it (Boxes 2, 6 and 8).

**How to edit `settings.json` without breaking it:** read the whole file, add without deleting what is already there (inside `"env"` and `"hooks"`, which may already have items), and at the end check that it is still valid:

```text
python <package folder>/scripts/check_settings.py
```

The script accepts a file with a BOM, warns if a key appears twice (two `"hooks"` or two `"env"`, for example) and prints `ok` when everything is fine.

On Mac and Linux, replace `python` with `python3` here and in the hook commands.

## Why it works

Explain this to the person in up to 3 sentences before Box 1.

At every step (each time Claude uses a tool and reads the result), it rereads the whole conversation. Almost all of the cost comes from this rereading, not from writing or thinking. What saves tokens is: a short conversation, fewer steps in the main conversation, and heavy work outside it (in an agent, which has its own conversation, or in a script, which costs no tokens).

The author's numbers (September to November 2026, measured in the session records; source: measured on the author's machine, your results may differ):
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

- **Token:** a piece of text, roughly one word. It is the unit Claude reads, writes and is billed in.
- **Conversation (or context):** everything that has been said and read in the session. Claude rereads it at every step.
- **Agent:** a helper that Claude opens for one task. It has its own conversation, which starts empty, and it returns only a summary.
- **Haiku, Sonnet, Opus:** the three Claude models. Haiku is the cheapest and fastest; Sonnet is in the middle; Opus is the strongest and the most expensive.
- **CLAUDE.md:** a file of rules that Claude reads at the start of every session.
- **Hook:** a small script that Claude Code runs by itself at a fixed moment (for example, at every message or before opening an agent).
- **Cache:** the conversation stored so it can be reread more cheaply. It lasts 5 minutes by default; after that, storing it again costs again.
- **`/clear` and `/compact`:** `/clear` erases the conversation; `/compact` replaces the conversation with a summary. Only the person can type them.

---

## General risks and undoing everything

Tell the person this, briefly, before Box 1. Each box carries its own risks; this is what holds for the whole bundle.

- **What the bundle changes:** CLAUDE.md (a "Quota Keeper" section), `settings.json` (variables in `"env"`, hooks and, only in Box 7, permissions) and scripts, templates and one skill copied into the config folder. Nothing else, and only what the person accepts.
- **Network:** no script in the bundle makes a network call. `copy_lock.py` only runs `ps` (Mac and Linux) and itself. `session_relay.py` runs the `claude` command (which, like all Claude use, sends the conversation to Anthropic) and, on Windows, `taskkill` only on the process it opened itself.
- **Permissions:** a hook runs with the user's permissions, like any program of theirs. Nothing here bypasses Claude Code's approvals, except what each box marked "(sensitive)" says in plain words. Otherwise Claude keeps asking for approval as before.
- **If Python is missing or a hook errors:** Claude Code shows the error and goes on. A hook blocks an action only when it exits with code 2 (at session start, not even that: it only shows the error) or when it answers "deny" on purpose, as this bundle's brake and lock do, with a message. An error with any other code doesn't block: the action goes on. Python missing = the script-based parts don't work, nothing else breaks. (Check the Claude Code hooks documentation in case the person's version changed this.)
- **Can it cost more?** Some tactics can cost MORE in some uses: the 1-hour cache (writing costs 2 times), new sessions (they reread everything they load at the start) and spares (reserve sessions, which spend one short turn when created and then stay archived). Each box says when.
- **Undo everything:** (1) put the Box 1 backups (`settings.json.before-quota-keeper-<date>` and `CLAUDE.md.before-quota-keeper-<date>`) back over the current files, or (2) delete the "Quota Keeper" section from CLAUDE.md, remove from `settings.json` the `"env"`, `"hooks"` and `"permissions"` lines the bundle added, and delete what was copied into the config folder (the scripts in `hooks` and `tools`, the templates in `templates`, the `skills/usage-report` folder and, if they exist, `spares.txt` and `relay_token.txt`). Applies from the next session.

---

## Recommended bundle (Quick mode)

What Quick mode shows before installing, in three groups. Paths are in the config folder; "rule" is a line in CLAUDE.md. Everything applies from the next session. Each part's steps are those of its box, with the "(Recommended)" answer unless this section says otherwise.

**Group 1 — Adopt (installed with one OK).** Only rules, two file templates and `"env"` settings. Nothing approves, blocks or changes permissions.

| Part (box) | What it installs | Risk | How to undo |
|---|---|---|---|
| Lean CLAUDE.md and short memory (3: `CLAUDE.md`, `Memory`) | Rules; Claude proposes cuts and moves only with a yes | A moved detail may be missed (a pointer stays) | Delete the lines; put the moved text back |
| Short chat, long text in a file (3: `Chat style`, `Long text`) | Rules | You see less detail along the way | Delete the lines |
| Reading habits (4: all four) | Rules | May miss what was outside the piece read | Delete the lines |
| Agents on Sonnet (2: `Agents`) | `CLAUDE_CODE_SUBAGENT_MODEL` | Sonnet errs more than Opus on hard tasks; Claude asks for Opus there | Delete the line in `"env"` |
| Right model per task, short and batched agents (5: `Short agent`, `Models` "By role", `Batching`) | Rules | More agents per task; Haiku errs more on what looked simple | Delete the lines |
| High effort (2: `Effort`) | Rule | Nothing relevant: the effort selector stays with you | Delete the line |
| 1-hour cache (2: `Long waits`), only if the person answers that agents wait more than 5 minutes | `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` | Writing costs 2 times; without long waits, it costs more | Delete the line in `"env"` |
| Handoff and summaries, session switch, one task per session (6: `Handoff`, `Switching`, `One task`) | Rules and the two templates in `templates/`; switch at ~250k (~100k with the 200k window) | New files in projects, created without asking; a stale handoff sends the new session to the wrong spot | Delete the lines and templates; files already created stay until you delete them |
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
| Spend watch (8: `Spend watch`, author's limits) | `hooks/spend_watch.py` under `"UserPromptSubmit"` and `"PostToolUse"`, and a rule | Reads the local conversation records (counts only); one warning line when a limit is crossed | Remove both entries from `settings.json`; delete the script and the rule |
| Agent brake (5: `Brake`) | `hooks/agent_limit.py` under `"PreToolUse"` | May deny an agent you wanted (the message says why) | Remove the entry; delete the script |
| Copy lock (5: `Copy lock`) | `hooks/copy_lock.py` under `"PreToolUse"` and `"SubagentStop"` | A stuck lock keeps another session from writing in that folder for up to 2 hours | Remove the entries; delete the script; `copy_lock.py release <folder>` frees it now |
| Handoff reminder (6: `Reminder`) | `hooks/handoff_reminder.py` under `"SessionStart"` | One more line at session start in folders with a handoff | Remove the entry; delete the script |
| Compact at 50% (2: `Compaction`), only with the 1-million window | `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | The automatic summary loses detail | Delete the line in `"env"` |
| Usage report (8: `Usage skill`) | `skills/usage-report/`, `tools/usage_report.py` and `tools/measure_point.py` | Reads the local records (counts only); nothing leaves the computer | Delete the skill folder and both scripts |
| Measure the plan (8: `Measure plan`), only with a weekly % limit | `tools/measure_point.py`, a rule and the first mark | It is an estimate; needs the % on two different days | Delete the line, the script and `tools/measure_marks.csv` |

How to ask (one call, `multiSelect: true` on both questions, each option with the table's risk in one line):
- **Which of these hooks should we try?** — header `Hooks` — options `Spend watch` / `Agent brake` / `Copy lock` / `Handoff reminder`.
- **And these?** — header `Others` — options `Compact at 50%` (drop it with the 200k window) / `Usage report` / `Measure the plan` (drop it with "API key"). If only one option is left, ask it without `multiSelect`, with `Yes` / `No`.
- Without Python, drop every option except `Compact at 50%` (the `Hooks` question is not asked) and say so in one line.

**Group 3 — Advanced, not at the start (Quick mode neither installs nor asks).** All of it is Box 7. Say it exists and is turned on later, through Box 7, box by box (just ask "run Box 7 of the Quota Keeper guide"), ideally after a week or two with the rest.

| Part (Box 7) | What it would install | Why it waits | How to undo, if turned on |
|---|---|---|---|
| Automatic succession with archiving of the previous session (`Successor`, `Close old`, `Refused`, `Spares`) | Rules that open the new session and spares by themselves and archive the previous one | Opens sessions without you looking and archives the previous one; each new session reloads instructions and the handoff, so it can cost more. Only pays off once the handoff already works well | Delete the lines; unarchive from the archived list |
| Long-lived token in a file (`Token`, `Permissions`) | `relay_token.txt` | A key to your account, valid for a year, in a file: whoever gets it (a program, an admin, a cloud backup) spends your quota, and revoking just that key is not simple. Only useful if you use only the terminal | Delete the file; revoke as Box 7 says |
| Screenless rounds (Path B) | `tools/session_relay.py` and a rule | Claude works hidden and nobody approves anything: what is on the list goes straight through, and a mistake can edit files without you seeing | Delete the script and the rule |
| Automatic Remote Control (`Remote`) | Rule that turns Remote Control on in successors | Whoever gets into your claude.ai account, or picks up your unlocked phone, can send orders to the computer | Delete the line; turn it off in each session and in the app |
| Automatic approval: spare hook, allow rules, auto mode as default (`Spare hook`, `Scheduled`, `Auto default`) | `hooks/spare_allow.py`; lines in `"permissions"` | Actions go through without you seeing. The allow rules and auto mode apply to all sessions and projects, and auto mode's filter can be wrong both ways | Remove the lines from `settings.json`; delete the script |

---

## Box 1 — Before you start

**What this does:** decide where the rules go, how the person uses Claude Code and how the setup goes on. Nothing changes yet.
**Real risks:** none in this box: it only keeps answers. The change comes in the steps (backup and the CLAUDE.md section).
**How to undo:** nothing to undo before the steps; afterwards, see "General risks and undoing everything".

Questions:

1. **Where should the rules you accept be saved?** — header `Save rules`
   - **In all projects (Recommended)** — They go to the `CLAUDE.md` of Claude Code's config folder (usually `~/.claude/CLAUDE.md`) and apply in any folder, in every session (every line is always read).
   - **Only in this project** — They go to the `CLAUDE.md` of the folder that is open now. This applies only to the rule lines; if the file is shared, others will see them.
2. **Where do you use Claude Code?** — header `Where used`
   - **Desktop app** — The Claude app on the computer, in the Code tab. Unlocks the parts that use the app's tools.
   - **Terminal** — The `claude` command in a terminal window or inside the code editor. The app-only parts will be skipped.
   - **Both** — Offers the parts of both; nothing is installed unless you accept.
3. **How do you pay for Claude?** — header `Plan`
   - **Pro, Max or Ultra** — Personal subscription, with a weekly usage limit; the parts that measure the quota in % are available.
   - **Team or Enterprise** — Company plan; the limits may be set by the company, so the quota-measuring parts are only suggestions.
   - **API key** — Pay per use (per token), no weekly limit in %; the parts that measure the quota in % are skipped.
   - **I don't know** — That's fine: the guide stays general and says, in each box, what depends on the plan.
4. **How should I install what you accept?** — header `Mode`
   - **Quick (Recommended)** — One screen with the recommended bundle, the risk of each part and how to undo it. One ok installs the basics (rules and settings that don't touch permissions); you check the hooks in a single box; the advanced part (sessions opened by themselves, automatic approval, token) is not installed now.
   - **Box by box** — One question box per tactic, with the risks of each. I save what you accept without asking again.
   - **Box by box, checking** — Like the previous one and, before each write (settings.json, hook, rule), I show the exact lines and wait for your ok. Maximum control, more clicks.

Don't put "(Recommended)" on any option in question 3: it is a fact about the person, not a choice. Question 4 is about how to run the setup: see "The three modes of the `Mode` question" at the start of the guide.

Steps:
1. Make a backup, with the date in the name, of each file that exists: `<config folder>/settings.json` → `settings.json.before-quota-keeper-<YYYY-MM-DD>`, and the chosen CLAUDE.md → `CLAUDE.md.before-quota-keeper-<YYYY-MM-DD>`. The date is today's, from the computer's clock (for example `2026-11-04`). Each backup stays in the same folder as the original, next to it. Tell the person where they are.
2. At the end of the chosen CLAUDE.md (create it if it doesn't exist), add the section below. The next boxes put rule lines under "Rules" and declines under "Declined".

   ```markdown
   ## Quota Keeper (tactics by Jaber Felippe Neto, JN Softworks)

   ### Rules

   ### Declined (don't offer again)
   ```

   If the answer was "Only in this project" and that CLAUDE.md is shared with other people (in a repository, for example), warn them before saving.

   Settings, hooks and scripts always belong to the whole user (`<config folder>/settings.json`), even with "Only in this project": that answer applies only to the rule lines. Tell the person this.

   If the "Quota Keeper" section (or "Token saving", its old name) already exists (the guide was run before), update the existing one, never create another. The same goes for the settings and hooks in the next boxes: if they are already in `settings.json`, update them, never duplicate.
3. Check that Python 3 is installed (`python --version` or `python3 --version`). The scripts in Boxes 5, 6, 7 and 8 need it. If it isn't, warn that those parts will need Python (https://www.python.org/downloads/) and go on with the rest.
4. Keep the answer to "Where used": Box 7 depends on it.
5. Keep the answer to "Mode": it decides how Boxes 2 onward go (rules of the three modes, at the start of the guide). With "Quick", after the steps of this box follow the Quick mode script (the "Recommended bundle (Quick mode)" tables, the `Bundle` question, the Group 2 box) instead of opening Box 2. With the other two, go box by box.
6. Keep the answer to "Plan": Boxes 7 and 8 depend on it. Never assume the plan, not even from what a tool shows. With "I don't know", speak in general terms ("if your plan has a weekly limit in %...") and let the person decide. If they want to find out, show what the usage screen says (in the app, the `get_usage` tool; in the terminal, `/usage`) and ask them to confirm; without their confirmation, it stays "I don't know".

**Declines, in all boxes:** every tactic answered "No" (or unchecked) becomes a line under "Declined", with its name, so that no session asks again.

---

## Box 2 — Settings

**What this does:** three adjustments in `<config folder>/settings.json` and one effort rule.
**Why:** agents on a cheaper model; an agent that waits doesn't pay for the whole conversation again; the conversation summarized before every step gets expensive.
**Real risks:**
- Sonnet for agents: an agent may get a hard task wrong more often than Opus; Claude asks for Opus for delicate cases.
- 1-hour cache: writing costs 2 times (not 1.25); if the agent doesn't wait more than 5 minutes, you pay more, not less.
- Compacting at 50% or 25%: the automatic summary loses some detail of the conversation.
- Nothing here approves an action or changes a permission; no data leaves the computer because of these settings.
**How to undo:** delete the matching line in `"env"` of `settings.json` (or restore the Box 1 backup) and, for the effort rule, delete its line from CLAUDE.md. Applies from the next session.
**Note:** the numbers in this box (compact at 50%) assume the 1-million-token window. Check the person's window (rule "Context window", at the start of the guide; if you can't see it, assume 200k). If it is 200k, don't lower the compaction: skip question 3 and leave the default.

Questions:

1. **Should agents start on Sonnet?** — header `Agents`
   - **Yes (Recommended)** — Every agent starts on Sonnet, which is cheaper than Opus. When needed, Claude asks for Opus or Haiku for a specific agent.
   - **No** — Agents use the same model as the conversation; nothing changes, and agents may cost more if the conversation is on Opus.
2. **Do your agents often wait more than 5 minutes for something (builds, tests, downloads, renders)?** — header `Long waits` (only if the person uses agents)
   - **Yes, 1-hour cache** — An agent that waits doesn't pay for the whole conversation again when it comes back. Risk: each write costs 2 times (instead of 1.25), so it only pays off with agents that wait more than 5 minutes; on the author's machine those waits were ~26% of the cost (measured Sep-Nov 2026; your results may differ). Without long waits, it costs more.
   - **No, leave as is** — Nothing changes: the default 5-minute cache is enough for quick tasks.
3. **When should the conversation be summarized automatically?** — header `Compaction` (only with the 1-million window)
   - **At 50% (Recommended)** — The conversation is summarized when it reaches half of the space, before every step gets expensive; the summary loses some detail.
   - **At 25%** — For long production in a single session. It summarizes more often and loses more detail.
   - **Leave it** — Nothing changes: stays at the default, near the end of the space (steps get more expensive before the summary).
4. **Make a rule: High effort, no agent-fleet mode?** — header `Effort`
   - **Yes (Recommended)** — Claude recommends High effort; Max only for a very hard problem; no mode that opens many agents at once unless you ask. It is only a rule: you change the effort itself in the selector.
   - **No** — Nothing changes; Claude won't have this guidance and may suggest more expensive effort or modes.

Steps (each one only if the answer asked for it):
1. In `settings.json`, inside `"env"` (create it if it doesn't exist), add without deleting what is already there:
   - question 1 "Yes": `"CLAUDE_CODE_SUBAGENT_MODEL": "sonnet"`. Tell the person: in old versions of Claude Code, this setting overrode the model requested for a specific agent. If an agent requested on Opus or Haiku doesn't change model, update Claude Code (`claude update`).
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
3. Tell the person: the settings apply from the next session; to undo, delete the line (or restore the backup from Box 1). Only they can change the conversation's effort, in the effort selector of the app or the terminal.

Rule text:
> - Effort: recommend High; Max only for a very hard problem (preferably in an agent with max effort, not in the whole conversation). Never open an agent-fleet mode unless the person asks.

Check: `settings.json` is still valid (command at the start of the guide). Show the person only the new lines.

---

## Box 3 — What Claude reads every time

**What this does:** CLAUDE.md and the memory index come into every session before the first message and are reread at every step. Every line in them is paid for many times a day. The way of talking comes with it: writing costs 5 times more than reading, and everything written stays in the conversation. Only rules (text) are saved here; no script and no permission.
**Real risks:**
- Moving parts of CLAUDE.md to another file: Claude may stop seeing the detail if it doesn't open the file. That's why nothing moves without your yes, and a pointer stays in place.
- Shortening memory lines can erase a useful detail; only with your yes, and the Box 1 backup covers CLAUDE.md (not memory: ask for a copy if it matters).
- Short messages in the middle of the work: you follow less of what Claude is doing.
**How to undo:** delete the rule's line in CLAUDE.md (Quota Keeper section). Moved text: put the piece back where the pointer is. Applies from the next session.

Questions:

1. **Keep CLAUDE.md short (rules and pointers; details go to other files)?** — header `CLAUDE.md`
   - **Yes, and suggest cuts (Recommended)** — It becomes a rule, and Claude proposes now what to move to another file. Nothing leaves without your yes.
   - **Rule only** — Applies from now on; the current file stays as it is.
   - **No** — Nothing changes; CLAUDE.md may keep growing and costing more in every session.
2. **Memory with a short index (one line per note; a big project gets a summary note)?** — header `Memory`
   - **Yes (Recommended)** — The index is read in every session, and only up to a certain size. A short line fits more and costs less; shortening existing lines only with your yes.
   - **I don't use memory** — Nothing to do; this part is skipped.
   - **No** — Nothing changes; a long index is cut after line 200 and costs in every session.
3. **Short messages in the middle of the work, everything together at the end?** — header `Chat style`
   - **Yes (Recommended)** — Between steps, just one line about what it is doing. Answers, results and warnings come together in the final message.
   - **No** — Nothing changes; you see more detail along the way, and the conversation grows faster (costs more).
4. **Long things go to a file, not to the chat?** — header `Long text`
   - **Yes (Recommended)** — To show a big text or log, you save it in a file in the folder and give the name; Claude reads only the part it needs. It's one extra step for you.
   - **No** — Nothing changes; pasting big text in the chat is handier, but it costs at every following step.

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

**What this does:** everything Claude reads stays in the conversation and is reread at every following step. Only rules (text) about how to read are saved here; no script and no permission.
**Why:** a 50k-token file read at the start costs ~5k of weight at every step after that; over 100 steps, ~560k (computed with the guide's yardstick, not an official price). Read by an agent, it never enters the main conversation.
**Real risks:**
- Search instead of reading: Claude may miss context that was outside the part it read.
- An agent reading in its place: the summary may leave something out; the agent itself costs a new conversation.
- A note extracted once may go stale if the source changes.
**How to undo:** delete the rule's line in CLAUDE.md (Quota Keeper section). Applies from the next session.

Question (just one, with several answers: `multiSelect: true`):

1. **Which of these reading habits become rules?** — header `Reading`
   - **Search instead of reading** — Look for the name or title and read only about 50 lines around it. Never read a big document, a log or a generated file in full. Risk: it may miss what was outside the part.
   - **Big reads go to agents** — An agent reads and returns only the summary; the volume doesn't enter the conversation. Haiku to find and filter; Sonnet to understand. Risk: the summary may leave something out.
   - **Extract once** — When several tasks use the same big source, an agent writes a short note with what matters, and the next ones read the note. Risk: the note may go stale.
   - **Filter logs at source** — Mark the log's own lines and search only for the mark; never load a whole build or test log. Risk: an error without a mark doesn't show up.

If the person checks none: nothing changes; everything is still read in full, and costs more at every step.

Steps: save one line per checked item; the unchecked ones go to "Declined".

Rule text:
> - Search before reading: look for the name and read only the part around it; big documents, logs and generated files are never read in full.
> - Big reads (logs, several files, long documents) go to an agent that returns only the summary (Haiku to find, filter and count; Sonnet to understand). Read in full only what I am going to edit.
> - Big source used by several tasks: extract once into a short note in the project and reuse the note.
> - Logs: mark my own lines and search for the mark; never load a whole build or test log.

---

## Box 5 — Agents

**What this does:** an agent is born with an empty conversation, so each of its steps is cheap at the start. But it also rereads its own conversation at every step, and it gets expensive if it works for a long time. This box limits how long each agent works, picks the model for each kind of work and, with two optional scripts, brakes chains of agents and protects a folder from two sessions at once.
**Why:** in the author's use, agents with 100 or more calls were 74% of the agents' cost, and 71% of that cost came from steps where the agent's conversation was above 200k tokens (measured on the author's machine, Sep-Nov 2026; your results may differ).
**Real risks:**
- Agent rules (questions 1 to 3) are only text in CLAUDE.md: they block nothing, they only guide Claude. Small risk: an agent stopped at ~100 calls may leave the task half done, and opening the next one costs one more read of the resume file.
- The brake (question 4) and the lock (question 5) are Python scripts that Claude Code runs before each tool use. They can only DENY an action, never approve anything: they skip no permission prompt. The brake denies opening an agent (level 2 or more than 6 children); the lock denies writing, running a command that writes, or opening an agent in a folder that an agent of ANOTHER session is using.
- If the script fails on its own error, it lets everything pass (the protection disappears, nothing gets stuck). If Python doesn't exist or the path is wrong, Claude Code shows the hook error and carries on; the work isn't blocked either (but check that `python` opens in the person's terminal; on Windows it may be `py`).
- Both read internal files of Claude Code (the conversation's list of agents) that may change in an update; in that case they stop protecting, without blocking anything by mistake.
- The lock writes small files in `<config folder>/locks` and a log in `<config folder>/hooks/copy_lock.log`. A lock stuck by mistake keeps another session from writing in that folder until released (it goes away by itself after 2 hours, or when the owner Claude closes). No script uses the network.
- "Opus coordinates" (question 2) uses more steps and more agents; it is not a proven saving: on the author's machine it is still being tested.
**How to undo:** delete this box's lines from CLAUDE.md (takes effect next session). For the brake and the lock: delete the entry that calls `agent_limit.py` / `copy_lock.py` under `"PreToolUse"` (and the `copy_lock.py` one under `"SubagentStop"`) in `settings.json`, or restore the backup from Box 1; then delete the files in `hooks/`. Stuck lock right now: `python <config folder>/hooks/copy_lock.py release <folder>`. See the locks: `... copy_lock.py list`.

Questions (there are 5; the question box takes 4 per call: ask in 2 calls, 1 to 3 and then 4 and 5):

1. **Short agents: stop at ~100 calls and hand over?** — header `Short agent`
   - **Yes, at ~100 (Recommended)** — The agent finishes the item, writes where it stopped in a file and returns the summary. If work is left, the main conversation opens another agent from that file. Risk: the work may be split across more agents.
   - **No** — Nothing changes; agents keep going with no size limit and can get expensive if they run long.
2. **Which model for each kind of work?** — header `Models`
   - **By role (Recommended)** — Sonnet by default; Haiku for the mechanical (finding a file, filtering a log, counting); Opus only for delicate code (security, accounts, money, cryptography). Risk: Haiku errs more on a task that looked simple.
   - **Experimental: Opus coordinates** — Opus coordinates, Sonnet executes: a strong agent (Opus) writes the request for each piece and opens Sonnet agents one at a time; Sonnet opens no agents. Opus runs the tests by script, reviews only what changed and fixes it; a piece that fails twice, Opus does itself. Risk: more steps and more agents; not a proven saving (being tested on the author's machine).
   - **Don't change** — Nothing changes; you keep choosing each agent's model by hand.
3. **Agents in batches and with short answers?** — header `Batching`
   - **Yes (Recommended)** — One agent per task (not one per tiny piece); several launched in the same message; each one writes the detail in a file and returns 5 to 10 lines. Risk: the short answer hides detail (it is in the file).
   - **No** — Nothing changes; agents return long answers, which the main conversation rereads at every step.
4. **Install the agent brake?** — header `Brake` (only with Python)
   - **Yes (Recommended)** — A script stops an agent opened by another agent from opening more agents, and limits each agent to 6 children. It prevents endless chains. Risk: it may deny an agent you wanted; the message says why.
   - **No** — Nothing changes; endless chains of agents stay possible.
5. **Install the copy lock?** — header `Copy lock` (only with Python)
   - **Yes (Recommended)** — When an agent writes in a working copy (a folder with `.git`, `.p4config` or a `.uproject`), its session takes that folder. Another session can't write there or launch an agent on it until those agents finish. Reading, and editing `.md` and `.txt` notes, always pass. It matters when two sessions may work in the same folder, for example after a session switch with an agent still running. Risk: a stuck lock blocks the other session until released (2 hours, or `release`).
   - **No** — Nothing changes; two sessions can touch the same folder at the same time and get in each other's way.

Steps:
1. Questions 1 to 3: save the accepted rules. For question 2, save the "By role" rule or the "Experimental" one (not both). The "[Only with 1-hour cache]" line goes in only if Box 2, question 2, was "Yes, 1-hour cache".
2. "Experimental": create `~/Documents/opus_sonnet_pilot.md` (not in the config folder, which is protected: writing there asks for permission) with a table (date, task, passed first time?, what Opus had to redo). The rule says to note each case and, after ~6, to ask the person whether it becomes the default. It works best with the brake (question 4), which stops the Sonnet agent from opening others.
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
   3. Tell the person: the brake reads an internal file of Claude Code, which may change in an update. If it changes, the brake stops braking, but it never blocks anything it shouldn't.
   4. Check. Some versions only read the hooks when the session opens, and Claude can't open a new session by itself at this point. So: try in this session; if the block doesn't come, ask the person to open a new session (in the app, a new session in the same folder; in the terminal, quit and run `claude` again) and paste the request below into it. If they prefer, leave the test for the final box. The test uses three agents: the conversation opens A; A opens B; B tries to open C and must be blocked; A returns the message that B received. Make the request: *"Brake test. Open a Haiku agent, A, and ask it: 'open an agent B and ask B: open an agent C that answers hi; if B is blocked, return the blocking message. Then return to me the message that B received.' Return what A answered."* The expected result is the message "Agent limit: ...". If agent A or B says it doesn't have the tool to open agents, the brake isn't needed in this version: tell the person and go on.
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

   3. Tell the person: only agents take the lock (the main conversation's own edits don't), and agents of the same session share it. It goes away when the last agent of that session returns with nothing running in the background, when the owner session is closed or archived (its Claude process ends), or after 2 hours with no sign of its agents. To see the locks: `python <config folder>/hooks/copy_lock.py list`; to release one, only when sure the agent finished: `python <config folder>/hooks/copy_lock.py release <folder>`. It reads fields that Claude Code sends to hooks and internal files of Claude Code, which may change in an update; on any error it lets everything pass. No rule goes into CLAUDE.md: the block message itself says what to do.
   4. Check: `python <config folder>/hooks/copy_lock.py test` runs 17 simulated cases in a temporary folder, without touching real locks; the last line must be `ALL OK`. Then check `settings.json` with `check_settings.py`.

Rule text:
> - Agent that edits or fixes: its request says "when you reach ~100 calls, finish the item, write the resume point in <file> and return the summary". If work is left, the main conversation opens another agent from that file. A big task is born already split into agents of ~100 calls.
> - **[Only with 1-hour cache]** An agent doesn't stay more than ~50 minutes in a single wait; a longer wait = write the resume point and return.
> - Models by role: Sonnet by default; Haiku for the mechanical (finding a file, filtering a log, counting); Opus only for an agent that edits delicate code (security, accounts, money, cryptography).
> - (Experimental) New code or a fix outside security, accounts and cryptography: an Opus agent coordinates. It writes the request for each piece, opens Sonnet agents one at a time (~80 calls each; Sonnet opens no agents), runs the tests by script, reviews only what changed, fixes what is bad and returns a few lines. A piece that fails twice, Opus does itself. Note each case in `~/Documents/opus_sonnet_pilot.md`; after ~6 cases, ask the person whether it becomes the default.
> - Agents: one per task, not one per tiny piece; several at the same time go out in the SAME message; each one writes the detail in a file and returns 5 to 10 lines.

---

## Box 6 — Handoff and session switch

**What this does:** Claude keeps, in each project, a short handoff file (what was done, what is half done, the exact next step) and a summaries file (one entry per session, to find later who did what). It creates both by itself on the first multi-stage work, notes the steps when each part is finished and, when the conversation gets big or the stage changes, a new session starts from the handoff, with an empty conversation.
**Why:** it was the author's biggest saving: the main conversation fell 75% after this rule (measured on the author's machine, Sep-Nov 2026; your results may differ). The automatic summary (compaction) loses detail; the file doesn't.
**Real risks:**
- The files live in the project folder, as plain text: nothing leaves the computer because of them. But if the folder is published (repository, cloud), the handoff goes with it; don't write passwords, tokens or personal data in it. Tell the person this.
- Claude will create and rewrite `HANDOFF.md`/`SUMMARIES.md` by itself, without asking each time: new files appear in projects (and in a repository, in `git status`). If you don't want them versioned, add them to `.gitignore`.
- An old or wrong handoff makes the new session start from the wrong point. Claude checks the "next step" before acting and asks for confirmation on irreversible actions, but the person should look at the file if the new session seems lost.
- Switching sessions costs one read of the handoff and loses what lived only in the conversation; a small price next to staying in a huge conversation.
- The session-start reminder (question 4) is a Python script with no network: it costs one line at the start of each session; if it fails, Claude Code shows the error and carries on.
**How to undo:** delete this box's lines from CLAUDE.md (takes effect next session); the `HANDOFF.md`/`SUMMARIES.md` files already created stay, delete them by hand if you want. Reminder: delete the `"SessionStart"` entry that calls `handoff_reminder.py` in `settings.json` (or restore the backup from Box 1) and the file in `hooks/`.
**Note:** the numbers in this box (switch at ~250k) assume the 1-million-token window. Check the person's window (rule "Context window", at the start of the guide; if you can't see it, assume 200k). If it is 200k, switch sessions at ~100k (tell the person this at question 2 and use `<100>` in the rule) and don't lower the compaction in Box 2.

Questions:

1. **Handoff and summaries in projects with work in progress?** — header `Handoff`
   - **Yes, handoff + summaries (Recommended)** — On a project's first multi-stage task, I create `HANDOFF.md` and `SUMMARIES.md` at the root by myself, from this guide's templates (if the project already has such a file, I use that one). I note the steps in the handoff when each part is finished and, at every session switch and end of stage, I append an entry to `SUMMARIES.md` (Did / Decided / Open). Risk: new files appear in projects, without asking each time.
   - **Handoff only** — I create and keep only `HANDOFF.md`; no summaries file. Fewer files, but later there is nowhere to find which session did something.
   - **No** — Nothing changes; a new session starts without a handoff file and loses what lived only in the conversation.
2. **When to switch sessions?** — header `Switching` (only if `Handoff` wasn't "No")
   - **~200k or new stage** — More switches, every step rereads less. A new stage always starts in a new session. Risk: more switches, each one loses a little of what the conversation knew.
   - **~250k or new stage (Recommended)** — In the author's numbers (260 sessions), the total cost barely changes between 200k and 300k, and 250k sits in the middle. Above ~300k, every step rereads so much that it costs more. A new stage always starts in a new session.
   - **~300k or new stage** — Fewer switches, every step more expensive. Worth it when the handoff loses a lot of what the conversation knew.
   - **Only when I ask** — Nothing switches by itself; I only warn in one line when the conversation passes ~250k. The conversation can get expensive if you forget.
3. **One task per session?** — header `One task`
   - **Yes (Recommended)** — A new subject, unrelated to what is open, goes to a new session (or `/clear`), not to the end of this conversation. Risk: more open sessions for you to keep track of.
   - **No** — Nothing changes; different subjects pile up in the same conversation, which gets big and expensive.
4. **A session-start reminder to read the handoff?** — header `Reminder` (only if `Handoff` wasn't "No"; with Python)
   - **Yes (Recommended)** — I install a script (`handoff_reminder.py`, session-start event) that, if the opened folder has a `PASSAGEM*.md` or `HANDOFF*.md`, shows Claude one line telling it to read that file first. It only lists the folder: it reads no file, writes nothing, uses no network. Cost: one extra line at the start of each session in those folders. If it fails (or Python doesn't exist), Claude Code shows the error and the session carries on normally.
   - **No** — Nothing changes; the CLAUDE.md rule already says to read the handoff, but without this reminder Claude may forget.

Steps:
1. Question 1 "Yes, handoff + summaries" or "Handoff only": copy `en/HANDOFF_TEMPLATE.md` to `<config folder>/templates/HANDOFF_TEMPLATE.md` (create `templates` if it doesn't exist). Only for "Yes, handoff + summaries": also copy `en/SUMMARIES_TEMPLATE.md` to `<config folder>/templates/SUMMARIES_TEMPLATE.md`. These are the templates: the session creates each project's `HANDOFF.md` (and `SUMMARIES.md`) from them. Save the rule of the chosen version.
2. Question 2: save the rule with the chosen number, or the "Only when I ask" rule. Tell the person where to see the conversation size: in the app, the context indicator next to the message box; in the terminal, the `/context` command.
3. Question 3: save the rule. Remind the person: only they can type `/clear` or `/compact`; Claude can't.
4. Question 4 "Yes":
   1. Copy `scripts/handoff_reminder.py` to `<config folder>/hooks/handoff_reminder.py`.
   2. In `settings.json`, inside `"hooks"`, add to `"SessionStart"` (create the list if it doesn't exist; don't delete what is already there):

      ```json
      "SessionStart": [
        {
          "hooks": [
            { "type": "command", "command": "python \"<config folder>/hooks/handoff_reminder.py\"", "timeout": 10 }
          ]
        }
      ]
      ```

   3. Tell the person: the script approves and blocks nothing, it only prints one line, and it only looks in the folder where the session opened. Check with `python <config folder>/hooks/handoff_reminder.py --test` (the last line must be `ALL OK`) and then with `check_settings.py`. The reminder shows up in the next session opened in a folder that has a handoff.
5. If there is a project with work in progress right now, offer to create its `HANDOFF.md` (and the `SUMMARIES.md` next to it, if question 1 was "Yes, handoff + summaries") (only with a yes).

Rule text (for the session switch, save one of the two versions):
> - Handoff: every project with work in progress has a handoff file (the one the project already has, or `HANDOFF.md` at the root, made from `<config folder>/templates/HANDOFF_TEMPLATE.md`). On the first multi-stage work in a project, create the file by yourself (and the summaries file, below). Rewrite, don't append to the end. Note in the handoff the steps done when each part is finished, before the session switch and when the spend watch warns. An unanswered question goes in the "Questions for the person" section. A new session starts by reading the handoff and does the "exact next step" without asking, except irreversible actions, which need confirmation. Never write passwords, tokens or personal data in the handoff.
> - **[Number]** Session switch: with the conversation at ~<250>k tokens, or at a new stage, finish the part in progress, update the handoff and switch sessions. If there is no successor rule, tell the person in one line what to paste into the new session.
> - **[Only when I ask]** Session switch only when the person asks; warn in one line when the conversation passes ~<250>k tokens.
> - One task per session: a new, unrelated subject goes to a new session.
> - **[Only with handoff + summaries]** Summaries: every project with a handoff file has a summaries file next to it (`HANDOFF.md` → `SUMMARIES.md`; `HANDOFF_X.md` → `SUMMARIES_X.md`; create it by yourself from `<config folder>/templates/SUMMARIES_TEMPLATE.md`). A mandatory step of EVERY session switch and every end of stage, without the person asking: when closing (before opening the successor or ending the stage), append ONE entry at the end: `## <n> — <session title> (<date>, <session id>)` with up to three short lines: **Did** (with the names someone would search for later: files, screens, tools), **Decided** (what was settled, and by whom), **Open** (what was left open or unanswered, or "nothing"). It doesn't reread the whole file, it only appends. Its only use is finding later which session did something.

---

## Box 7 — Automatic successor session (the most laborious)

**What this does:** at the moment of switching sessions (Box 6), instead of asking the person to open a new session, Claude itself opens the successor, which starts from the handoff. The successor can open the next one the same way: the chain goes on as long as there is work. Depending on the answers, the box writes rules in `CLAUDE.md` and may write to `settings.json` allow rules and auto mode as the default, install a hook (a program Claude Code runs before an action) that approves certain actions on its own in the "spares" (reserve sessions, stopped and archived), and store a token (access key) for screenless rounds. **This whole box is sensitive:** in Quick mode it is neither installed nor asked (Group 3 of the recommended bundle); whoever wants it runs this box later, box by box, and every part below becomes a question, with its own risk.
**Advanced:** recommended only after a week or two using the other tactics.
**Why:** without this, the switch depends on the person being there to look. The author had a stage stopped all night waiting for a click. And the previous session, if it stays connected to the new one, wakes up and rereads the whole conversation every time the new one finishes a turn.

**Real risks:**
- **It opens sessions on its own**, with the person not looking, and may leave spare sessions (spares) stopped in the folder. Each new session reloads the instructions and reads the handoff again, so it may use more quota than staying in one conversation; a spare uses one short turn when it is created. The author has no measured number for this.
- **Actions approved without the person seeing them (only if they accept each one):** the spares hook, the allow rules for the scheduled task and auto mode as the default. The allow rules and auto mode apply to ALL sessions and projects of this computer account, not only to the successor.
- **It archives sessions** (the previous one and used spares). Archiving doesn't delete: it can be undone.
- **Remote Control** links the session to the person's claude.ai account: whoever gets into it can send orders to the computer.
- **Token** (terminal users only): an account key stored in a file on the computer.
**How to undo** (applies from the next session; sessions already open keep what they read; you can also ask Claude to do any of this):
- `CLAUDE.md`: delete the lines that start with "Successor:", "Close the previous one:", "Notify and carry on:", "Spares:", "Switch with an agent running:", "Remote Control:", "Inheritance" and "Screenless rounds:".
- `settings.json` (or restore the Box 1 backup): remove from `"permissions"` → `"allow"` the two lines `"mcp__scheduled-tasks__create_scheduled_task"` and `"mcp__scheduled-tasks__run_scheduled_task"`; remove `"defaultMode": "auto"` from `"permissions"` (or put back the value the backup shows); remove from `"hooks"` → `"PreToolUse"` the block whose `matcher` is `SendMessage|mcp__ccd_session_mgmt__.*`; remove from `"permissions"` → `"deny"` the line `Read(.../relay_token.txt)` (optional: it is harmless).
- Files: delete `<config folder>/hooks/spare_allow.py`, `.../hooks/spare_allow.log`, `.../spares.txt`, `.../tools/session_relay.py`, `.../relay_token.txt` and, in each project, `SUCCESSOR.md` and `relay.log`.
- Sessions and task: the spares are the sessions titled "Spare <folder> N" in the app's archived list; leave them archived (archived costs nothing) or delete them (ask Claude: `list_sessions` and `delete_session`, if the tool exists, or use the session's menu). The scheduled task is "successor-<folder>": ask Claude for `list_scheduled_tasks` and `delete_scheduled_task`, or delete it in the app's Routines section. Careful: deleting a task archives the session it opened.
- Remote Control: turn it off in each session (`set_remote_control` with false, or the session's menu) and turn off, in the app settings, the option that turns it on in every new session.
- Token: delete the `relay_token.txt` file (Box 7, Path B, says how to revoke).

**Questions a skeptical reviewer would ask, with straight answers:**
- **Does `spare_allow.py` get around permissions?** It skips one thing only: the approval prompt (and the auto mode filter) for six tools, and only when the target is an id listed in `spares.txt`: `SendMessage` (message to the session) and, in the app, unarchive, change title, change model, change effort and turn Remote Control on or off. It doesn't read the message text. Everything else follows the normal flow and still asks for approval or goes through the filter: opening a session (`start_session`), archive, detach, delete, stop, changing another session's permission mode, and any action on a session that isn't on the list. Deny rules, according to the Claude Code documentation, still apply (the author didn't test this). Two caveats: a message to a spare is an order to another session, which then acts with its own permissions; and if the id stays in `spares.txt` after the spare became a working session, those six actions stay approved on it (Claude removes the id after using the spare; check the file now and then). Every decision goes to `hooks/spare_allow.log` (time, tool and id, no message text; the file isn't cleaned automatically).
- **What if the hook fails (Python missing, an error, going past 10 s)?** Nothing is approved: per the Claude Code documentation, a hook that fails neither blocks nor approves, and the action follows the normal flow (asks for approval or goes to the filter). Only convenience is lost: the spare may be blocked and the switch falls back to "Notify and carry on". The author didn't test it by removing Python.
- **Does auto mode (`"defaultMode": "auto"`) let Claude act without asking about what?** Instead of asking for your OK on each action, a filter judges each one: it lets through what looks safe and routine (reading and editing project files, common commands) and blocks what looks risky or beyond what you asked. It can be wrong both ways. It is not the mode that ignores all permissions (the guide doesn't use that one), and deny rules still apply. It applies to every new session the person opens, in any project.
- **Token in a file: who can read it, how to delete and revoke?** `relay_token.txt` sits in the config folder. On Windows the guide leaves only the person's user with access; on Mac and Linux, only the owner (mode 600). Even so, any program that runs as the person, computer administrators, and backups or cloud sync that take the folder can read it. Claude doesn't read it (a deny rule on reading, which covers the read tool but is no guarantee against a terminal command). To delete: delete the file. To revoke: the official documentation (checked in November 2026) doesn't show how to revoke just this token; look at the list of access and sessions in the account settings on claude.ai or contact Anthropic support. The token lasts one year.
- **Can this cost more?** Yes. Each new session (successor, spare, scheduled task) starts with an empty conversation but reloads instructions and memory and reads the handoff, and its first use doesn't benefit from what the previous one already had in cache. In exchange, it avoids the cost of continuing in a very large conversation. "Notify and carry on" and a conversation that goes past the limit with no reply cost the opposite: each step in a large conversation costs more. The screenless rounds use the same quota. No author number for the total.
- **Does data leave the computer?** The package's scripts make no network calls. What runs in Claude (including the screenless rounds, which call the `claude` command) sends the conversation to Anthropic, like any use of Claude. Remote Control shows the conversation in the person's claude.ai account and on their devices.

Prerequisite: Box 6, question 1 (`Handoff`), answered "Yes, handoff + summaries" or "Handoff only". Without a handoff file, skip this box. If this box is run later, in another session, first ask Box 1's `Where used` and `Plan` questions again and check in CLAUDE.md what Boxes 5 and 6 saved.

There are two paths. Explain both to the person before the box:
- **Path A, through the app (visible, no token):** in the desktop app, Claude has a tool to open another session. The successor appears in the sidebar like any session. It is the recommended one.
- **Path B, through the terminal (screenless, needs a token):** a script runs Claude through the terminal (`claude -p`) in rounds, each with an empty conversation, reading and updating the handoff. It doesn't appear in the app; the result stays in the files and in a log. It needs a long-lived access token. It is only for people who use only the terminal: in the app, spares, "notify and carry on" and the scheduled task cover the refusals without a token, so app users don't install the token.

**Before showing any question** (only if Box 1 answered "Desktop app" or "Both"): find the tools with ToolSearch, by name (list in step 1 of Path A), and check this session's permission mode (`get_session` with "self", field `permissionMode`). Then:
- If `start_session` exists: go on as below.
- If `start_session` doesn't exist: Path A isn't available in this version. Tell the person in one line and treat the case as "Terminal" (next item): don't ask questions 1, 2, 5, 6, 7, 8, 9 and 10, which depend on that tool. If they decline Path B ("Not now"), save only the "[I open it]" rule (the minimum rule: Claude updates the handoff and **tells the person to open the new session**), don't save the close-the-previous rule or the inheritance rule, put "Automatic successor session (no tool in the app)" under "Declined", and skip the Path A steps.

How to show the questions (there are ten, split into up to three AskUserQuestion calls, which accepts at most four questions at a time; conditional ones come only after the answer that unlocks them). Before each call, show in a few lines the "Real risks" and "How to undo" of its questions:
- If Box 1 answered "Terminal": don't ask questions 1, 2, 5, 6, 7, 8, 9 and 10, which depend on the app. Ask only 3 and, if the answer is "Yes, guide me", ask 4 in a second call. The successor in this case is the Path B rule; with "Not now", the "[I open it]" rule is used.
- If it answered "Desktop app" or "Both": don't ask questions 3 and 4 (the token isn't needed in the app; treat it as "Not now", without adding it to "Declined"). First call: question 1. Second call, only if 1 is "Claude, on its own": questions 2, 5, 6 and 8 (with the other answers to 1, Claude opens no session, so there is no previous one to close, no fallback and no successor Remote Control to decide). Third call, only with the answers to the second and only with the questions they unlock: 7 and 10 (if 6 is "Spare session") and 9 (if 5 is "Allow both rules"); if none is unlocked, there is no third call. With "Claude proposes, I click" or "I open it" in 1, only the first call happens. In the "[Claude, on its own]" rule, "If that also fails" becomes "warn the person in one line".

Question 3 and the plan (Box 1): with "API key", don't ask question 3 (the token exists only for subscriptions) and treat it as "Not now"; if Box 1 also answered "Terminal", the "[I open it]" rule is used. With "I don't know", ask it and say the token exists only on subscription plans (Pro, Max, Ultra, Team and Enterprise); if the token command refuses their account, treat it as "Not now".

In question 3 (only in the "Terminal" case), put "(Recommended)" on **"Yes, guide me"**.

In question 9, use the permission mode seen before the questions. If it is `auto` (auto mode), put "(Recommended)" on **"Yes, auto"**; otherwise, or if it couldn't be seen, on **"Don't change"**. Never set auto mode as the default without question 9 answered "Yes, auto".

1. **Who opens the successor session?** — header `Successor` (sensitive: opens sessions on its own; only in the app, with `start_session`)
   **Real risks:** the new session starts without you looking and may be hidden (see "Routines" in the traps); each new session reloads the instructions and reads the handoff again, which may use more quota than staying in one conversation; the chain only stops when the handoff says the stage is done or has a question for you. With the first option Claude also saves the "Switch with an agent running" rule.
   **How to undo:** delete from `CLAUDE.md` the lines "Successor:", "Switch with an agent running:" and "Inheritance"; archive in the sidebar the sessions it opened. Applies from the next session.
   - **Claude, on its own (Recommended)** — At the switch, Claude updates the handoff, opens the successor and stops. You just see the new session appear; nobody asks for your OK, and the chain goes on by itself until the handoff says it is done.
   - **Claude proposes, I click** — A card appears for you to start it. Nothing opens without your click; if you are not looking, the work stops until the click.
   - **I open it** — Claude updates the handoff and says what to paste into the new session. Nothing opens on its own; it is the safest option and more work for you.
2. **Does the successor close the previous one?** — header `Close old` (sensitive: archives sessions; only if `Successor` is "Claude, on its own")
   **Real risks:** archiving doesn't delete the conversation (it leaves the normal list and comes back from the archived list); if Claude got the id wrong it would archive the wrong session, which is why the id comes in the request ("Previous session: <id>") and the rule doesn't apply to a parallel session for another task. The successor also turns off the previous one's Remote Control and detaches from it. In the "Switch with an agent running" rule, the previous session archives itself when its last agent returns.
   **How to undo:** delete the "Close the previous one:" line from `CLAUDE.md`; to bring a session back, unarchive it from the archived list.
   - **Yes (Recommended)** — The successor detaches from the previous one and archives it, so the previous one doesn't wake up and reread everything at every turn of the new one. The title gets a number ("Site" → "Site 2" → "Site 3").
   - **No** — Nothing is archived on its own; both stay open and the previous one may reread the whole conversation at every turn of the new one (uses quota) until you archive it. In the "Switch with an agent running" rule, remove the part where the previous session archives itself.
3. **Install the token for screenless rounds (Path B)?** — header `Token` (sensitive: stores an account key in a file; only in the terminal, not with "API key", with Python)
   **Real risks:** the token is an access key to the person's Claude account, valid for one year: whoever has it uses their quota. It lives in `<config folder>/relay_token.txt`; the guide restricts the file to their user, but any program that runs as them, administrators, and backups or cloud sync that take the folder can read it. Claude never sees the token. The rounds run with nobody watching and use the same quota.
   **How to undo:** delete `relay_token.txt`, `tools/session_relay.py` and the "Screenless rounds:" rule; remove from `settings.json` the line `Read(.../relay_token.txt)` (optional). To revoke, see "Token in a file" above and the end of Path B.
   - **Yes, guide me** — You run a command, log in in the browser and save the token in a file. Claude never sees the token. It takes about 10 minutes.
   - **Not now** — Nothing is stored; only Path A stays, which needs the desktop app.
4. **What can the screenless rounds use?** — header `Permissions` (only if `Token` is "Yes, guide me")
   **Real risks:** no round asks for approval: what is on the list goes straight through and the rest is refused. Even with files only, a wrong round can edit or overwrite project files without you seeing (use git or a copy).
   - **Files only (Recommended)** — Read, search, create and edit files. No commands.
   - **Files + terminal** — Also runs commands (tests, builds). More useful and riskier: nobody is watching, and the round's terminal can also see the token.
   - **Decide per project** — Claude asks the first time in each project, and nothing runs without that yes.
5. **Allow the scheduled-task fallback?** — header `Scheduled` (sensitive: stores allow rules; only if `Successor` is "Claude, on its own")
   **Real risks:** adds two rules under `"permissions"` → `"allow"` in `settings.json`: create and run a scheduled task without asking for approval. They apply to ALL sessions and projects, not only the successor; a session misled by malicious text (on a page or in a file) could schedule something that runs later with nobody watching, in the default permission mode and under the deny rules. The task is only created at the first switch where spares and "Notify and carry on" are not enough.
   **How to undo:** remove from `"allow"` the lines `"mcp__scheduled-tasks__create_scheduled_task"` and `"mcp__scheduled-tasks__run_scheduled_task"`; delete the `successor-<folder>` task (see "How to undo" at the top of the box). Applies from the next session.
   - **Allow both rules (Recommended)** — Claude creates and runs the scheduled task without asking for approval, but only as a fallback. Without the rules, auto mode usually blocks the task.
   - **Don't allow** — Nothing is stored; when the app refuses to open the session, and spares and "Notify and carry on" are not enough, the fallback is Path B (if installed) or a warning to you.
6. **When the app refuses to open the successor?** — header `Refused` (sensitive: may create and reactivate sessions on its own; only if `Successor` is "Claude, on its own")
   **Real risks:** "Spare session" creates reserve sessions without you seeing them (see question 7) and later archives and reactivates them; "Notify and carry on" lets the conversation grow until your next message, and each step in a large conversation uses more quota; "Fallback right away" may leave the successor hidden in Routines.
   **How to undo:** delete from `CLAUDE.md` the lines "Spares:" and "Notify and carry on:"; delete the spares (see "How to undo" at the top of the box).
   - **Spare session (Recommended)** — On each message from you, Claude checks and refills a few stopped, archived sessions in the project folder (the "spares"; question 7 says how many). At the switch, it unarchives one, gives it the new title and sends the task by message: the successor starts right away, in the normal list, even with you away from the screen. With no spare in the folder, it falls back to "Notify and carry on".
   - **Notify and carry on** — Claude saves the handoff, sends a notification (on the computer and, with Remote Control on, on the phone) and keeps working in this session. On your next message, any message, it opens the successor in the normal list before anything else. The fallback (scheduled task, screenless rounds) is kept for when the conversation goes well past the limit with no reply from you. It creates no session before your message.
   - **Fallback right away** — Claude uses the fallback at once. The successor starts sooner but, if it comes from a scheduled task, it is hidden in the Routines section and can't open the next one on its own.
7. **How many spares per folder?** — header `Spares` (only if question 6 is "Spare session"; the box's "Other" option lets the person type another number)
   **Real risks:** Claude creates up to that number of empty sessions in the folder, without you seeing, and refills the used ones on each message from you. Each uses a short turn when created (it reloads the instructions and replies "ready"); archived, it costs nothing. They fill the archived list. The author has no measured number for the total cost.
   - **10 (Recommended)** — Covers a night with several switches, even with several sessions in the same folder sharing the spares. Creates up to 10 sessions at once on your first message after the install.
   - **6** — The minimum: enough if you have one or two sessions per folder; creates fewer sessions at once.
   - **16** — For when many sessions work in the same folder for a long time without you coming back to the computer; it creates the most sessions and uses the most short turns.
8. **Turn on Remote Control?** — header `Remote` (sensitive: desktop app only, Path A, and only if `Successor` is "Claude, on its own"). Show the risks below before asking.
   **What this does:** links the session to the person's claude.ai account, so they can follow it and send messages from their phone or a browser; it is what makes the "Notify and carry on" alert reach the phone.
   **Real risks:** anyone who gets into their claude.ai account, or picks up their unlocked phone, can send orders to the session, which runs on their computer with the session's permissions (files and commands); so, two-step verification on the account and a locked phone. The conversation also shows on those other devices. And a session open through Remote Control counts as "live work": the app won't archive it, which is why the successor turns the previous one's off before archiving.
   **How to undo:** delete the "Remote Control:" line from `CLAUDE.md`; turn it off in each session (`set_remote_control` with false, or the session's menu) and turn off, in the app settings, the option that turns it on in every new session. If you suspect unwanted access to the account, change the password and sign out of connected devices in the account settings.
   - **Successors only (Recommended)** — Claude turns Remote Control on in every successor it opens (normal list, spare or scheduled task), so you can follow the chain from afar. Other sessions stay as you leave them.
   - **Turn on now** — The same, and Claude also turns this session's on now; to have it on every new session, you turn on the app option that does that (in November 2026, "Connect new sessions to Remote Control", in the app's settings).
   - **Don't use** — Nothing is turned on: Claude never turns Remote Control on. It still turns off the previous session's before archiving it, if it is on. Without it, the "Notify and carry on" alert only shows on the computer.
9. **Start every session in auto mode?** — header `Auto default` (sensitive: changes the default permission mode; only if question 5 is "Allow both rules")
   **What this does:** stores `"defaultMode": "auto"` under `"permissions"` in the user's `settings.json`. Reason: a scheduled task doesn't inherit the mode of the session that created it; without this, the successor it opens stops at the first command, waiting for approval.
   **Real risks:** it applies to EVERY new session, in every project, not only the successor: instead of you approving each action, a filter decides (it lets through what looks safe and routine, blocks what looks risky) and can be wrong both ways. It doesn't ignore permissions, and deny rules still apply. It needs a recent Claude Code version and a plan with this mode; without them the session starts in normal mode.
   **How to undo:** remove `"defaultMode": "auto"` from `"permissions"` (or put back the value the Box 1 backup shows). Applies from the next session.
   - **Yes, auto** — Every new session starts in auto mode, including the successor the task opens. For people who already work in auto mode.
   - **Don't change** — The default mode stays as it is. The successor opened by the task starts in normal mode and stops at the first command or edit, waiting for you to approve. (The app says each routine keeps the approvals given during a run and that they apply to the next runs; not tested.)
10. **Install the hook that approves actions on spares?** — header `Spare hook` (sensitive: approves actions on its own; only if question 6 is "Spare session"; with Python)
   **What this does:** copies `scripts/spare_allow.py` to `<config folder>/hooks/`, creates an empty `spares.txt` and adds a block under `"hooks"` → `"PreToolUse"`.
   **Real risks:** it approves on its own only six actions (message, unarchive, title, model, effort and Remote Control) and only on a session whose id is in `spares.txt`; it doesn't read the message text; if it fails, it approves nothing. Details in the answer "Does `spare_allow.py` get around permissions?" at the top of the box. It logs everything in `hooks/spare_allow.log`, on your computer.
   **How to undo:** remove from `"hooks"` → `"PreToolUse"` the block with `matcher` `SendMessage|mcp__ccd_session_mgmt__.*` and delete `hooks/spare_allow.py`, `hooks/spare_allow.log` and `spares.txt`. Applies from the next session.
   - **Install the hook (Recommended)** — Switches through spares go through without an approval box; the six actions are approved only on the listed spares.
   - **Without the hook** — Nothing is approved on its own; auto mode may block changing a spare another session created, or the message with the task, and then the switch falls back to "Notify and carry on" or you approve in the box.

### Steps for Path A (desktop app)

Only if Box 1 answered "Desktop app" or "Both" and `start_session` exists. If it answered "Terminal", or the tool doesn't exist, go straight to Path B (or, without it, to the minimum rule above).

1. **Tools** (found before the questions, with ToolSearch, by name): `start_session` (open a session), `create_scheduled_task` and `list_scheduled_tasks` (create and list scheduled tasks), `run_scheduled_task` (run a task now), `set_session_title` (change a session's title), `detach_session`, `archive_session` and `unarchive_session` (detach, archive and unarchive), `list_sessions` and `get_session` (list and view sessions), `set_remote_control` (turn Remote Control on and off), `set_session_effort` and `set_session_model` (another session's effort and model), `list_task_runs` (sessions a task opened), `list_sections` (sidebar sections), `PushNotification` (a notification on the computer and, with Remote Control, on the phone) and `SendMessage` (a message to another session). In November 2026 they existed with these names in the desktop app. Before any `set_remote_control`, check `remoteControlState` with `get_session` and only call it if the state is different: an unneeded call may open an approval box or turn Remote Control off by mistake. Call `start_session` with initiation "user_asked" (the values "offer" and "own_initiative" become a card waiting for a click) and context "fresh" (empty conversation).
2. **Save the rules** from question 1 (one of the three versions below) and, if question 2 is "Yes", the close-the-previous one; if question 6 is "Notify and carry on", the notify-and-carry-on one; if it is "Spare session", the spares one (with the number from question 7) and also the notify-and-carry-on one, for when there is no spare (with "Fallback right away", nothing extra: the question 1 rule already uses the fallback). With "Claude, on its own" (question 1), also save the switch-with-an-agent-running rule. If question 8 is not "Don't use", save the Remote Control rule; if it is "Turn on now", turn this session's Remote Control on now (first look at `remoteControlState` with `get_session` and only call `set_remote_control` with "self" and true if it is off) and tell the person where the app option for new sessions is. Always save the inheritance rule. With question 2 "No", don't save the close-the-previous rule and, in the switch-with-an-agent-running rule, remove the part where the previous session archives itself. Explain to the person that the successor's request carries the current session's id ("Previous session: <id>"), found with `list_sessions` or `get_session`, so the successor knows which one to archive; with the manual-only task (step 4), the whole request goes in the file `SUCCESSOR.md`.
3. **Save only what the person accepted**, in `<config folder>/settings.json` (not in the project's: there, auto as the default mode doesn't take effect). Each item below is sensitive: save it only with the answer to its own question and, in "Box by box, checking" mode, show the snippet and wait for "Save". Never save `"defaultMode"`, an allow rule or a hook on your own:
   - Question 5 "Allow both rules": under `"permissions"` → `"allow"`, add the exact names of the create and run scheduled-task tools as ToolSearch showed them (in November 2026: `"mcp__scheduled-tasks__create_scheduled_task"` and `"mcp__scheduled-tasks__run_scheduled_task"`). Create what is missing and don't delete what already exists.
   - Question 9 "Yes, auto": under `"permissions"` set `"defaultMode": "auto"`. With "Don't change", leave that field alone.
   - Question 5 "Don't allow": nothing in `settings.json`; in the question 1 rule, delete the part from "I use a scheduled task" to "If that also fails:", inclusive.
   - Question 10 "Install the hook": copy `scripts/spare_allow.py` to `<config folder>/hooks/spare_allow.py`, create an empty `<config folder>/spares.txt` and, under `"hooks"` → `"PreToolUse"`, add `{ "matcher": "SendMessage|mcp__ccd_session_mgmt__.*", "hooks": [ { "type": "command", "command": "python \"<config folder>/hooks/spare_allow.py\"", "timeout": 10 } ] }` (replace `mcp__ccd_session_mgmt__` with the name prefix ToolSearch showed). The hook approves the switch actions on its own (unarchive, title, model, effort, Remote Control and message) only when the target is a spare listed in `spares.txt`; everything else goes through the normal classifier. Without it, auto mode blocks changing a spare that another session created, and sometimes blocks the message with the task, judging it a way around the `start_session` lock (seen on 2026-11-04). With it, a session did all of this on a spare it hadn't created, with no box at all (tested the same day). Don't use allow rules for these tools: they would apply to every session. With "Without the hook": copy and register nothing, don't create `spares.txt` and, in the "Spares" rule, delete the parts about `spares.txt`.

   Check with `check_settings.py`. Tell the person that auto as the default mode needs a recent Claude Code version and a plan that has this mode; without them, the session starts in normal mode.
4. **Explain to the person the traps** the author found (tested in November 2026):
   - **The app refuses to open the session** when the turn didn't come from a message by the person: an agent notice, a message from another session, a scheduled task, and even the first turn of a session opened by another one. The refusal comes from the app itself, and no setting changes it. A new message from the person in the middle of such a turn already unlocks it: in a test on 2026-11-04, the turn started from an automatic notice, the person answered question boxes and sent messages in the middle, and the successor opened. A question-box answer alone does not unlock it (another test the same day: the person answered "open it now" in the box and the app refused again), so the rule asks for a new message. That is why the rule leaves the switch, when possible, for a turn that came from a message by the person ("notify and carry on", question 6), and has fallbacks: first a scheduled task (the project's manual-only one, run right away, or a one-time one for ~2 minutes later, with the same request; it appears in the app as a session); then Path B, if installed; last, warn the person.
   - **In auto mode, the classifier** (the filter that approves or blocks each action) **may block the scheduled task**, because it runs on its own later. The allow rule from question 5 solves it: an action with its own rule skips the classifier (this is in the auto mode documentation). With the rules, creating and running the task worked on an automatic turn; without the run rule, the classifier blocked `run_scheduled_task` even on a turn from the person (2026-11-04).
   - **A scheduled task doesn't keep the mode of the session that created it**, not even when created on a turn from the person: it runs in the default mode from the settings. If that mode is normal, the successor stops at the first command, waiting for approval. Hence question 9 ("Start every session in auto mode?").
   - **The app refuses to archive the previous one while it has "live work"**: a turn in progress (it is still writing its last message when the successor starts), an agent or background task, a queued message, or someone watching through Remote Control (on the phone, for example). That is why the rule turns off the previous one's Remote Control first, tries again on the next turns and, if it is a background agent, doesn't force it. Archiving may also ask for approval in a card, depending on the permission mode.
   - An approval given earlier doesn't unlock opening the session: the app looks at whether a message came from the person, not at what they already approved. What helps is switching sessions on a turn from the person when the conversation is already near the limit, without waiting.
   - **Why spares and "notify and carry on" come before the scheduled task:** a successor opened by a scheduled task lives only in the Routines section and has no `start_session`, so the chain gets stuck there. A spare stays in the normal list. By notifying and carrying on, the switch happens on the person's next message, in the normal list. The notification (`PushNotification`) reaches the phone only with Remote Control on, and the app doesn't show it if the person is already looking at the session.
   - **Spare session** (question 6; tested on 2026-11-04, all on an automatic turn): a session created ahead of time with the request "do nothing, reply only 'ready'", then detached and archived, can be unarchived, renamed and given the task by message without the person. It worked in the default mode from the settings (in the test, auto), without asking for approval, and it sits in the normal session list, not in Routines. Model and effort don't need one spare of each kind: the session that uses the spare changes both on it (`set_session_model`, `set_session_effort`) before sending the message; the app doesn't let a session change its own model, only another's. Traps: the spare's Remote Control only turns on after it receives the message (before that, the app replies "requires an active session"); each spare starts in the folder of the session that created it, so spares are per folder; creating a spare uses `start_session`, which only works on a turn that came from a message by the person, so refilling waits for such a turn; a successor that came from a spare is already detached and doesn't call `detach_session`.
   - A one-time task stays in the scheduled tasks list, turned off, after it runs. Deleting the task archives the session it opened: only delete it once the chain has moved past it.
   - **A manual-only task (no schedule) is the best fallback** in a regular session. Created ahead of time, it stays on after it runs (it doesn't turn itself off like a one-time task), runs again at every switch, and opens the session within seconds with `run_scheduled_task`, on an automatic turn too (with the question 5 rules; tested on 2026-11-04). Limits: the app refuses to run a task from inside a session a task opened ("from a scheduled-task run session"), and that session doesn't have `start_session` either; it refuses to run while another run of the same task is in progress; and the task runs in the folder of the session that created it (the tool has no folder field). Since the task's request is fixed, what changes at each switch goes in a file `SUCCESSOR.md` in the folder, which the previous session rewrites right before running the task: the whole request (handoff, "Previous session: <id>", the successor's title). That way a folder with several handoffs uses a single task. The new session starts with the task's title; the previous one changes it with `set_session_title` (worked on 2026-11-04). Create the task with `notifyOnCompletion` false: otherwise the session that created it gets a notice on every run and wakes up to reread the conversation.
   - **A session opened by a scheduled task starts without Remote Control and with medium effort.** The session that created the task, if it is still in its turn, checks in `list_task_runs` that it opened and adjusts both (`set_remote_control` and `set_session_effort`). The task's own session can't: while nobody opens it on screen, every action that needs approval is refused ("nobody has opened this scheduled run"). That included turning its own Remote Control on and creating another scheduled task, even with the allow rule (tested on 2026-11-04). So a successor opened by a task only opens the next one on a turn that came from a message by the person, or after the person opens it on screen; if it can't, it warns the person.
   - **Routines:** in the app, each scheduled task becomes a "routine". The session it opens appears only inside the Routines section of the sidebar, under the routine, not with the other sessions. If that section is turned off, the successor exists but the person doesn't see it. Check with `list_sections` (section `routines`, field `shown`). If it is off, ask the person to turn it on in the sidebar's filter menu: Claude can't (no tool turns the section on or moves the session out of it). Also, a one-time task turns itself off after it runs; once off, it and its session disappear from the Routines section when the session ends its turn (the session isn't archived, only hidden; seen on 2026-11-04). That is why the final message of the session that created the task always includes the new session's link.
5. **Test** (with the person's yes; it opens a real session and uses a little quota):
   1. Create a test folder, `~/Documents/successor_test/` (not in the config folder, which is protected), with a `HANDOFF.md` whose exact next step is: *"Create `ok.txt` with the word ok and write STAGE DONE on the first line of this handoff."*
   2. Open a session called "Successor test" with the request: *"Install test: don't archive or detach any session. Read and follow `<path>/HANDOFF.md`."* (Without that sentence, the close-the-previous rule could detach or archive this install session.)
   3. Check with `list_sessions` that it appeared. When it finishes, check that `ok.txt` exists. Tell the person they can archive the test session and delete the folder.

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

Only if question 3 was "Yes, guide me". Go slowly: one step at a time, waiting for the person to say they did it before going on.

**What the token is** (explain it to the person like this): an access key to their Claude account, valid for one year, made for scripts. Whoever has the token uses their quota. It is like a password.

1. **Check the terminal Claude Code.** Run `claude --version`. If the command doesn't exist, the person needs to install the terminal Claude Code (official instructions at https://code.claude.com/docs). The token works on the Pro, Max, Ultra, Team and Enterprise plans.
2. **The person generates the token.** You, Claude, don't run this command: it opens the browser and shows the token on screen. Ask them to run, in a separate system terminal window that they open themselves outside this conversation:

   ```text
   claude setup-token
   ```

   **Never** in the terminal panel of the Claude app, nor in the code editor's terminal: Claude can read those panels, and the token would end up in the conversation.

   They log in in the browser, and the terminal shows the token (a long text). They copy the token and **don't paste it anywhere yet, not even in the chat**.
3. **The person saves the token in a file**, in the same terminal window, with the token still copied. The commands below assume the default folder (`.claude` in the home folder); if the config folder is another one, change the file path in them (and use `--token-file` in the script, if it doesn't find the file):
   - Windows (PowerShell):

     ```powershell
     Get-Clipboard | Out-File -NoNewline -Encoding ascii "$HOME\.claude\relay_token.txt"
     icacls "$HOME\.claude\relay_token.txt" /inheritance:r /grant:r "$($env:USERDOMAIN)\$($env:USERNAME):F"
     icacls "$HOME\.claude\relay_token.txt"
     ```

     (The second line leaves only their user able to read the file; the third shows the permissions, and only their user should appear.)
   - Mac and Linux: they run the command below, paste the token (it doesn't show on screen) and press Enter:

     ```bash
     umask 077; read -rs T; printf %s "$T" > <config folder>/relay_token.txt; unset T
     ```

   Then they really clear the clipboard and close that terminal window:
   - Windows: copy anything else and, if the clipboard history (Win+V) is on, delete the token's item there too.
   - Mac: copy something else. Remind them that the universal clipboard carries what was copied to their other Apple devices.
   - Linux: copy something else.

   **Why a file, and not a system variable** (`setx` on Windows, `export` in the terminal profile): the token would apply to every `claude` opened on that account of the computer, and the normal login (`/login`) would stop working until the variable is removed. In the file, it is read only by the script and handed only to the rounds.
4. **You check without seeing the token**; the command prints only yes or no:

   ```text
   python -c "import os, pathlib; t = (pathlib.Path(os.environ.get('CLAUDE_CONFIG_DIR') or pathlib.Path.home() / '.claude') / 'relay_token.txt').read_text(encoding='utf-8-sig').strip(); print('ok' if t.startswith('sk-ant-') and not any(c.isspace() for c in t) else 'check the file: it must have only the token, one line')"
   ```

   Never run `cat`, `type` or `Get-Content` on that file, and never open it with Read. If the config folder is inside a git repository or a cloud-synced folder, warn them: the token can't go along (put `relay_token.txt` in `.gitignore` or take it out of the sync).
5. **Forbid reading the file.** In `settings.json`, under `"permissions"` → `"deny"` (create what is missing and don't delete what already exists), add the rule `"Read(<config folder>/relay_token.txt)"`, with the full path already filled in (no `~`). This way the sessions' read tool doesn't open the file (a terminal command isn't covered for sure; that is why the guide says never to run `cat` on it). Tell the person that the relay script already passes the same prohibition to the rounds.
6. **Copy the script:** `scripts/session_relay.py` → `<config folder>/tools/session_relay.py`.
7. **Test in a toy project** (with the person's yes; it uses a little of the quota: two or three quick rounds on Haiku). The test folder is in `~/Documents`, not in the config folder: there the rounds can't write, because the folder is protected and the rounds can't ask for permission.
   1. Create `~/Documents/relay_test/HANDOFF.md` with:

      ```markdown
      # Handoff — relay test

      ## Exact next step
      If `count.txt` doesn't exist, create it with the line "one". If it already exists with "one", add the line "two" and write STAGE DONE on the first line of this handoff.
      ```
   2. Run (always with the full path of `tools/session_relay.py` in the config folder; on Windows, with `/` slashes):

      ```text
      python <config folder>/tools/session_relay.py --folder ~/Documents/relay_test --handoff HANDOFF.md --model haiku --rounds 3
      ```
   3. Expected: round 1 creates "one" (STATUS: CONTINUE); round 2 adds "two" and writes STAGE DONE; the script stops by itself. The record is in `~/Documents/relay_test/relay.log`, one line per round.
   4. If there is an unknown-option error, the person updates Claude Code (`claude update`) and you try again. On Windows, if the error mentions odd arguments, pass `--claude "<path to claude.exe>"`: `claude.cmd` mangles arguments with parentheses and asterisks.
8. **Save the rule** for Path B with the tools from question 4:
   - "Files only": `--tools "Read,Glob,Grep,Edit,Write"` (the script's default).
   - "Files + terminal": add the name of the terminal tool that appears in the person's tool list (on Windows it may be `Bash`, which is Git Bash, or `PowerShell`); don't assume it from the system. For example `--tools "Read,Glob,Grep,Edit,Write,PowerShell"`.
   - "Decide per project": the rule says to ask the first time in each project and note the answer in that project's CLAUDE.md.
9. **Explain to the person the gaps** the author found (the rule already covers the first three):
   - It runs hidden: it doesn't appear in the app. Whoever launches it warns in one line, and the next conversation checks `relay.log`.
   - A round that goes past the time limit (`--timeout`, default 1 hour) is cut, and the relay stops. A long task needs a bigger `--timeout`.
   - The script stops at the round limit even if the last one says CONTINUE, and nobody opens the next one.
   - It uses the same quota as the person.
   - If the token leaks, treat it as a leaked password. The official documentation (checked in November 2026) doesn't show how to revoke only this token: look in the account settings on claude.ai for the list of accesses and sessions, or contact Anthropic support.
   - To turn Path B off: delete `<config folder>/relay_token.txt` (without the token the script doesn't run), `<config folder>/tools/session_relay.py` and, in each project, `relay.log`; remove the "Screenless rounds:" rule from `CLAUDE.md` and, from `settings.json`, the line `Read(.../relay_token.txt)` under `"deny"` (optional). If the token may have leaked, deleting the file doesn't revoke it: see the item above. The token lasts one year.
   - None of this is approved on its own: the round only uses the tools on the list the person chose (question 4); the rest is refused, with no question.

Rule text (Path B):
> - Screenless rounds: `python <config folder>/tools/session_relay.py --folder <project> --handoff <handoff> --model sonnet --rounds 3 --tools "<list>"`, launched detached in the background (Windows: `Start-Process ... -WindowStyle Hidden -PassThru`; Mac and Linux: `nohup ... &`), keeping the process number. Use: <when I am in the terminal | only as a fallback, when the app refuses to open a session>. It runs hidden: I warn the person in one line; at their next message, I check the project's `relay.log` and, if the handoff doesn't say STAGE DONE and nothing is running, I launch it again or open the successor. Long task: bigger `--timeout`. I never read, show or copy `relay_token.txt`.

---

## Box 8 — Spend watch and measuring

**What this does:** a script that runs by itself at every message and every tool used, and warns Claude when the session passes certain limits. Claude tells the person in one line and proposes what to do (update the handoff, open the successor, use a cheaper agent).
**Why:** nobody notices the conversation growing. In the author's use, 14 of 36 session switches only happened after 250k tokens, until the watch started warning in the middle of the turn.
**Real risks:**
- The scripts read the local session records (`<config folder>/projects`), which contain the whole conversations. They only count tokens, model and time; they don't copy the content. Nothing leaves the computer: no script uses the network.
- They write only small files next to the script (`hooks/spend_watch_state/` and `tools/measure_marks.csv`).
- If the watch fails (no Python, record format changed): it goes silent or Claude Code shows a hook error; it neither blocks nor approves anything, and work goes on.
- Cost: the warning is one line in the context, only when a limit is crossed (a few times per session). The watch runs at every message and every tool, but reads only what is new.
- The plan measuring is an estimate; it holds only for your use and may vary.
**How to undo:** delete `hooks/spend_watch.py` and the two spend-watch lines under `"UserPromptSubmit"` and `"PostToolUse"` in `settings.json` (or restore the Box 1 backup), and the Box 8 lines in CLAUDE.md. If you want, also delete `hooks/spend_watch_state/`, `tools/measure_point.py`, `tools/measure_marks.csv`, `tools/usage_report.py` and the `skills/usage-report/` folder. Applies from the next session.

Plan (Box 1): with "API key", don't ask questions 2 and 3 (there is no weekly %; spending shows up in money, in the API console) and don't put them under "Declined"; the spend watch (question 1) works the same, because it warns in tokens. With "Team or Enterprise" or "I don't know", ask both, but say they only work if the usage screen shows a weekly limit %; if, when reading it, there is no %, stop and tell the person.

Questions:

1. **Install the spend watch?** — header `Spend watch` (only with Python)
   - **Yes, author's limits (Recommended)** — Warns with the conversation at 200k tokens (and every 100k more), at 40, 80 and 150 prompts, and when an agent reaches 100 and 150 calls. Reads the local records; nothing leaves the PC.
   - **Yes, warn earlier** — Conversation at 150k; agent at 60 and 100 calls. More warnings in the context, in return for switching sessions sooner.
   - **No** — Nothing is installed; you keep going without a big-conversation warning.
2. **Check usage before and after a big task?** — header `Before/after` (not with "API key")
   - **Yes (Recommended)** — Claude notes the plan usage % before a big task and says the difference at the end, in one line. Just a rule in CLAUDE.md; no script.
   - **No** — Nothing changes; you check usage whenever you like.
3. **Measure how much 1% of the quota is worth on your plan?** — header `Measure plan` (not with "API key"; with Python)
   - **Yes** — You note the usage % at two moments, with one or two days between them, and a script does the math. After that, the watch also warns in % of the quota. The script reads the local records and writes a small .csv.
   - **No** — The watch warns only in tokens.
4. **Install the usage report skill?** — header `Usage skill` (only with Python)
   - **Yes** — I copy a skill to `<config folder>/skills/usage-report/`: when you ask "how much did I spend" or "where did my quota go", Claude runs a script that adds up spending by session and by model. It reads the local conversations (counts only); nothing leaves the PC.
   - **No** — Nothing is installed; Claude answers those questions without the ready-made report.

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
   5. Tell the person: the watch reads the sessions' internal records, which may change in a Claude Code update. If they change, it goes silent, without getting in the way.
   6. Check: open a Haiku agent with the request *"SPEND-WATCH-TEST. List 6 files in this folder, one per tool call, and return any 'SPEND WATCH' warning that appears."* With that mark at the start of the request, the watch uses test limits (3 and 5 calls). If the warning doesn't come, the person opens a new session (in the app, a new session in the same folder; in the terminal, quit and run `claude` again) and you repeat the request there; some versions only read the hooks when the session opens. If they prefer, leave the test for the final box.
2. Question 2 "Yes": save the rule. To read the usage %: in the app, the `get_usage` tool (look for it with ToolSearch); without it, ask the person for the number (the usage screen of the app or of claude.ai, or `/usage` in the terminal).
3. Question 3 "Yes":
   1. Copy `scripts/measure_point.py` to `<config folder>/tools/measure_point.py`.
   2. Read the weekly % now (as in question 2) and run `python <config folder>/tools/measure_point.py <%>`. This records the first mark.
   3. Save the rule. From the second mark on, the script shows how many weighted tokens 1% of the quota is worth. When the result is stable (two or three similar calculations), put that number in `POINT`, at the top of `spend_watch.py`: the watch then also warns in % of the quota.
   4. Tell the person: between two marks there can't be a reset of the quota week, and conversations outside Claude Code (in the regular chat of claude.ai or of the app) are not in the records; if they use the regular chat a lot in that interval, the number comes out low. Marks less than 3 points apart are not lost: the script adds them to the next ones until they reach 3.
4. Question 4 "Yes": copy the package's `skills/usage-report/` folder to `<config folder>/skills/usage-report/` and `scripts/usage_report.py` to `<config folder>/tools/usage_report.py`. If question 3 was "No", also copy `scripts/measure_point.py` to `tools/` (the skill uses it for "how much is 1% worth"), without running it. Say: applies from the next session; to undo, delete the skill folder. No CLAUDE.md rule needed.

Rule text:
> - Spend watch: when a "SPEND WATCH" warning appears, tell the person in one line, with the number, and propose what to do (handoff, successor, cheaper agent).
> - Before and after a big task: note the plan usage % and say the difference at the end, in one line.
> - Plan measuring: at the start of a session, if the last mark in `<config folder>/tools/measure_marks.csv` is more than a day old, read the weekly % and run `measure_point.py` with it. When the estimate gets stable over two or three calculations, propose putting the number in `POINT` in `spend_watch.py`.

---

## Box 9 — Checking the work

**What this does:** checking is mandatory, but you can check while spending less. This box only saves behavior rules in CLAUDE.md; no script, hook or permission changes.
**Real risks:**
- "Two reviews, sensitive only" may let an error through in an area you don't consider sensitive; if in doubt, leave it unchecked.
- "Cheap proof" uses fewer images: rarely, the text won't show a visual defect. Ask for an image whenever you want.
- The end-of-turn habits make final messages a little longer; no other risk.
- They are only instructions: Claude may forget one in a very long conversation.
**How to undo:** delete the rule's line in CLAUDE.md (or restore the Box 1 backup). Applies from the next session.

Questions (two, both with several answers: `multiSelect: true`):

1. **Which of these habits become rules?** — header `Checking`
   - **Cheap proof** — When a text proves it (a log line, a value, test output), use the text. An image only cropped to what matters and at a smaller scale; measurements taken by script. A visual-only defect may slip through; ask for an image if you want.
   - **Tests in parts** — After each change, the tests for what changed and a short regression; the whole suite before publishing. An error outside the tested part only shows in the final suite.
   - **Two reviews, sensitive only** — Security, accounts, payment and cryptography get two independent reviews; the rest, one. Costs more in those areas and less elsewhere.
   - **Don't pay twice** — After an interruption, check whether agents and background tasks are still running and resume, instead of starting over. A process is ended only by the number (PID) that the session itself started, never by name. Avoids taking down other sessions' work.
2. **Which end-of-turn habits become rules?** — header `Turn end`
   - **Pending questions** — Questions that come up during the work go to a project questions file and are repeated at the end of every final message. The final message gets a little longer.
   - **Can I stop?** — Before stopping, Claude asks itself "should I be doing something before stopping?"; if so, it does it; if not, it says what it is waiting for and what will wake the session. Avoids idle sessions; costs a short check.
   - **Complete final message** — The answer comes on the first line, followed by the pending items and what didn't go so well or could have gone better. More honest; a little longer.

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

**What this does:** if the guide helps, a star on the repository helps other people find it. Instead of asking now, before the person has seen any result, Claude can remind them in a week. Explain this in up to 2 sentences. Don't push, and don't put "(Recommended)" on any option.
**Real risks:** practically none. It saves one line in CLAUDE.md, which costs a few words of context until used. No data leaves the computer; the link is only shown, and Claude never stars it for you.
**How to undo:** delete the "One-time reminder (star)" line from CLAUDE.md. It also deletes itself once used.

Question:

1. **Do you want me to remind you in a week to decide whether to star the repository?** — header `Star`
   - **Yes, remind me** — In 7 days, in the first conversation, Claude asks just once whether the tactics helped and shows the link. You decide; Claude never stars it for you.
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
4. How to undo, one line for each thing installed: each rule (delete the line in CLAUDE.md); each setting (delete the key under `"env"` or `"permissions"` in `settings.json`); each hook (delete its entry under `"hooks"` and the copied file: `spend_watch.py` under `"UserPromptSubmit"` and `"PostToolUse"`, `agent_limit.py` under `"PreToolUse"`, `copy_lock.py` under `"PreToolUse"` and `"SubagentStop"`, `handoff_reminder.py` under `"SessionStart"`, `spare_allow.py` under `"PreToolUse"`, plus `spares.txt`); each script in `tools/`; the templates in `templates/`; the usage skill (delete the `skills/usage-report/` folder); and, if there is one, `<config folder>/relay_token.txt` (delete the file and, if a token was created, revoke it where it was created). To undo everything at once: restore the Box 1 backups and delete the copied files. Also say when each thing starts to apply (the next session, for settings, hooks and the skill).
5. What was left half done (for example, the second mark of the plan measuring). If the brake test or the spend-watch test was left for later, tell the person to open a new session and say there: "repeat the brake (or spend watch) test from the Quota Keeper guide".
6. If Box 10 saved the reminder, the date it will show up.
7. If the mode was Quick: Group 3 (Box 7) was not installed. To turn it on later, ideally after a week or two, just ask "run Box 7 of the Quota Keeper guide".
8. The credit: "Tactics by Jaber Felippe Neto (JN Softworks), text under CC BY 4.0, scripts under MIT." If the person is going to share the guide, they should send the whole folder, with the credit.
