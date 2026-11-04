# JN's Quota Keeper — token saving for Claude Code

> **Made by Jaber Neto (JN Softworks).** License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may copy, adapt and share it, as long as you keep the author's name and the license link. The scripts are under the MIT license, which also asks you to keep the credit. Version 1.0, November 2026.

This file is for Claude. If you are the person: you don't need to read it. Claude will show one question box per tactic and will change only what you accept.

## How to run the setup (Claude, read this before anything else)

1. **Nothing changes without a yes.** Each tactic has a question box. Show the box, wait for the answer, do only the steps for that answer, check them, and only then go to the next box.
2. **Show each box with AskUserQuestion**, one call per box, with the questions, headers and options exactly as written here. The tool adds an "Other" option by itself. Without that tool, ask the same questions in a short numbered list and wait.
3. **Before each box, explain in up to 3 simple sentences** what the tactic does and why. The person may not be technical: no acronym or jargon without a plain explanation in the same sentence.
4. **Follow the order of the boxes.** If a box doesn't apply (for example, the person doesn't use agents), say so in one line and go to the next one.
5. **Write the rules with the ready-made text** of each box ("Rule text"). Don't rewrite or decorate it: every extra line in CLAUDE.md is paid for in every session. Of the parts between `< >`, fill in only the ones that belong to the setup:
   - a chosen number, like `<200>`: put in the number from the person's answer;
   - `<config folder>`: its full path (defined just below), with `/` slashes, for example `C:/Users/jane/.claude`;
   - `<path>`: only in the Box 7 tests, the full path of the test folder;
   - `<list>`: the tools chosen in Box 7;
   - a choice `<a | b>`: keep only the option that matches the answer and delete the other.

   These stay literal in the saved rule, for the session to fill in later: `<file>`, `<handoff>`, `<project>`, `<id>`, `<n>`, `<session title>`, `<date>`, `<session id>`.

   **Where the rule lines go:** inside the `## Quota Keeper ...` section of the chosen CLAUDE.md, under the `### Rules` subtitle, before `### Declined`. Box 1 creates the section and both subtitles (at the end of the file if the section doesn't exist). If the section already exists without `### Rules`, create that subtitle before `### Declined`. Decline lines go under `### Declined`. The labels in square brackets (like "[Number]") only say which version to pick: they are not saved.
6. **Never ask for a token, password or key in the chat**, and never run a command that shows one on screen. Box 7 teaches the person to save the token by themselves.
7. **Talk little between steps.** The full summary comes in the final box.
8. **When in doubt, stop and ask.** If something here doesn't match what you see on the person's computer (a tool with another name, an option that doesn't exist, an error), say what you found and ask. Don't make things up.
9. **Tool and option names change.** The ones named here are from November 2026. Look for them by name with ToolSearch; if you can't find one, say so and go on without that part.

**What is never skimped on** (always applies, no box): a backup before changing settings, confirmation before anything irreversible, building and testing what changed, and reading the exact piece of code that is about to be edited.

**Files in this package** (paths start from the folder where `START_HERE.md` is):
- `en/GUIDE.md` (this one) and `en/HANDOFF_TEMPLATE.md` (template for the handoff file) and `en/SUMMARIES_TEMPLATE.md` (template for the summaries file)
- `scripts/spend_watch.py` (spend watch), `scripts/agent_limit.py` (agent brake), `scripts/session_relay.py` (screenless rounds), `scripts/measure_point.py` (measure how much 1% of the plan is worth), `scripts/check_settings.py` (check `settings.json`)
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

The author's numbers (Ultra plan, formerly Max 20x, September to November 2026, measured in the session records):
- Rereading the conversation was 73% of the cost; storing the conversation to reread it later (the cache) was 19%; writing and thinking, 8%.
- With the handoff and session-switch rules (Box 6), the main conversation fell from ~12.7 to ~3.2 points of the quota per day of use (75% less).
- Agents that went past 100 calls were 74% of the agents' cost (Box 5).
- Agents waiting for a build or a test, with the default 5-minute cache, rewrote the whole conversation when they came back: ~26% of all the cost in 8 days, until the 1-hour cache was turned on (Box 2).

The yardstick used to compare (it is not an official price):

```text
weight = input × 1 + cache write × 1.25 (5-minute cache) or × 2 (1-hour cache) + cache read × 0.1 + output × 5
```

How much 1% of the quota is worth depends on the plan. On the author's Ultra plan (formerly Max 20x), 1% of the week was ~8.5 million weight. Don't use this number for another plan: Box 8 measures the person's own.

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

## Box 1 — Before you start

**What it is:** decide where the rules go and how the person uses Claude Code. Nothing changes yet.

Questions:

1. **Where should the rules you accept be saved?** — header `Save rules`
   - **In all projects (Recommended)** — They go to the `CLAUDE.md` of Claude Code's config folder (usually `~/.claude/CLAUDE.md`) and apply in any folder.
   - **Only in this project** — They go to the `CLAUDE.md` of the folder that is open now. This applies only to the rule lines.
2. **Where do you use Claude Code?** — header `Where used`
   - **Desktop app** — The Claude app on the computer, in the Code tab.
   - **Terminal** — The `claude` command in a terminal window or inside the code editor.
   - **Both**
3. **How do you pay for Claude?** — header `Plan`
   - **Pro, Max or Ultra** — Personal subscription, with a weekly usage limit.
   - **Team or Enterprise** — Company plan; the limits may be set by the company.
   - **API key** — Pay per use (per token), no weekly limit in %.
   - **I don't know** — That's fine: the guide stays general and says, in each box, what depends on the plan.

Don't put "(Recommended)" on any option in this question: it is a fact about the person, not a choice.

Steps:
1. Make a backup, with the date in the name, of each file that exists: `<config folder>/settings.json` → `settings.json.before-quota-keeper-<YYYY-MM-DD>`, and the chosen CLAUDE.md → `CLAUDE.md.before-quota-keeper-<YYYY-MM-DD>`. The date is today's, from the computer's clock (for example `2026-11-04`). Each backup stays in the same folder as the original, next to it. Tell the person where they are.
2. At the end of the chosen CLAUDE.md (create it if it doesn't exist), add the section below. The next boxes put rule lines under "Rules" and declines under "Declined".

   ```markdown
   ## Quota Keeper (tactics by Jaber Neto, JN Softworks)

   ### Rules

   ### Declined (don't offer again)
   ```

   If the answer was "Only in this project" and that CLAUDE.md is shared with other people (in a repository, for example), warn them before saving.

   Settings, hooks and scripts always belong to the whole user (`<config folder>/settings.json`), even with "Only in this project": that answer applies only to the rule lines. Tell the person this.

   If the "Quota Keeper" section (or "Token saving", its old name) already exists (the guide was run before), update the existing one, never create another. The same goes for the settings and hooks in the next boxes: if they are already in `settings.json`, update them, never duplicate.
3. Check that Python 3 is installed (`python --version` or `python3 --version`). The scripts in Boxes 5, 7 and 8 need it. If it isn't, warn that those parts will need Python (https://www.python.org/downloads/) and go on with the rest.
4. Keep the answer to "Where used": Box 7 depends on it.
5. Keep the answer to "Plan": Boxes 7 and 8 depend on it. Never assume the plan, not even from what a tool shows. With "I don't know", speak in general terms ("if your plan has a weekly limit in %...") and let the person decide. If they want to find out, show what the usage screen says (in the app, the `get_usage` tool; in the terminal, `/usage`) and ask them to confirm; without their confirmation, it stays "I don't know".

**Declines, in all boxes:** every tactic answered "No" (or unchecked) becomes a line under "Declined", with its name, so that no session asks again.

---

## Box 2 — Settings

**What it is:** three adjustments in `<config folder>/settings.json` and one effort rule.
**Why:** agents on a cheaper model; an agent that waits doesn't pay for the whole conversation again; the conversation summarized before every step gets expensive.
**Note:** the numbers in this box (compact at 50%) assume the 1-million-token window. Check the person's window (rule "Context window", at the start of the guide; if you can't see it, assume 200k). If it is 200k, don't lower the compaction: skip question 3 and leave the default.

Questions:

1. **Should agents start on Sonnet?** — header `Agents`
   - **Yes (Recommended)** — Every agent starts on Sonnet, which is cheaper than Opus. When needed, Claude asks for Opus or Haiku for a specific agent.
   - **No** — Agents use the same model as the conversation.
2. **Do your agents often wait more than 5 minutes for something (builds, tests, downloads, renders)?** — header `Long waits`
   - **Yes, 1-hour cache** — An agent that waits doesn't pay for the whole conversation again when it comes back. Each write costs more (2 times instead of 1.25), so it only pays off with long waits.
   - **No, leave as is** — Quick tasks: the default 5-minute cache is enough.
3. **When should the conversation be summarized automatically?** — header `Compaction`
   - **At 50% (Recommended)** — The conversation is summarized when it reaches half of the space, before every step gets expensive.
   - **At 25%** — For long production in a single session. It summarizes more often and loses more detail.
   - **Leave it** — Stays at the default, near the end of the space.
4. **Make a rule: High effort, no agent-fleet mode?** — header `Effort`
   - **Yes (Recommended)** — Claude recommends High effort; Max only for a very hard problem; no mode that opens many agents at once unless you ask.
   - **No**

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

**What it is:** CLAUDE.md and the memory index come into every session before the first message and are reread at every step. Every line in them is paid for many times a day. The way of talking comes with it: writing costs 5 times more than reading, and everything written stays in the conversation.

Questions:

1. **Keep CLAUDE.md short (rules and pointers; details go to other files)?** — header `CLAUDE.md`
   - **Yes, and suggest cuts (Recommended)** — It becomes a rule, and Claude proposes now what to move to another file. Nothing leaves without your yes.
   - **Rule only** — Applies from now on; the current file stays as it is.
   - **No**
2. **Memory with a short index (one line per note; a big project gets a summary note)?** — header `Memory`
   - **Yes (Recommended)** — The index is read in every session, and only up to a certain size. A short line fits more and costs less.
   - **I don't use memory**
   - **No**
3. **Short messages in the middle of the work, everything together at the end?** — header `Chat style`
   - **Yes (Recommended)** — Between steps, just one line about what it is doing. Answers, results and warnings come together in the final message.
   - **No** — I prefer to follow in more detail.
4. **Long things go to a file, not to the chat?** — header `Long text`
   - **Yes (Recommended)** — To show a big text or log, you save it in a file in the folder and give the name; Claude reads only the part it needs.
   - **No**

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

**What it is:** everything Claude reads stays in the conversation and is reread at every following step.
**Why:** a 50k-token file read at the start costs ~5k of weight at every step after that; over 100 steps, ~560k. Read by an agent, it never enters the main conversation.

Question (just one, with several answers: `multiSelect: true`):

1. **Which of these reading habits become rules?** — header `Reading`
   - **Search instead of reading** — Look for the name or title and read only about 50 lines around it. Never read a big document, a log or a generated file in full.
   - **Big reads go to agents** — An agent reads and returns only the summary; the volume doesn't enter the conversation. Haiku to find and filter; Sonnet to understand.
   - **Extract once** — When several tasks use the same big source, an agent writes a short note with what matters, and the next ones read the note.
   - **Filter logs at source** — Mark the log's own lines and search only for the mark; never load a whole build or test log.

Steps: save one line per checked item; the unchecked ones go to "Declined".

Rule text:
> - Search before reading: look for the name and read only the part around it; big documents, logs and generated files are never read in full.
> - Big reads (logs, several files, long documents) go to an agent that returns only the summary (Haiku to find, filter and count; Sonnet to understand). Read in full only what I am going to edit.
> - Big source used by several tasks: extract once into a short note in the project and reuse the note.
> - Logs: mark my own lines and search for the mark; never load a whole build or test log.

---

## Box 5 — Agents

**What it is:** an agent is born with an empty conversation, so each of its steps is cheap at the start. But it also rereads its own conversation at every step, and it gets expensive if it works for a long time.
**Why:** in the author's use, agents with 100 or more calls were 74% of the agents' cost, and 71% of that cost came from steps where the agent's conversation was above 200k tokens.

Questions:

1. **Short agents: stop at ~100 calls and hand over?** — header `Short agent`
   - **Yes, at ~100 (Recommended)** — The agent finishes the item, writes where it stopped in a file and returns the summary. If work is left, the main conversation opens another agent from that file.
   - **No**
2. **Which model for each kind of work?** — header `Models`
   - **By role (Recommended)** — Sonnet by default; Haiku for the mechanical (finding a file, filtering a log, counting); Opus only for delicate code (security, accounts, money, cryptography).
   - **Experimental: Opus coordinates** — An Opus agent splits the task, opens Sonnet agents one at a time, runs the tests and reviews only what changed. Still being tested by the author.
   - **Don't change**
3. **Agents in batches and with short answers?** — header `Batching`
   - **Yes (Recommended)** — One agent per task (not one per tiny piece); several launched in the same message; each one writes the detail in a file and returns 5 to 10 lines.
   - **No**
4. **Install the agent brake?** — header `Brake`
   - **Yes (Recommended)** — A script stops an agent opened by another agent from opening more agents, and limits each agent to 6 children. It prevents endless chains.
   - **No**

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

Rule text:
> - Agent that edits or fixes: its request says "when you reach ~100 calls, finish the item, write the resume point in <file> and return the summary". If work is left, the main conversation opens another agent from that file. A big task is born already split into agents of ~100 calls.
> - **[Only with 1-hour cache]** An agent doesn't stay more than ~50 minutes in a single wait; a longer wait = write the resume point and return.
> - Models by role: Sonnet by default; Haiku for the mechanical (finding a file, filtering a log, counting); Opus only for an agent that edits delicate code (security, accounts, money, cryptography).
> - (Experimental) New code or a fix outside security, accounts and cryptography: an Opus agent coordinates. It writes the request for each piece, opens Sonnet agents one at a time (~80 calls each), runs the tests by script, reviews only what changed, fixes what is bad and returns a few lines. A piece that fails twice, Opus does itself. Note each case in `~/Documents/opus_sonnet_pilot.md`; after ~6 cases, ask the person whether it becomes the default.
> - Agents: one per task, not one per tiny piece; several at the same time go out in the SAME message; each one writes the detail in a file and returns 5 to 10 lines.

---

## Box 6 — Handoff and session switch

**What it is:** a short file in each project with what was done, what is half done and the exact next step. When the conversation gets big or the stage changes, Claude updates this file, and a new session starts from it, with an empty conversation.
**Why:** it was the author's biggest saving: the main conversation fell 75% after this rule. The automatic summary (compaction) loses detail; the file doesn't.
**Note:** the numbers in this box (switch at ~250k) assume the 1-million-token window. Check the person's window (rule "Context window", at the start of the guide; if you can't see it, assume 200k). If it is 200k, switch sessions at ~100k (tell the person this at question 2 and use `<100>` in the rule) and don't lower the compaction in Box 2.

Questions:

1. **Use a handoff file in projects with work in progress?** — header `Handoff`
   - **Yes, with the template (Recommended)** — A `HANDOFF.md` at the project root, made from this guide's template. If the project already has a file like that, it uses that one.
   - **No**
2. **When to switch sessions?** — header `Switching`
   - **~200k or new stage** — More switches, every step rereads less. A new stage always starts in a new session.
   - **~250k or new stage (Recommended)** — In the author's numbers (260 sessions), the total cost barely changes between 200k and 300k, and 250k sits in the middle. Above ~300k, every step rereads so much that it costs more. A new stage always starts in a new session.
   - **~300k or new stage** — Fewer switches, every step more expensive. Worth it when the handoff loses a lot of what the conversation knew.
   - **Only when I ask**
3. **One task per session?** — header `One task`
   - **Yes (Recommended)** — A new subject, unrelated to what is open, goes to a new session (or `/clear`), not to the end of this conversation.
   - **No**
4. **A summaries file next to the handoff?** — header `Summaries` (only if question 1 was "Yes")
   - **Yes (Recommended)** — Each session leaves one short entry at the end of a `SUMMARIES.md`: what it did, what it decided, what was left open. It is only for finding later which session did something.
   - **No**

Steps:
1. Question 1 "Yes": copy `en/HANDOFF_TEMPLATE.md` to `<config folder>/templates/HANDOFF_TEMPLATE.md` (create `templates` if it doesn't exist). This is the template: the session creates each project's `HANDOFF.md` from it when there is work in progress. Save the rule.
2. Question 2: save the rule with the chosen number, or the "Only when I ask" rule. Tell the person where to see the conversation size: in the app, the context indicator next to the message box; in the terminal, the `/context` command.
3. Question 3: save the rule. Remind the person: only they can type `/clear` or `/compact`; Claude can't.
4. Question 4 "Yes": copy `en/SUMMARIES_TEMPLATE.md` to `<config folder>/templates/SUMMARIES_TEMPLATE.md` and save the rule.
5. If there is a project with work in progress right now, offer to create its `HANDOFF.md` and the `SUMMARIES.md` next to it (only with a yes).

Rule text (for the session switch, save one of the two versions):
> - Handoff: every project with work in progress has a handoff file (the one the project already has, or `HANDOFF.md` at the root, made from `<config folder>/templates/HANDOFF_TEMPLATE.md`). Rewrite, don't append to the end. Update when each part is finished, before the session switch and when the spend watch warns. A new session starts by reading the handoff and does the "exact next step" without asking, except irreversible actions, which need confirmation.
> - **[Number]** Session switch: with the conversation at ~<250>k tokens, or at a new stage, finish the part in progress, update the handoff and switch sessions. If there is no successor rule, tell the person in one line what to paste into the new session.
> - **[Only when I ask]** Session switch only when the person asks; warn in one line when the conversation passes ~<250>k tokens.
> - One task per session: a new, unrelated subject goes to a new session.
> - Summaries: every project with a handoff file has a summaries file next to it (`HANDOFF.md` → `SUMMARIES.md`; `HANDOFF_X.md` → `SUMMARIES_X.md`; create it from `<config folder>/templates/SUMMARIES_TEMPLATE.md`). Every session, when closing (before opening the successor or ending the stage), appends ONE entry at the end: `## <n> — <session title> (<date>, <session id>)` with up to three short lines: **Did** (with the names someone would search for later: files, screens, tools), **Decided** (what was settled, and by whom), **Open** (what was left open or unanswered, or "nothing"). It doesn't reread the whole file, it only appends. Its only use is finding later which session did something.

---

## Box 7 — Automatic successor session (the most laborious)

**What it is:** at the moment of switching sessions (Box 6), instead of asking the person to open a new session, Claude itself opens the successor, which starts from the handoff. The successor can open the next one the same way: the chain goes on as long as there is work.
**Why:** without this, the switch depends on the person being there to look. The author had a stage stopped all night waiting for a click. And the previous session, if it stays connected to the new one, wakes up and rereads the whole conversation every time the new one finishes a turn.

Prerequisite: Box 6, question 1, answered "Yes". Without a handoff file, skip this box.

There are two paths. Explain both to the person before the box:
- **Path A, through the app (visible, no token):** in the desktop app, Claude has a tool to open another session. The successor appears in the sidebar like any session. It is the recommended one.
- **Path B, through the terminal (screenless, needs a token):** a script runs Claude through the terminal (`claude -p`) in rounds, each with an empty conversation, reading and updating the handoff. It doesn't appear in the app; the result stays in the files and in a log. It needs a long-lived access token. It suits people who use only the terminal, or as a fallback when the app refuses to open the session.

**Before showing any question** (only if Box 1 answered "Desktop app" or "Both"): find the tools with ToolSearch, by name (list in step 1 of Path A), and check this session's permission mode (`get_session` with "self", field `permissionMode`). Then:
- If `start_session` exists: go on as below.
- If `start_session` doesn't exist: Path A isn't available in this version. Tell the person in one line and treat the case as "Terminal" (next item): don't ask questions 1, 2, 5 and 6, which depend on that tool. If they decline Path B ("Not now"), save only the "[I open it]" rule (the minimum rule: Claude updates the handoff and **tells the person to open the new session**), don't save the close-the-previous rule or the inheritance rule, put "Automatic successor session (no tool in the app)" under "Declined", and skip the Path A steps.

How to show the questions (there are six, but not all at once):
- If Box 1 answered "Terminal": don't ask questions 1, 2, 5 and 6, which depend on the app. Ask only 3 and, if the answer is "Yes, guide me", ask 4 in a second call. The successor in this case is the Path B rule; with "Not now", the "[I open it]" rule is used.
- If it answered "Desktop app" or "Both": first call with questions 1, 2 and 3. Second call, if any of these applies: 4 if 3 is "Yes, guide me", and 5 and 6 if 1 is "Claude, on its own".

Question 3 and the plan (Box 1): with "API key", don't ask question 3 (the token exists only for subscriptions) and treat it as "Not now"; if Box 1 also answered "Terminal", the "[I open it]" rule is used. With "I don't know", ask it and say the token exists only on subscription plans (Pro, Max, Ultra, Team and Enterprise); if the token command refuses their account, treat it as "Not now".

In question 3, put "(Recommended)" on **"Yes, guide me"** if Box 1 answered "Terminal", and on **"Not now"** if it answered "Desktop app" or "Both".

In question 5, use the permission mode seen before the questions. If it is `auto` (auto mode), put "(Recommended)" on **"Allow and start in auto"**; otherwise, or if it couldn't be seen, on **"Allow the task only"**.

1. **Who opens the successor session?** — header `Successor`
   - **Claude, on its own (Recommended)** — At the switch, Claude updates the handoff, opens the successor and stops. You just see the new session appear.
   - **Claude proposes, I click** — A card appears for you to start it. If you are not looking, the work stops until the click.
   - **I open it** — Claude updates the handoff and says what to paste into the new session.
2. **Does the successor close the previous one?** — header `Close old`
   - **Yes (Recommended)** — The successor detaches from the previous one and archives it, so the previous one doesn't wake up and reread everything at every turn of the new one. The title gets a number ("Site" → "Site 2" → "Site 3").
   - **No** — Both stay open; you archive when you want.
3. **Install the token for screenless rounds (Path B)?** — header `Token`
   - **Yes, guide me** — You run a command, log in in the browser and save the token in a file. Claude never sees the token. It takes about 10 minutes.
   - **Not now** — Only Path A stays, which needs the desktop app.
4. **What can the screenless rounds use?** — header `Permissions`
   - **Files only (Recommended)** — Read, search, create and edit files. No commands.
   - **Files + terminal** — Also runs commands (tests, builds). More useful and riskier: nobody is watching, and the round's terminal can also see the token.
   - **Decide per project** — Claude asks the first time in each project.
5. **Allow the scheduled-task fallback?** — header `Scheduled`
   - **Allow and start in auto** — Two rules that let Claude create and run a scheduled task without asking for approval, and every new session (in the app and in the terminal) starts in auto mode, including the successor the task opens. For people who already work in auto mode.
   - **Allow the task only** — Only the rules. The successor opened by the task starts in normal mode and stops at the first command or edit, waiting for you to approve. (The app says each routine keeps the approvals given during a run and that they apply to the next runs; not tested.)
   - **Don't allow** — When the app refuses to open the session, the fallback is Path B (if installed) or a warning to you.
6. **When the app refuses to open the successor?** — header `Refused`
   - **Notify and carry on (Recommended)** — Claude saves the handoff, sends a notification (on the computer and, with Remote Control on, on the phone) and keeps working in this session. On your next message, any message, it opens the successor in the normal list before anything else. The fallback (scheduled task, screenless rounds) is kept for when the conversation goes well past the limit with no reply from you.
   - **Fallback right away** — Claude uses the fallback at once. The successor starts sooner but, if it comes from a scheduled task, it is hidden in the Routines section and can't open the next one on its own.

### Steps for Path A (desktop app)

Only if Box 1 answered "Desktop app" or "Both" and `start_session` exists. If it answered "Terminal", or the tool doesn't exist, go straight to Path B (or, without it, to the minimum rule above).

1. **Tools** (found before the questions, with ToolSearch, by name): `start_session` (open a session), `create_scheduled_task` and `list_scheduled_tasks` (create and list scheduled tasks), `run_scheduled_task` (run a task now), `set_session_title` (change a session's title), `detach_session` and `archive_session` (detach and archive), `list_sessions` and `get_session` (list and view sessions), `set_remote_control` (turn Remote Control on and off), `set_session_effort` (a session's effort), `list_task_runs` (sessions a task opened), `list_sections` (sidebar sections), `PushNotification` (a notification on the computer and, with Remote Control, on the phone) and `SendMessage` (a message to another session). In November 2026 they existed with these names in the desktop app. Call `start_session` with initiation "user_asked" (the values "offer" and "own_initiative" become a card waiting for a click) and context "fresh" (empty conversation).
2. **Save the rules** from question 1 (one of the three versions below) and, if question 2 is "Yes", the close-the-previous one; if question 6 is "Notify and carry on", the notify-and-carry-on one (with "Fallback right away", nothing extra: the question 1 rule already uses the fallback). Always save the inheritance rule. Explain to the person that the successor's request carries the current session's id ("Previous session: <id>"), found with `list_sessions` or `get_session`, so the successor knows which one to archive; with the manual-only task (step 4), the whole request goes in the file `SUCCESSOR.md`.
3. **Do what question 5 asked for**, in `<config folder>/settings.json` (not in the project's: there, auto as the default mode doesn't take effect):
   - "Allow and start in auto": under `"permissions"` → `"allow"`, add the exact names of the create and run scheduled-task tools as ToolSearch showed them (in November 2026: `"mcp__scheduled-tasks__create_scheduled_task"` and `"mcp__scheduled-tasks__run_scheduled_task"`); and under `"permissions"` set `"defaultMode": "auto"`. Create what is missing and don't delete what already exists.
   - "Allow the task only": only the two rules under `"allow"`.
   - "Don't allow": nothing in `settings.json`; in the question 1 rule, delete the part from "I use a scheduled task" to "If that also fails:", inclusive.

   Check with `check_settings.py`. Tell the person that auto as the default mode needs a recent Claude Code version and a plan that has this mode; without them, the session starts in normal mode.
4. **Explain to the person the traps** the author found (tested in November 2026):
   - **The app refuses to open the session** when the turn didn't come from a message by the person: an agent notice, a message from another session, a scheduled task, and even the first turn of a session opened by another one. The refusal comes from the app itself, and no setting changes it. A new message from the person in the middle of such a turn already unlocks it: in a test on 2026-11-04, the turn started from an automatic notice, the person answered question boxes and sent messages in the middle, and the successor opened. Whether a box answer alone is enough is unknown (both happened together), so the rule asks for a new message. That is why the rule leaves the switch, when possible, for a turn that came from a message by the person ("notify and carry on", question 6), and has fallbacks: first a scheduled task (the project's manual-only one, run right away, or a one-time one for ~2 minutes later, with the same request; it appears in the app as a session); then Path B, if installed; last, warn the person.
   - **In auto mode, the classifier** (the filter that approves or blocks each action) **may block the scheduled task**, because it runs on its own later. The allow rule from question 5 solves it: an action with its own rule skips the classifier (this is in the auto mode documentation). With the rules, creating and running the task worked on an automatic turn; without the run rule, the classifier blocked `run_scheduled_task` even on a turn from the person (2026-11-04).
   - **A scheduled task doesn't keep the mode of the session that created it**, not even when created on a turn from the person: it runs in the default mode from the settings. If that mode is normal, the successor stops at the first command, waiting for approval. Hence the "start in auto" option.
   - **The app refuses to archive the previous one while it has "live work"**: a turn in progress (it is still writing its last message when the successor starts), an agent or background task, a queued message, or someone watching through Remote Control (on the phone, for example). That is why the rule turns off the previous one's Remote Control first, tries again on the next turns and, if it is a background agent, doesn't force it. Archiving may also ask for approval in a card, depending on the permission mode.
   - An approval given earlier doesn't unlock opening the session: the app looks at whether a message came from the person, not at what they already approved. What helps is switching sessions on a turn from the person when the conversation is already near the limit, without waiting.
   - **Why "notify and carry on" is recommended:** a successor opened by a scheduled task lives only in the Routines section and has no `start_session`, so the chain gets stuck there. By notifying and carrying on, the switch happens on the person's next message, in the normal list. The notification (`PushNotification`) reaches the phone only with Remote Control on, and the app doesn't show it if the person is already looking at the session.
   - A one-time task stays in the scheduled tasks list, turned off, after it runs. Deleting the task archives the session it opened: only delete it once the chain has moved past it.
   - **A manual-only task (no schedule) is the best fallback** in a regular session. Created ahead of time, it stays on after it runs (it doesn't turn itself off like a one-time task), runs again at every switch, and opens the session within seconds with `run_scheduled_task`, on an automatic turn too (with the question 5 rules; tested on 2026-11-04). Limits: the app refuses to run a task from inside a session a task opened ("from a scheduled-task run session"), and that session doesn't have `start_session` either; it refuses to run while another run of the same task is in progress; and the task runs in the folder of the session that created it (the tool has no folder field). Since the task's request is fixed, what changes at each switch goes in a file `SUCCESSOR.md` in the folder, which the previous session rewrites right before running the task: the whole request (handoff, "Previous session: <id>", the successor's title). That way a folder with several handoffs uses a single task. The new session starts with the task's title; the previous one changes it with `set_session_title` (worked on 2026-11-04). Create the task with `notifyOnCompletion` false: otherwise the session that created it gets a notice on every run and wakes up to reread the conversation.
   - **A session opened by a scheduled task starts without Remote Control and with medium effort.** The session that created the task, if it is still in its turn, checks in `list_task_runs` that it opened and adjusts both (`set_remote_control` and `set_session_effort`). The task's own session can't: while nobody opens it on screen, every action that needs approval is refused ("nobody has opened this scheduled run"). That included turning its own Remote Control on and creating another scheduled task, even with the allow rule (tested on 2026-11-04). So a successor opened by a task only opens the next one on a turn that came from a message by the person, or after the person opens it on screen; if it can't, it warns the person.
   - **Routines:** in the app, each scheduled task becomes a "routine". The session it opens appears only inside the Routines section of the sidebar, under the routine, not with the other sessions. If that section is turned off, the successor exists but the person doesn't see it. Check with `list_sections` (section `routines`, field `shown`). If it is off, ask the person to turn it on in the sidebar's filter menu: Claude can't (no tool turns the section on or moves the session out of it). Also, a one-time task turns itself off after it runs; once off, it and its session disappear from the Routines section when the session ends its turn (the session isn't archived, only hidden; seen on 2026-11-04). That is why the final message of the session that created the task always includes the new session's link.
5. **Test** (with the person's yes):
   1. Create a test folder, `~/Documents/successor_test/` (not in the config folder, which is protected), with a `HANDOFF.md` whose exact next step is: *"Create `ok.txt` with the word ok and write STAGE DONE on the first line of this handoff."*
   2. Open a session called "Successor test" with the request: *"Install test: don't archive or detach any session. Read and follow `<path>/HANDOFF.md`."* (Without that sentence, the close-the-previous rule could detach or archive this install session.)
   3. Check with `list_sessions` that it appeared. When it finishes, check that `ok.txt` exists. Tell the person they can archive the test session and delete the folder.

Rule text (question 1, one of the three):
> - **[Claude, on its own]** Successor: when it is time to switch sessions, I open the successor myself, without the person asking (`start_session`, initiation "user_asked", context "fresh", request "Read and follow <handoff>. Previous session: <id>" + the successor rules of this section; the <id> is this session's, found with `list_sessions` or `get_session`), tell the person in one line with the link, and stop. I don't open a successor if the handoff says STAGE DONE or has a question for the person that blocks the next step. Title = current title + number ("Site" → "Site 2"). I never end with "open a new session", and never leave a card waiting for a click. If the app refuses or turns it into a card: I use a scheduled task. If this session wasn't opened by a task and the manual-only task `successor-<project folder>` exists (`list_scheduled_tasks`), I rewrite `SUCCESSOR.md` in the folder with the same request and run the task right away (`run_scheduled_task`); otherwise (or if the app refuses to run it), I immediately create a one-time task for ~2 minutes later, with the same request. I check in `list_task_runs` that it opened; I adjust its title, Remote Control and effort (`set_session_title`, `set_remote_control`, `set_session_effort`), if I can; and I check with `list_sections` whether the sidebar's Routines section is on (the session only appears there): if it is off, I tell the person in one line where to turn it on. I always put the new session's link in my final message (a one-time task disappears from the sidebar after it runs). In a regular session (not opened by a task) in the folder of a project with a handoff, if the folder's manual-only task doesn't exist, I create it: no schedule, `notifyOnCompletion` false, title "Successor <folder>", request "Read `SUCCESSOR.md` in this folder and follow what it says." If that also fails: <screenless rounds, rule below | warn the person in one line>. When possible, I leave the switch for a turn that came from a message by the person.
> - **[Claude proposes]** Successor: at the switch, I update the handoff and propose the new session (card), with the request "Read and follow <handoff>".
> - **[I open it]** Successor: at the switch, I update the handoff and say in one line what to paste into the new session: "Read and follow <handoff>".

Rule text (question 2 "Yes"):
> - Close the previous one: the successor, right at the start, detaches from the session that opened it (`detach_session`), turns off the previous one's Remote Control (`set_remote_control` with its id and false) and archives the session whose id comes in "Previous session: <id>" in the request (`archive_session`). If it is refused, it tries again at the end of the first turn and at the start of every turn that comes from a message by the person, until it works; if the refusal mentions an agent or a background task, it doesn't force it: it says in one line that the person can archive it from the sidebar. Before opening the successor, the session stops the agents and background tasks that already delivered. It doesn't apply to a parallel session for another task (that one archives nobody).

Rule text (question 6 "Notify and carry on"; replace `<400>` with the Box 6 limit + 150k):
> - Notify and carry on: if the app refuses to open the successor (a turn that didn't come from a message by the person) or turns it into a card, I don't switch yet: I save the handoff, send `PushNotification` ("<title>: time to switch sessions, reply anything here") and keep working in this session. When a new message from the person arrives, before anything else I update the handoff and open the successor with `start_session`; its request says which agents are still running here and where each one saves its resume point. Then, here, I ask each running agent to finish its item and save its resume point (`SendMessage`), gather their summaries in the handoff and tell the successor (`SendMessage` with its id). The fallback in the successor rule (scheduled task, screenless rounds, warning) is kept for the ceiling only: the conversation passing ~<400>k tokens with no message from the person.

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
5. **Forbid reading the file.** In `settings.json`, under `"permissions"` → `"deny"` (create what is missing and don't delete what already exists), add the rule `"Read(<config folder>/relay_token.txt)"`, with the full path already filled in (no `~`). This way no session reads the file. Tell the person that the relay script already passes the same prohibition to the rounds.
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
   - To turn Path B off: delete `<config folder>/relay_token.txt`.

Rule text (Path B):
> - Screenless rounds: `python <config folder>/tools/session_relay.py --folder <project> --handoff <handoff> --model sonnet --rounds 3 --tools "<list>"`, launched detached in the background (Windows: `Start-Process ... -WindowStyle Hidden -PassThru`; Mac and Linux: `nohup ... &`), keeping the process number. Use: <when I am in the terminal | only as a fallback, when the app refuses to open a session>. It runs hidden: I warn the person in one line; at their next message, I check the project's `relay.log` and, if the handoff doesn't say STAGE DONE and nothing is running, I launch it again or open the successor. Long task: bigger `--timeout`. I never read, show or copy `relay_token.txt`.

---

## Box 8 — Spend watch and measuring

**What it is:** a script that runs by itself at every message and every tool used, and warns Claude when the session passes certain limits. Claude tells the person in one line and proposes what to do (update the handoff, open the successor, use a cheaper agent).
**Why:** nobody notices the conversation growing. In the author's use, 14 of 36 session switches only happened after 250k tokens, until the watch started warning in the middle of the turn.

Plan (Box 1): with "API key", don't ask questions 2 and 3 (there is no weekly %; spending shows up in money, in the API console) and don't put them under "Declined"; the spend watch (question 1) works the same, because it warns in tokens. With "Team or Enterprise" or "I don't know", ask both, but say they only work if the usage screen shows a weekly limit %; if, when reading it, there is no %, stop and tell the person.

Questions:

1. **Install the spend watch?** — header `Spend watch`
   - **Yes, author's limits (Recommended)** — Warns with the conversation at 200k tokens (and every 100k more), at 40, 80 and 150 prompts, and when an agent reaches 100 and 150 calls.
   - **Yes, warn earlier** — Conversation at 150k; agent at 60 and 100 calls.
   - **No**
2. **Check usage before and after a big task?** — header `Before/after`
   - **Yes (Recommended)** — Claude notes the plan usage % before a big task and says the difference at the end, in one line.
   - **No**
3. **Measure how much 1% of the quota is worth on your plan?** — header `Measure plan`
   - **Yes** — You note the usage % at two moments, with one or two days between them, and a script does the math. After that, the watch also warns in % of the quota.
   - **No** — The watch warns only in tokens.

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

Rule text:
> - Spend watch: when a "SPEND WATCH" warning appears, tell the person in one line, with the number, and propose what to do (handoff, successor, cheaper agent).
> - Before and after a big task: note the plan usage % and say the difference at the end, in one line.
> - Plan measuring: at the start of a session, if the last mark in `<config folder>/tools/measure_marks.csv` is more than a day old, read the weekly % and run `measure_point.py` with it. When the estimate gets stable over two or three calculations, propose putting the number in `POINT` in `spend_watch.py`.

---

## Box 9 — Checking the work

**What it is:** checking is mandatory, but you can check while spending less.

Question (just one, with several answers: `multiSelect: true`):

1. **Which of these habits become rules?** — header `Checking`
   - **Cheap proof** — When a text proves it (a log line, a value, test output), use the text. An image only cropped to what matters and at a smaller scale; measurements taken by script.
   - **Tests in parts** — After each change, the tests for what changed and a short regression; the whole suite before publishing.
   - **Two reviews, sensitive only** — Security, accounts, payment and cryptography get two independent reviews; the rest, one.
   - **Don't pay twice** — After an interruption, check whether agents and background tasks are still running and resume, instead of starting over. A process is ended only by the number (PID) that the session itself started, never by name.

Steps: save one line per checked item; the unchecked ones go to "Declined".

Rule text:
> - Cheap proof: text when text proves it; image cropped and at a smaller scale; measurements by script.
> - Tests: what changed + a short regression at every change; the whole suite before publishing. Tests and checks run by script, directly.
> - Review: two independent ones only for security, accounts, payment and cryptography; one for the rest.
> - After an interruption, check whether agents and tasks are still running and resume, don't start over. End a process only by the PID I started, never by name (it takes down other sessions' work).

---

## Final box — Summary

No questions. Tell the person, in a few lines:
1. What changed, by file (CLAUDE.md, settings.json, copied scripts), and where the backups are.
2. What was declined (it stays under "Declined" and is not offered again).
3. What only applies from the next session (settings and hooks).
4. How to undo everything: restore the backups from Box 1, delete the copied scripts and, if there is one, `<config folder>/relay_token.txt`.
5. What was left half done (for example, the second mark of the plan measuring). If the brake test or the spend-watch test was left for later, tell the person to open a new session and say there: "repeat the brake (or spend watch) test from the Quota Keeper guide".
6. The credit: "Tactics by Jaber Neto (JN Softworks), text under CC BY 4.0, scripts under MIT." If the person is going to share the guide, they should send the whole folder, with the credit.
