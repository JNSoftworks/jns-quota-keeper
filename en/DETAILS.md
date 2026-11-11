# JN's Quota Keeper — question details

> Made by Jaber Felippe Neto (JN Softworks). CC BY 4.0 license, like the guide.

This file holds the details of each question in `GUIDE.md`. The guide shows the summary; Claude reads the section here when the person asks for details (and the Path B steps, Box 7, when the person accepts the token). The person can also read it directly.

## Box 1

This box installs nothing: it keeps four answers that decide the rest. The change comes in its steps: a backup of `settings.json` and `CLAUDE.md` (each next to the original, with the date in the name) and a "Quota Keeper" section in `CLAUDE.md`.

### Box 1 · Save rules
- **What it does inside:** it only chooses which `CLAUDE.md` gets the rule lines: the config folder's (applies in every project) or the one in the folder open now. Settings, hooks and scripts always belong to the whole user, with either answer.
- **You gain:** with "all projects", the rules apply in any folder; with "only this project", they stay where you want.
- **Risks:** "all projects" makes every line be read in every session in any folder (a small but fixed cost). "Only this project" in a shared `CLAUDE.md` (in a repository) shows the lines to other people; the guide warns before saving.
- **If you skip it:** there is no "no": without this answer the rules have nowhere to live.
- **Undo:** delete the "Quota Keeper" section from the chosen file, or put the `CLAUDE.md.before-quota-keeper-<date>` copy back over it. Applies from the next session.
- **Skeptical reviewer's doubt:** "Does it touch my files?" Only the chosen `CLAUDE.md` (one section at the end) and `settings.json`, and only after a backup.

### Box 1 · Where used
- **What it does inside:** the desktop app has tools the terminal doesn't (open a visible new session, archive the old one, Remote Control). The answer decides whether Box 7 offers the app path, the terminal path or both.
- **You gain:** the guide doesn't offer what wouldn't work the way you use Claude Code.
- **Risks:** none; it only keeps the answer.
- **If you skip it:** "Terminal" skips the app parts; the new session then depends on the token (Path B) or on the rule where Claude only warns. The rest of the bundle works the same.
- **Undo:** nothing to undo. If you got it wrong, ask the question again.

### Box 1 · Plan
- **What it does inside:** only subscription plans (Pro, Max, Ultra) have a weekly limit in %. The parts that measure the quota (`Before/after`, `Measure plan`) and the long-lived token only make sense there.
- **You gain:** no useless part is offered; with "I don't know", the guide stays general.
- **Risks:** none. The guide never assumes the plan, not even from what a tool shows; only with your confirmation.
- **If you skip it:** with "API key" the %-of-quota parts are left out; everything else works, and the spend watch warns only in tokens.
- **Undo:** nothing to undo.

### Box 1 · Mode
- **What it does inside:** it chooses how the other boxes run. **Quick:** one screen with the tables of Group 1 (adopt), Group 2 (try and watch) and Group 3 (advanced, not turned on now); one ok installs Group 1, one box checks the Group 2 hooks. **Box by box:** one box per tactic. **Checking:** like the previous one, but before each write Claude shows the exact lines and you say `Write` or `Don't write`.
- **You gain:** Quick = fewer clicks; "checking" = you see what goes into each file.
- **Risks:** in Quick, Group 1 goes in with one ok: only rules in `CLAUDE.md`, two file templates and `"env"` settings (nothing approves, blocks or changes permissions). What is sensitive (permissions, automatic approval, sessions opened by themselves, Remote Control, token) is neither installed nor asked in Quick: it stays in Box 7.
- **If you skip it:** there is no "no". The mode only changes how I ask; the files written are the same for the same answers. Quick leaves all of Box 7 for later, on purpose.
- **Undo:** see "General risks and undoing everything" in the guide: put the backups back, or delete the `CLAUDE.md` section, the `settings.json` lines and the copied files.
- **Skeptical reviewer's doubt:** "Doesn't Quick install too much without me seeing?" It shows the bundle first (tables with risk and how to undo) and installs only after your ok; you can choose "See box by box" or "Cancel".

## Box 2

Three adjustments in `settings.json` (inside `"env"`) and one effort rule. Nothing here approves an action, changes a permission or sends data off the computer. The adjustments apply from the next session.

### Box 2 · Agents
- **What it does inside:** `CLAUDE_CODE_SUBAGENT_MODEL` = `sonnet` makes every agent start on Sonnet. When needed, Claude asks for Opus or Haiku for a specific agent (in old versions of Claude Code the setting overrode that request: if the model doesn't change, run `claude update`).
- **You gain:** an agent on Sonnet costs less than on Opus (Sonnet is the middle model between Haiku and Opus). The guide promises no savings percentage: it depends on how many agents you use.
- **Risks:** Sonnet gets hard tasks wrong more often than Opus (delicate code, math, security); that's why Claude asks for Opus in those cases. It approves nothing and nothing leaves the PC because of it.
- **If you skip it:** agents use the conversation's model. Everything works; if the conversation is on Opus, agents cost more.
- **Undo:** delete the `"CLAUDE_CODE_SUBAGENT_MODEL"` line in `"env"` of `settings.json` (or restore the Box 1 backup). Applies from the next session.
- **Skeptical reviewer's doubt:** "Can it cost more?" Only if you start many agents that wouldn't exist otherwise; the cheaper model itself doesn't raise the cost.

### Box 2 · Long waits
- **What it does inside:** `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` = `1h` keeps the agents' conversation stored for 1 hour instead of 5 minutes. The cache is the conversation stored to be reread more cheaply; after the time is up, storing it again costs again.
- **You gain:** an agent that waits more than 5 minutes (build, test, download, render) doesn't rewrite the whole conversation when it returns. On the author's machine those rewrites were ~26% of all the cost over 8 days (measured Sep-Nov 2026; your results may differ).
- **Risks:** writing to the 1-hour cache costs 2 times (instead of 1.25). If your agents almost never wait more than 5 minutes, you pay more with no gain. That's why the question comes first and "Yes" only fits people whose agents wait.
- **If you skip it:** the 5-minute cache stays. Everything works; long waits pay for the whole conversation again.
- **Undo:** delete the `"CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL"` line in `"env"`. Applies from the next session.
- **Skeptical reviewer's doubt:** "Is it worth it if I use few agents?" No: skip it (the question is only asked of people who use agents).

### Box 2 · Compaction
- **What it does inside:** `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` = `50` (or `25`) says when Claude Code replaces the conversation with an automatic summary: when it reaches that fraction of the space, instead of near the end. The numbers assume the 1-million-token window; with 200k the question isn't even asked.
- **You gain:** steps don't get expensive, because the conversation is already short when it would have become too big. No measured number here: it depends on how you work.
- **Risks:** the automatic summary loses detail of the conversation (more at 25% than at 50%). Anyone doing long production in a single session should keep this in mind.
- **If you skip it:** the default stays, near the end of the space; steps before the summary cost more; nothing breaks.
- **Undo:** delete the line in `"env"`. Applies from the next session.

### Box 2 · Effort
- **What it does inside:** it only saves one line of text in `CLAUDE.md`: recommend High effort, Max only for a very hard problem (preferably in an agent), and never open an agent-fleet mode unless you ask. The effort itself is yours, in the app's or the terminal's selector.
- **You gain:** Claude stops suggesting more expensive efforts and modes without need.
- **Risks:** almost none; it changes no setting.
- **If you skip it:** Claude may suggest more expensive effort or modes; you always decide.
- **Undo:** delete the line in `CLAUDE.md` (Quota Keeper section).

## Box 3

Only text rules in `CLAUDE.md`: no script and no permission. `CLAUDE.md` and the memory index come into every session before the first message and are reread at every step, so every line of them is paid for many times a day.

### Box 3 · CLAUDE.md
- **What it does inside:** the rule says to keep the file as rules and pointers; explanation and detail go to another file, cited in one line. With "Yes, and suggest cuts", Claude measures the file; if it is over ~200 lines or ~10 KB, it proposes a list of blocks to move (each with the pointer line that stays in its place) and moves only with your yes.
- **You gain:** less text paid for in every session. No percentage promised: it depends on the size of your file.
- **Risks:** a moved detail may be missed if Claude doesn't open the other file; that's why a pointer stays and nothing moves without a yes. The Box 1 backup keeps `CLAUDE.md` before anything is touched.
- **If you skip it:** the file stays as it is, may grow and cost more in every session. Nothing breaks.
- **Undo:** delete the rule's line; put the moved piece back into `CLAUDE.md` (the pointer says where it is), or restore the backup. Applies from the next session.

### Box 3 · Memory
- **What it does inside:** automatic memory has an index (`MEMORY.md`) read in every session, only up to line 200. The rule asks for one short line per note and, in a project with many notes, a summary note where new ones go. With "Yes", Claude shows how many lines and KB the index has and proposes shortening lines over ~150 characters, only with your yes.
- **You gain:** a short line fits more and costs less; nothing is cut after line 200.
- **Risks:** shortening a line may erase a useful detail. The Box 1 backup does NOT cover memory (only `settings.json` and `CLAUDE.md`): if memory matters, ask for a copy first.
- **If you skip it:** a long index is cut after line 200 and costs in every session; nothing breaks. With "I don't use memory" the part is skipped.
- **Undo:** delete the rule's line; put back the original text (from the copy you asked for).

### Box 3 · Chat style
- **What it does inside:** rule: between one tool and the next, just one line about what is being done; answers, results and warnings come together in the final message. Writing costs 5 times more than reading, and everything written stays in the conversation and is reread later.
- **You gain:** the conversation grows more slowly.
- **Risks:** you follow less of what Claude does in the middle of the work, and a warning only arrives at the end. For work where you want to see every step, answer "No".
- **If you skip it:** more detail along the way; the conversation costs more.
- **Undo:** delete the rule's line.

### Box 3 · Long text
- **What it does inside:** rule: long text or logs go to a file in the folder (you save it and give the name) instead of being pasted in the chat; Claude reads only the part needed.
- **You gain:** pasted text stays in the conversation forever and is reread at every step; in a file, only what is read comes in.
- **Risks:** one extra step for you (saving the file). Nothing leaves the computer because of this.
- **If you skip it:** pasting in the chat stays handy, but costs at every following step.
- **Undo:** delete the rule's line.

## Box 4

Only text rules in `CLAUDE.md` about how to read: no script and no permission. Everything Claude reads stays in the conversation and is reread at every following step. Example (computed with the guide's yardstick, not an official price): a 50k-token file read at the start weighs ~5k at every step after that; over 100 steps, ~560k. Read by an agent, it never enters the main conversation.

### Box 4 · Reading
One question with four habits; check the ones you want (each becomes a rule line; the unchecked ones go to "Declined").
- **Search instead of reading:** look for the name or title and read only ~50 lines around it; never read a big document, a log or a generated file in full. Risk: missing what was outside the part.
- **Big reads go to agents:** an agent reads and returns only the summary (Haiku to find and filter; Sonnet to understand). Risk: the summary may leave something out; the agent itself costs a new conversation.
- **Extract once:** when several tasks use the same big source, an agent writes a short note and the next ones read the note. Risk: the note goes stale if the source changes.
- **Filter logs at source:** mark the log's own lines and search only for the mark. Risk: an error without a mark doesn't show up.
- **You gain:** a smaller conversation, cheaper steps. No percentage promised: it depends on what you read.
- **If you check none:** everything is still read in full and costs more at every step; nothing breaks.
- **Undo:** delete the habit's line in `CLAUDE.md` (Quota Keeper section). Applies from the next session.
- **Skeptical reviewer's doubt:** "Will Claude stop seeing something important?" It can, with the search and summary habits; that's why the rule says to read in full only what is going to be edited, and the guide never skimps on reading the exact piece of code before changing it.

## Box 5

True for the whole box: questions 1 to 3 only save text in CLAUDE.md (they guide Claude, they block nothing). Questions 4 and 5 install Python scripts that Claude Code runs before each tool use. Those scripts can only DENY an action; they never approve anything and skip no permission prompt. If the script fails on its own error, it lets everything pass (the protection disappears, nothing gets stuck). If Python doesn't exist or the path is wrong, Claude Code shows the hook error and carries on (on Windows the command may be `py` instead of `python`; check in the terminal). No script uses the network. Both read internal files of Claude Code (the conversation's list of agents), which may change in an update: then they stop protecting, without blocking anything by mistake.

### Box 5 · Short agent

- **Inside:** a CLAUDE.md rule makes the request of every agent that edits or fixes say "when you reach ~100 calls, finish the item, write the resume point in a file and return the summary". If work is left, the main conversation opens another agent from that file.
- **What you gain:** an agent rereads its own conversation at every step, so it gets expensive if it works long. In the author's use, agents with 100 or more calls were 74% of the agents' cost, and 71% of that cost came from steps where the agent's conversation was above 200k tokens (measured on the author's machine, Sep-Nov 2026; your results may differ).
- **Risks:** (1) an interrupted agent may leave the task half done; (2) opening the next one costs one more read of the resume file; (3) the work is split across more agents. All small and visible: nothing is deleted, the resume point sits in a file.
- **If you skip it:** agents keep going with no size limit. The extra "[Only with 1-hour cache]" line (maximum wait of ~50 min) and "Opus coordinates" in the Models question (pieces of ~80 calls) were designed around this limit and lose their basis; the rest of the bundle works the same.
- **Undo:** delete this box's lines from CLAUDE.md. Takes effect next session.
- **Skeptical reviewer:** "does this change permissions?" No, it is only text. "Does it cost more?" It may cost a little more in rereads of the resume file; the aim is to avoid the long agent, which costs more.

### Box 5 · Models

- **Inside:** "By role" saves a rule: Sonnet by default; Haiku for the mechanical (finding a file, filtering a log, counting); Opus only for an agent that edits delicate code (security, accounts, money, cryptography). "Experimental: Opus coordinates" adds that, for new code or a fix outside security, accounts and cryptography, an Opus agent writes the request for each piece and opens Sonnet agents one at a time (~80 calls each; Sonnet opens no agents), runs the tests by script, reviews only what changed and fixes it; a piece that fails twice, Opus does. Each case is noted in `~/Documents/opus_sonnet_pilot.md` and, after ~6, Claude asks whether it becomes the default.
- **What you gain:** mechanical work runs on a cheaper model. This guide has no saving figure for "By role"; for "Opus coordinates" there is no proven saving yet: it is being tested on the author's machine.
- **Risks:** (1) the cheaper model errs more on a task that looked simple; (2) "Opus coordinates" uses more steps and more agents and may cost more than doing it directly; (3) the pilot file sits in `~/Documents`, outside the config folder, as plain text.
- **If you skip it ("Don't change"):** you pick each agent's model by hand. Nothing else stops working. Without the brake (Brake question), "Opus coordinates" is held only by the text rule that Sonnet opens no agents.
- **Undo:** delete the line from CLAUDE.md; delete `~/Documents/opus_sonnet_pilot.md` if you want.
- **Skeptical reviewer:** "does this get around any permission?" No; it only guides which model to use.

### Box 5 · Batching

- **Inside:** CLAUDE.md rule: one agent per task (not one per tiny piece); several at the same time go out in the SAME message; each one writes the detail in a file and returns 5 to 10 lines.
- **What you gain:** fewer open agents and short answers that the main conversation rereads at every step.
- **Risks:** the short answer hides detail; it is in the file, but you have to open it. Several agents at once spend in parallel.
- **If you skip it:** agents return long answers and may be opened in small pieces. Nothing else stops working.
- **Undo:** delete the line from CLAUDE.md.

### Box 5 · Brake

- **Inside:** copies `agent_limit.py` to the `hooks/` folder and registers it under `"PreToolUse"` with `matcher` `Agent|Task` (both names because old versions called the tool `Task`). Before each agent is opened, the script denies if the opener is already a level-2 agent or more, or already has 6 children.
- **What you gain:** it prevents endless chains of agents opening agents.
- **Risks:** (1) it may deny an agent you wanted; the message "Agent limit: ..." says why; (2) if Claude Code changes the internal file the script reads, the brake stops braking; (3) it only DENIES, never approves: no permission prompt is skipped.
- **If you skip it:** endless chains stay possible. "Opus coordinates" is held only by the text rule.
- **Undo:** delete from `settings.json` the entry that calls `agent_limit.py` under `"PreToolUse"` (or restore the backup from Box 1) and delete the file in `hooks/`. Takes effect next session.
- **Skeptical reviewer:** "what if Python doesn't exist?" Claude Code shows the hook error and carries on; the work doesn't get stuck.

### Box 5 · Copy lock

- **Inside:** copies `copy_lock.py` to `hooks/` and registers it under `"PreToolUse"` (matcher `Bash|PowerShell|Edit|Write|NotebookEdit|MultiEdit|Agent|Task`) and under `"SubagentStop"`. When an agent writes in a working copy (a folder with `.git`, `.p4config` or a `.uproject`), its session takes that folder. Another session can't write, run a command that writes, or launch an agent there until those agents finish. Reading, and editing `.md` and `.txt` notes, always pass. Only agents take the lock (the main conversation's own edits don't), and agents of the same session share it.
- **What you gain:** two sessions don't write in the same folder at once, for example after a session switch with an agent still running.
- **Risks:** (1) a lock stuck by mistake keeps the other session from writing in that folder; (2) the script writes small files in `<config folder>/locks` and a log in `<config folder>/hooks/copy_lock.log`; (3) it only DENIES, never approves. The lock goes away when the last agent of that session returns with nothing running in the background, when the owner session is closed or archived, or after 2 hours with no sign.
- **If you skip it:** two sessions can touch the same folder and get in each other's way. The session switch with an agent still running (Box 7) checks the handoff instead of the lock.
- **Undo:** delete from `settings.json` the `copy_lock.py` entries under `"PreToolUse"` and `"SubagentStop"` (or restore the backup from Box 1) and delete the file in `hooks/`. Stuck lock right now: `python <config folder>/hooks/copy_lock.py release <folder>`. See the locks: `... copy_lock.py list`.
- **Skeptical reviewer:** "what does it block?" Only writing, commands that write and opening agents, in a folder that an agent of ANOTHER session is using. Everything else passes.

## Box 6

True for the whole box: the numbers (switch at ~250k) assume the 1-million-token window; with a 200k window, the switch is at ~100k. The handoff and summaries files live in the project folder, as plain text; nothing leaves the computer because of them.

### Box 6 · Handoff

- **Inside:** on a project's first multi-stage task, Claude creates `HANDOFF.md` by itself (what was done, what is half done, the exact next step) and, with "Yes, handoff + summaries", also `SUMMARIES.md` (one entry per session: Did / Decided / Open), from templates copied to `<config folder>/templates`. If the project already has such a file, it uses that one. It notes the steps when each part is finished and, at every session switch and end of stage, appends an entry to the summaries.
- **What you gain:** it was the author's biggest saving: the main conversation fell 75% after this rule (measured on the author's machine, Sep-Nov 2026; your results may differ). The automatic summary (compaction) loses detail; the file doesn't. The summaries let you find later which session did something.
- **Risks:** (1) new files appear in projects without asking each time (in a repository, in `git status`; to avoid versioning them, use `.gitignore`); (2) if the folder is published (repository, cloud), the handoff goes with it: don't write passwords, tokens or personal data in it; (3) an old or wrong handoff makes the new session start from the wrong point: Claude checks the "next step" before acting and asks for confirmation on irreversible actions, but look at the file if the new session seems lost; (4) switching sessions costs one read of the handoff and loses what lived only in the conversation.
- **If you skip it:** a new session starts without a handoff file and loses what lived only in the conversation. The Switching and Reminder questions and all of Box 7 (automatic successor) lose their point and are skipped. "Handoff only" keeps the handoff but with no summaries file.
- **Undo:** delete this box's lines from CLAUDE.md (takes effect next session). Files already created stay; delete them by hand if you want.
- **Skeptical reviewer:** "does Claude write to disk by itself?" Yes, only these two text files, inside the project. Claude Code's permission prompts still apply.

### Box 6 · Switching

- **Inside:** CLAUDE.md rule: with the conversation at the chosen number (~200k, ~250k or ~300k tokens) or at a new stage, Claude finishes the part in progress, updates the handoff and switches sessions. With no successor rule, it tells the person in one line what to paste into the new session. "Only when I ask" just warns in one line.
- **What you gain:** every step rereads less. In the author's numbers (260 sessions), the total cost barely changes between 200k and 300k, and above ~300k every step rereads so much that it costs more (measured on the author's machine, Sep-Nov 2026; your results may differ).
- **Risks:** (1) each switch loses a little of what the conversation knew; (2) switching late costs more; (3) the new session rereads the handoff (small next to staying in a huge conversation).
- **If you skip it ("Only when I ask"):** nothing switches by itself; the conversation can get expensive if you forget. The automatic successor (Box 7) has no trigger.
- **Undo:** delete the line from CLAUDE.md.

### Box 6 · One task

- **Inside:** rule: a new subject, unrelated to what is open, goes to a new session (or `/clear`, which only the person can type).
- **What you gain:** short, focused conversations, which cost less per step.
- **Risks:** more open sessions for you to keep track of.
- **If you skip it:** different subjects pile up in the same conversation, which gets big and expensive. Nothing else stops working.
- **Undo:** delete the line from CLAUDE.md.

### Box 6 · Reminder

- **Inside:** copies `handoff_reminder.py` to `hooks/` and registers it under `"SessionStart"` (matcher `startup`). If the opened folder has a `PASSAGEM*.md` or `HANDOFF*.md`, the script shows Claude one line telling it to read that file first. It only lists the folder: it reads no file, writes nothing, uses no network, approves and blocks nothing.
- **What you gain:** Claude doesn't forget to read the handoff when the folder opens.
- **Risks:** one extra line at the start of each session in those folders. If the script fails or Python doesn't exist, Claude Code shows the error and the session carries on normally.
- **If you skip it:** the CLAUDE.md rule already says to read the handoff, but without the reminder Claude may forget. Nothing else stops working.
- **Undo:** delete from `settings.json` the `"SessionStart"` entry that calls `handoff_reminder.py` (or restore the backup from Box 1) and the file in `hooks/`. If there is another item under `"SessionStart"` (such as the Box 8 daily report), delete only this one. Takes effect next session.
- **Skeptical reviewer:** "what if Python doesn't exist?" Claude Code shows the error and carries on. Check with `handoff_reminder.py --test` (the last line must be `ALL OK`).

## Box 7

(Details for Box 7's questions. Each one's summary is in the guide; here is what it does inside, what you gain, each risk, what keeps working without it and how to undo it.)

### Box 7 · Overview and undoing everything

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

### Box 7 · Questions a skeptical reviewer would ask

**Questions a skeptical reviewer would ask, with straight answers:**
- **Does `spare_allow.py` get around permissions?** It skips one thing only: the approval prompt (and the auto mode filter) for six tools, and only when the target is an id listed in `spares.txt`: `SendMessage` (message to the session) and, in the app, unarchive, change title, change model, change effort and turn Remote Control on or off. It doesn't read the message text. Everything else follows the normal flow and still asks for approval or goes through the filter: opening a session (`start_session`), archive, detach, delete, stop, changing another session's permission mode, and any action on a session that isn't on the list. Deny rules, according to the Claude Code documentation, still apply (the author didn't test this). Two caveats: a message to a spare is an order to another session, which then acts with its own permissions; and if the id stays in `spares.txt` after the spare became a working session, those six actions stay approved on it (Claude removes the id after using the spare; check the file now and then). Every decision goes to `hooks/spare_allow.log` (time, tool and id, no message text; the file isn't cleaned automatically).
- **What if the hook fails (Python missing, an error, going past 10 s)?** Nothing is approved: per the Claude Code documentation, a hook that fails neither blocks nor approves, and the action follows the normal flow (asks for approval or goes to the filter). Only convenience is lost: the spare may be blocked and the switch falls back to "Notify and carry on". The author didn't test it by removing Python.
- **Does auto mode (`"defaultMode": "auto"`) let Claude act without asking about what?** Instead of asking for your OK on each action, a filter judges each one: it lets through what looks safe and routine (reading and editing project files, common commands) and blocks what looks risky or beyond what you asked. It can be wrong both ways. It is not the mode that ignores all permissions (the guide doesn't use that one), and deny rules still apply. It applies to every new session the person opens, in any project.
- **Token in a file: who can read it, how to delete and revoke?** `relay_token.txt` sits in the config folder. On Windows the guide leaves only the person's user with access; on Mac and Linux, only the owner (mode 600). Even so, any program that runs as the person, computer administrators, and backups or cloud sync that take the folder can read it. Claude doesn't read it (a deny rule on reading, which covers the read tool but is no guarantee against a terminal command). To delete: delete the file. To revoke: the official documentation (checked in November 2026) doesn't show how to revoke just this token; look at the list of access and sessions in the account settings on claude.ai or contact Anthropic support. The token lasts one year.
- **Can this cost more?** Yes. Each new session (successor, spare, scheduled task) starts with an empty conversation but reloads instructions and memory and reads the handoff, and its first use doesn't benefit from what the previous one already had in cache. In exchange, it avoids the cost of continuing in a very large conversation. "Notify and carry on" and a conversation that goes past the limit with no reply cost the opposite: each step in a large conversation costs more. The screenless rounds use the same quota. No author number for the total.
- **Does data leave the computer?** The package's scripts make no network calls. What runs in Claude (including the screenless rounds, which call the `claude` command) sends the conversation to Anthropic, like any use of Claude. Remote Control shows the conversation in the person's claude.ai account and on their devices.

### Box 7 · The app's traps

What the author found while testing (November 2026). The guide's rules already handle each one; this explains why.

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

### Box 7 · Successor

**What it does inside:** At the switch (Box 6 rule), Claude saves the handoff and calls `start_session` with the request "Read and follow <handoff>. Previous session: <id>" plus this section's rules (inheritance); the new session reads the handoff and does the "exact next step". With the first option Claude also saves the "Switch with an agent running" rule.

**What you gain:** The stage doesn't stop waiting for you: the author had a stage stopped all night waiting for a click (the author's account, no number).

**Real risks:** the new session starts without you looking and may be hidden (see "Routines" in the traps); each new session reloads the instructions and reads the handoff again, which may use more quota than staying in one conversation; the chain only stops when the handoff says the stage is done or has a question for you. With the first option Claude also saves the "Switch with an agent running" rule.

**If you skip it (what works and what doesn't):** "Claude proposes, I click" and "I open it" work: nothing opens on its own, the work waits for you. In both, questions 2 and 5 to 10 make no sense and are skipped. Handoff, summaries, session switching and the watch stay as they are.

**What protects the context in the succession:** the handoff and the summaries (Box 6) keep what was done and the next step; the successor's initial request tells it to read the handoff and repeats the rules; the handoff is updated before the new one opens. **The risk that remains:** a badly written handoff (the new one starts from the wrong point; what was only in the conversation is lost) and archiving something still alive, which the rule already doesn't force when an agent or background task exists.

**How to undo:** delete from `CLAUDE.md` the lines "Successor:", "Switch with an agent running:" and "Inheritance"; archive in the sidebar the sessions it opened. Applies from the next session.

### Box 7 · Close old

**What it does inside:** The successor, right at the start, detaches from the session that opened it, turns off its Remote Control and archives it by the id in the request. The title gets a number ("Site" → "Site 2").

**What you gain:** Each end of turn of the new one would wake the previous one, which would reread the whole conversation; archived, it costs nothing.

**Real risks:** archiving doesn't delete the conversation (it leaves the normal list and comes back from the archived list); if Claude got the id wrong it would archive the wrong session, which is why the id comes in the request ("Previous session: <id>") and the rule doesn't apply to a parallel session for another task. The successor also turns off the previous one's Remote Control and detaches from it. In the "Switch with an agent running" rule, the previous session archives itself when its last agent returns.

**If you skip it (what works and what doesn't):** Both sessions stay open and the previous one may reread the whole conversation at every turn of the new one (uses quota) until you archive it. The rest of the box works. In the "Switch with an agent running" rule, remove the part where the previous one archives itself.

**How to undo:** delete the "Close the previous one:" line from `CLAUDE.md`; to bring a session back, unarchive it from the archived list.

### Box 7 · Token

**What it does inside:** You generate the token with `claude setup-token` in a system terminal window and save it in a file (steps in Path B); the `session_relay.py` script reads the file and hands it only to the `claude -p` rounds. Claude never sees the token.

**What you gain:** The chain moves on by itself in the terminal, with no screen and no app, with an empty conversation each round.

**Real risks:** the token is an access key to the person's Claude account, valid for one year: whoever has it uses their quota. It lives in `<config folder>/relay_token.txt`; the guide restricts the file to their user, but any program that runs as them, administrators, and backups or cloud sync that take the folder can read it. Claude never sees the token. The rounds run with nobody watching and use the same quota.

**If you skip it (what works and what doesn't):** **Works without it:** Path A in the app (if `start_session` exists), the "[I open it]" rule (Claude updates the handoff and tells you), spares, "Notify and carry on" and the scheduled task. **Stops working:** in the terminal, the chain of sessions doesn't move on its own; and the "screenless rounds" fallback disappears from Path A (it falls back to a warning to you). Handoff, summaries, switching, the watch and the rest of the package don't depend on the token.

**Why a file, and not a system variable** (`setx` on Windows, `export` in the terminal profile): the token would apply to every `claude` opened on that account of the computer, and the normal login (`/login`) would stop working until the variable is removed. In the file, it is read only by the script and handed only to the rounds.

**How to undo:** delete `relay_token.txt`, `tools/session_relay.py` and the "Screenless rounds:" rule; remove from `settings.json` the line `Read(.../relay_token.txt)` (optional). To revoke, see "Token in a file" above and the end of Path B.

### Box 7 · Permissions

**What it does inside:** Sets the script's `--tools`: the list of tools a hidden round may use. Nothing outside the list runs; nobody is asked.

**What you gain:** Limits the possible damage of a round nobody is watching.

**Real risks:** no round asks for approval: what is on the list goes straight through and the rest is refused. Even with files only, a wrong round can edit or overwrite project files without you seeing (use git or a copy).

**If you skip it (what works and what doesn't):** Without the token the question doesn't even exist. With the token, the list is required; "Files only" is the smallest.

**How to undo:** 

### Box 7 · Scheduled

**What it does inside:** Adds two allow rules to `settings.json`: create and run a scheduled task. The task is the visible fallback for when the app refuses to open the session; it is created only at the first switch where spares and "Notify and carry on" are not enough.

**What you gain:** A successor opened with a single command, within seconds, even on an automatic turn (tested on 2026-11-04 on the author's machine).

**Real risks:** adds two rules under `"permissions"` → `"allow"` in `settings.json`: create and run a scheduled task without asking for approval. They apply to ALL sessions and projects, not only the successor; a session misled by malicious text (on a page or in a file) could schedule something that runs later with nobody watching, in the default permission mode and under the deny rules. The task is only created at the first switch where spares and "Notify and carry on" are not enough.

**If you skip it (what works and what doesn't):** The fallback becomes screenless rounds (if installed) or a warning to you; question 9 (auto as default mode) is skipped, since it only serves the task. The allow rules apply to all sessions of the account.

**How to undo:** remove from `"allow"` the lines `"mcp__scheduled-tasks__create_scheduled_task"` and `"mcp__scheduled-tasks__run_scheduled_task"`; delete the `successor-<folder>` task (see "How to undo" at the top of the box). Applies from the next session.

### Box 7 · Refused

**What it does inside:** Chooses what Claude does when the app refuses to open the new session (a turn that didn't come from a message by you): use spares, notify and carry on, or go straight to the fallback.

**What you gain:** The switch doesn't get stuck when the app refuses.

**Real risks:** "Spare session" creates reserve sessions without you seeing them (see question 7) and later archives and reactivates them; "Notify and carry on" lets the conversation grow until your next message, and each step in a large conversation uses more quota; "Fallback right away" may leave the successor hidden in Routines.

**If you skip it (what works and what doesn't):** There is no "no" here: the minimum is "Notify and carry on", which creates no session before your message. Without "Spare session", questions 7 and 10 are skipped.

**How to undo:** delete from `CLAUDE.md` the lines "Spares:" and "Notify and carry on:"; delete the spares (see "How to undo" at the top of the box).

### Box 7 · Spares

**What it does inside:** Spares are empty, archived sessions that Claude unarchives, renames and uses at the switch. The rule checks the folder at every message from you and refills the used ones up to the chosen number.

**What you gain:** Switching with you away from the screen, in the normal session list (the scheduled task stays hidden in Routines).

**Real risks:** Claude creates up to that number of empty sessions in the folder, without you seeing, and refills the used ones on each message from you. Each uses a short turn when created (it reloads the instructions and replies "ready"); archived, it costs nothing. They fill the archived list. The author has no measured number for the total cost.

**If you skip it (what works and what doesn't):** With fewer spares (6), a night with many switches in the same folder may run them out; then it falls back to "Notify and carry on". The cost: one short turn per spare when created.

**How to undo:** 

### Box 7 · Remote

**What it does inside:** Turns on Remote Control: the session becomes reachable through the person's claude.ai account, on the phone or in a browser. The rule turns it on in successors; "Turn on now" also turns it on in this session. Before turning it on or off, Claude checks the state with `get_session` (calling it needlessly can open an approval box or turn off what you wanted on).

**What you gain:** Follow and send messages from afar; it is what makes the alert reach the phone.

**Real risks:** anyone who gets into their claude.ai account, or picks up their unlocked phone, can send orders to the session, which runs on their computer with the session's permissions (files and commands); so, two-step verification on the account and a locked phone. The conversation also shows on those other devices. And a session open through Remote Control counts as "live work": the app won't archive it, which is why the successor turns the previous one's off before archiving.

**If you skip it (what works and what doesn't):** Everything works without it; the "Notify and carry on" alert only shows on the computer. Claude still turns off the previous session's Remote Control before archiving it, if it is on. If you suspect unwanted access to the account: change the password and sign out of connected devices.

**How to undo:** delete the "Remote Control:" line from `CLAUDE.md`; turn it off in each session (`set_remote_control` with false, or the session's menu) and turn off, in the app settings, the option that turns it on in every new session. If you suspect unwanted access to the account, change the password and sign out of connected devices in the account settings.

### Box 7 · Auto default

**What it does inside:** Stores `"defaultMode": "auto"` under `"permissions"` in the user's `settings.json`. Reason: a scheduled task doesn't inherit the mode of the session that created it; without this the successor stops at the first command. It needs a recent Claude Code version and a plan with auto mode; without them the session starts in normal mode.

**What you gain:** The task's successor works on its own, without waiting for you.

**Real risks:** it applies to EVERY new session, in every project, not only the successor: instead of you approving each action, a filter decides (it lets through what looks safe and routine, blocks what looks risky) and can be wrong both ways. It doesn't ignore permissions, and deny rules still apply. It needs a recent Claude Code version and a plan with this mode; without them the session starts in normal mode.

**If you skip it (what works and what doesn't):** The default mode stays as it is. The successor opened by the task starts in normal mode and stops at the first command or edit, waiting for you to approve. (The app says each routine keeps the approvals given and reuses them in the next runs; the author didn't test it.)

**How to undo:** remove `"defaultMode": "auto"` from `"permissions"` (or put back the value the Box 1 backup shows). Applies from the next session.

### Box 7 · Spare hook

**What it does inside:** Copies `scripts/spare_allow.py` to `<config folder>/hooks/`, creates an empty `spares.txt` and registers a block under `"hooks"` → `"PreToolUse"`. The hook approves only when the target is an id listed in `spares.txt`. It logs each decision in `hooks/spare_allow.log` (time, tool, id; no message text).

**What you gain:** Switches through spares go through without a box; without it auto mode blocked changing a spare created by another session, and sometimes the message with the task, judging it a way around the `start_session` lock (seen on 2026-11-04). With the hook, a session did all of this on a spare it hadn't created, with no box at all (tested the same day). Don't use allow rules for these tools: they would apply to every session.

**Real risks:** it approves on its own only six actions (message, unarchive, title, model, effort and Remote Control) and only on a session whose id is in `spares.txt`; it doesn't read the message text; if it fails, it approves nothing. Details in the answer "Does `spare_allow.py` get around permissions?" at the top of the box. It logs everything in `hooks/spare_allow.log`, on your computer.

**If you skip it (what works and what doesn't):** Nothing is approved on its own. Auto mode may block changing a spare or the message with the task; the switch falls back to "Notify and carry on" or you approve in the box.

**How to undo:** remove from `"hooks"` → `"PreToolUse"` the block with `matcher` `SendMessage|mcp__ccd_session_mgmt__.*` and delete `hooks/spare_allow.py`, `hooks/spare_allow.log` and `spares.txt`. Applies from the next session.

### Box 7 · Screenless rounds and prior warning

**What it does inside:** `session_relay.py` runs `claude -p` in rounds (each with an empty conversation, reading and updating the handoff) and stops when the handoff says STAGE DONE, at the round limit or at the time limit. It doesn't appear in the app. Each round is logged in `<config folder>/quota_keeper/relay_log.jsonl` (`start`, `round`, `end` lines, with time, folder, model, reason and whether a warning was given; the token never goes in). An error writing this record is ignored and never stops the relay.

**The warning rule:** before opening any hidden session, Claude warns the person in one line (what will run, why, how many rounds, that it uses their quota) and launches with `--reason "<reason>" --notified`. Without `--notified`, the daily report (Box 8) marks the round as "without a recorded warning".

**What you gain:** no hidden session uses quota without you knowing; and the daily report can tell an announced round from a screenless session nobody announced.

**If you decline screenless rounds (question 3, "Not now"):** in the terminal the chain of sessions doesn't move on its own (Claude updates the handoff and tells you to open the new one); in the app, Path A covers it. The rest of the package works. Without the token, `session_relay.py` isn't even copied.

**Script limits:** a round that goes past the time limit (`--timeout`, default 1 hour) is cut and the relay stops (a long task needs a bigger `--timeout`); the script also stops at the round limit even if the last one says CONTINUE. Nothing is approved on its own: the round only uses the tools on the list chosen in question 4; the rest is refused, with no question.

**Risks that remain:** the round uses the same quota; a wrong round can edit project files (use git); the record only sees rounds launched by the script, not another program that uses `claude -p` on the same PC.

**How to undo:** delete `tools/session_relay.py`, `relay_token.txt`, the "Screenless rounds:" rule and, in each project, `relay.log`; `quota_keeper/relay_log.jsonl` can be deleted at any time (it is created again on the next round).

**Daily report:** whoever chooses the token or screenless rounds should get the daily report offer; the question belongs to Box 8. Among other things, it shows screenless sessions opened without a recorded warning and screenless sessions running for a long time. Honest limit: it only sees this computer.

### Box 7 · Token (revoking and turning off)

- **Revoking:** the official documentation (checked in November 2026) doesn't show how to revoke only this token. Look in the account settings on claude.ai for the list of accesses and sessions, or contact Anthropic support. Deleting the file doesn't revoke it; the token lasts one year. If it leaked, treat it as a leaked password.
- **Turning Path B off:** delete `<config folder>/relay_token.txt` (without it the script doesn't run), `<config folder>/tools/session_relay.py` and, in each project, `relay.log`; remove the "Screenless rounds:" rule from `CLAUDE.md` and, from `settings.json`, the line `Read(.../relay_token.txt)` under `"deny"` (optional).

### Box 7 · Path B steps

Only if question 3 was "Yes, guide me". One step at a time, waiting for the person to say they did it.

**What the token is** (say it like this): an access key to their Claude account, valid for one year, made for scripts. Whoever has it uses their quota; it is like a password.

1. **Check the terminal Claude Code:** `claude --version`. If it doesn't exist, the person installs it (https://code.claude.com/docs). The token works on the Pro, Max, Ultra, Team and Enterprise plans.
2. **The person generates the token.** You don't run this command (it opens the browser and shows the token). They run, in a system terminal window they open themselves outside this conversation:

   ```text
   claude setup-token
   ```

   **Never** in the terminal panel of the Claude app nor in the code editor's terminal: Claude reads those panels, and the token would end up in the conversation.

   They log in in the browser, the terminal shows the token, and they copy it without pasting it anywhere yet, not even in the chat.
3. **The person saves the token in a file**, in the same window, with the token still copied. The commands assume the default folder (`.claude` in the home folder); if the config folder is another, change the path (and use `--token-file` in the script, if it doesn't find the file):
   - Windows (PowerShell):

     ```powershell
     Get-Clipboard | Out-File -NoNewline -Encoding ascii "$HOME\.claude\relay_token.txt"
     icacls "$HOME\.claude\relay_token.txt" /inheritance:r /grant:r "$($env:USERDOMAIN)\$($env:USERNAME):F"
     icacls "$HOME\.claude\relay_token.txt"
     ```

     (The second line leaves only their user able to read the file; the third shows the permissions: only their user should appear.)
   - Mac and Linux: they run the command, paste the token (it doesn't show on screen) and press Enter:

     ```bash
     umask 077; read -rs T; printf %s "$T" > <config folder>/relay_token.txt; unset T
     ```

   Then they clear the clipboard and close the window: copy something else (Windows: and delete the token's item in the clipboard history, Win+V, if on; Mac: the universal clipboard carries what was copied to their other Apple devices).

   Save it in a file, never in a system variable (`setx`, `export`); reason: `en/DETAILS.md`, "Box 7 · Token".
4. **Check without seeing the token** (prints only yes or no):

   ```text
   python -c "import os, pathlib; t = (pathlib.Path(os.environ.get('CLAUDE_CONFIG_DIR') or pathlib.Path.home() / '.claude') / 'relay_token.txt').read_text(encoding='utf-8-sig').strip(); print('ok' if t.startswith('sk-ant-') and not any(c.isspace() for c in t) else 'check the file: it must have only the token, one line')"
   ```

   Never run `cat`, `type` or `Get-Content` on that file, and never open it with Read. If the config folder is inside a git repository or a cloud-synced folder, warn them: the token can't go along (`relay_token.txt` in `.gitignore` or out of the sync).
5. **Forbid reading the file.** In `settings.json`, under `"permissions"` → `"deny"` (create what is missing, don't delete what exists), add `"Read(<config folder>/relay_token.txt)"`, with the full path (no `~`). This covers the read tool, not a terminal command (hence never `cat`). Say that the script already passes the same prohibition to the rounds.
6. **Copy the script:** `scripts/session_relay.py` → `<config folder>/tools/session_relay.py`.
7. **Test in a toy project** (with the person's yes; two or three quick rounds on Haiku, a little quota). The folder is in `~/Documents`, not the config folder: there the rounds can't write (protected, and a round can't ask for permission).
   1. Create `~/Documents/relay_test/HANDOFF.md` with:

      ```markdown
      # Handoff — relay test

      ## Exact next step
      If `count.txt` doesn't exist, create it with the line "one". If it already exists with "one", add the line "two" and write STAGE DONE on the first line of this handoff.
      ```
   2. Run (full path of `tools/session_relay.py`; on Windows, `/` slashes):

      ```text
      python <config folder>/tools/session_relay.py --folder ~/Documents/relay_test --handoff HANDOFF.md --model haiku --rounds 3 --reason "install test" --notified
      ```
   3. Expected: round 1 creates "one" (STATUS: CONTINUE); round 2 adds "two" and writes STAGE DONE; the script stops by itself. The record is in `~/Documents/relay_test/relay.log`, one line per round.
   4. Unknown-option error: the person updates Claude Code (`claude update`) and you try again. On Windows, odd-arguments error: pass `--claude "<path to claude.exe>"` (`claude.cmd` mangles arguments with parentheses and asterisks).
8. **Save the rule** for Path B with the tools from question 4:
   - "Files only": `--tools "Read,Glob,Grep,Edit,Write"` (the script's default).
   - "Files + terminal": add the name of the terminal tool in the person's tool list (`Bash` or `PowerShell`; don't assume it from the system), e.g. `--tools "Read,Glob,Grep,Edit,Write,PowerShell"`.
   - "Decide per project": the rule says to ask the first time in each project and note the answer in that project's CLAUDE.md.
9. **Tell the person the gaps** (the rule already covers the warning, `relay.log` and the quota): a round that goes past `--timeout` (default 1 hour) is cut and the relay stops (a long task needs a bigger `--timeout`); the script stops at the round limit even if the last one says CONTINUE; the round only uses the tools on the question 4 list. A leaked token is a leaked password: revoking and turning Path B off are in `en/DETAILS.md`, "Box 7 · Token (revoking and turning off)"; limits and risks, in "Box 7 · Screenless rounds and prior warning".

## Box 8

True for all five questions: no script in this box uses the network; none blocks or approves a Claude Code action (the hooks only print a warning); all use only Python's standard library. If Python doesn't exist, the hook gives a command-not-found error, Claude Code shows it and carries on.

### Box 8 · Spend watch

**Inside:** `spend_watch.py` runs at every message (`UserPromptSubmit`) and every tool (`PostToolUse`). It reads only what is new in the session record (`<config folder>/projects/.../*.jsonl`), adds up tokens, and when a limit is crossed (conversation at 200k and every 100k more; 40, 80 and 150 prompts; agent at 100 and 150 calls) it prints a "SPEND WATCH" line that enters the context. Claude tells the person and proposes a handoff, a successor or a cheaper agent. It writes only `hooks/spend_watch_state/` (one small file per session, with what it already warned).

**What you gain:** the warning arrives mid-turn, not only at the end. In the author's use, 14 of 36 session switches only happened after 250k tokens, before the watch warned this way (measured on the author's machine, Sep-Nov 2026; your results may differ). A big conversation is what raises cost most, because every step rereads it all.

**Risks:**
- It reads the local records, which contain the whole conversations. It only counts tokens, model and time; it copies no content and nothing leaves the computer.
- If the record format changes in a Claude Code update, it goes silent or the hook shows an error. It blocks and approves nothing.
- Cost: one line in the context, a few times per session. The watch itself runs at every message and tool (one Python start, tens of milliseconds on a roomy PC; more on a loaded one).
- "Warn earlier" gives more warnings (more context lines), in return for switching sessions sooner.

**If you skip it:** no big-conversation warning. Everything keeps working, but the session switch (Box 6) depends on Claude noticing the size by itself, which often fails. Questions 2 to 4 are still possible (question 3 warns in % only if the watch exists).

**Undo:** delete `hooks/spend_watch.py`; remove its two entries (`"UserPromptSubmit"` and `"PostToolUse"`) from `settings.json`; delete the rule line in CLAUDE.md and, if you want, `hooks/spend_watch_state/`. Or restore the Box 1 backup. Applies from the next session.

**Skeptical reviewer:** "does it get around permissions?" No: it only prints text. "Does it read my conversations?" It opens the files but extracts only counts; the code is short and in the package to check. "Can it cost more than it saves?" The warning is one line; the real cost is delaying a session switch, which is what it prevents.

### Box 8 · Before/after

**Inside:** just a CLAUDE.md rule. Before a big task Claude reads the plan usage % (the usage tool in the app; in the terminal the person types `/usage`), and at the end says the difference in one line.

**What you gain:** you see the real cost of each big task, in % of the quota, and learn what weighs. No saving figure is promised.

**Risks:** almost nothing. The account % is an integer and includes other uses (another computer, phone, regular chat), so the difference is approximate. In the terminal Claude can't see `/usage`; it asks the person for the number.

**If you skip it:** nothing stops working; you just check usage on screen whenever you like.

**Undo:** delete the "Before and after a big task" line from CLAUDE.md. Applies from the next session.

### Box 8 · Measure plan

**Inside:** `measure_point.py <%>` records a mark (time, weekly %, weighted tokens added from the local records) in `tools/measure_marks.csv`. Between two marks it divides the weighted tokens by the rise in points and estimates how many are worth 1%. Marks less than 3 points apart are added to the next ones. With a stable number, the person puts it in `POINT` in `spend_watch.py` and the watch also warns in %.

**What you gain:** the warning in % of the quota, which is what the person feels, and the base for the daily report to compare with the account. The estimate is yours alone: on the author's machine 1 point was worth around 8.5 million weighted tokens, but this changes by plan and by use (measured on the author's machine, Sep-Nov 2026; don't use their number).

**Risks:**
- It is an estimate. Between two marks there can't be a reset of the quota week. Conversations outside Claude Code (regular chat of claude.ai or the app) are not in the records; if you use them a lot, the number comes out low.
- It reads the local records (counts only) and writes a small .csv; nothing leaves the PC.
- The rule has Claude read the % at the start of a session if the last mark is over a day old: one extra reading now and then.

**If you skip it:** the watch warns only in tokens; the daily report (question 5) works, but without the verdict about the account. Nothing else is affected.

**Undo:** delete `tools/measure_point.py` and `tools/measure_marks.csv`, the "Plan measuring" line in CLAUDE.md and, if you had set it, put `POINT` back to its original value in `spend_watch.py`.

### Box 8 · Usage skill

**Inside:** copies `skills/usage-report/` and `tools/usage_report.py`. When you ask "how much did I spend" or "where did my quota go", Claude runs the script, which adds weighted tokens by session and by model from the local records.

**What you gain:** an exact, fast answer instead of Claude guessing. No saving figure: it only informs.

**Risks:** almost nothing. It reads the local conversations only to count; nothing leaves the PC. The skill is loaded only when the question matches. The record format is internal to Claude Code and may change; if it does, the report comes out incomplete.

**If you skip it:** Claude answers those questions without the ready-made report (less exact). The daily report needs `usage_report.py`, but question 5 copies it by itself.

**Undo:** delete `skills/usage-report/` and `tools/usage_report.py`. Applies from the next session.

### Box 8 · Daily report

**Inside:** `daily_report.py` makes yesterday's report. The hook sits under `"SessionStart"` with `matcher: startup` (it runs once per new session, not at every message: the author measured 0.7 to 8 s per start on a PC with many open sessions, which is why it is not under `UserPromptSubmit`). With `--once-a-day`, if it hasn't warned today, it writes the date to `quota_keeper/daily_asked.txt` and puts in the context a line asking Claude to, before the person's request, ask in a box "Want yesterday's usage report?" (See it now / Not today). The report runs only if they accept. It stays silent inside screenless rounds and when the session has no person. A cheap check (header and date of the session files since yesterday) may add a line: "found N screenless sessions with no recorded warning or running for over 8 h".

The report shows: weighted tokens for the day on this PC (by model and the heaviest sessions); screenless sessions (the record's `entrypoint` field starting with `sdk`), each marked "logged and warned", "not in the log" or "ran X h"; and, if there are two account-% marks around the day, the comparison: it adds what this PC recorded between them, divides by the value of 1% and, if the account rose more than 1.5 times the explained amount + 2 points, warns. The CLAUDE.md rule has Claude record the account % (`--record-account <%>`) once a day when it can see usage (usage tool in the app; `/usage` in the terminal, which only the person types).

**What you gain:** catching spending you didn't see: a forgotten screenless session running, rounds opened without a warning, and a hint of account use outside this PC. Recommended if you turned on the token or screenless rounds (Box 7), because those are ways to spend with nobody watching. No saving figure promised.

**Risks:**
- A one-line reminder in the context at the start of the first session of the day (and a question box). It may bother someone who doesn't want it; "Not today" ends it for that day.
- Writes three small files in `<config folder>/quota_keeper/`: `daily_asked.txt`, `account_marks.csv` (only if Claude records the %), `relay_log.jsonl` (written by `session_relay.py`, without the token). It reads the local records only to count.
- False alarm: any other program that uses `claude -p` on this PC shows as "not in the log", and so do screenless sessions from before installation.
- The account % is an integer, hence the margin in the comparison; a weekly reset between two marks cancels the comparison (the script says so).

**Honest limits:** the script only sees this PC. Another computer, claude.ai, the phone or someone using your token don't show in the records: a difference from the account is a hint, not proof. Without the measured value of 1% (question 3), there is no verdict, only the numbers. A session left open from one day to the next asks again only if the person says "yesterday's report". Matching session and round by folder can fail with a path written another way. The record format is internal to Claude Code and may change; unreadable lines are skipped.

**If you skip it:** no report and no odd-spending warning; the watch, the measuring and the skill work the same. If question 3 (Measure plan) was "No", the report exists but without the comparison with the account.

**Undo:** remove the `daily_report.py` entry under `"SessionStart"` in `settings.json`; delete `tools/daily_report.py`, the CLAUDE.md rule and the `<config folder>/quota_keeper/` folder. Applies from the next session. `relay_log.jsonl` can be deleted at any time (it comes back with the next round).

**Skeptical reviewer:** "does it spy on my activity?" It only counts your account's use on this PC, on your computer; nothing is sent. "Does it prove someone stole my token?" No: it is a hint; check the account dashboard and, if in doubt, revoke the token. "A Python hook on every session?" One start per new session, and it exits early if it already warned today.

## Box 9

This box only saves behavior rules in CLAUDE.md. No script, hook or permission changes, and nothing leaves the computer.

### Box 9 · Checking

**Inside:** one rule line per checked habit. Cheap proof: use the text (a log line, a value, test output) when it proves it, and an image only cropped and at a smaller scale. Tests in parts: what changed plus a short regression at every change, the whole suite only before publishing. Two reviews, sensitive only: security, accounts, payment and cryptography get two independent reviews, the rest one. Don't pay twice: after an interruption, check what is still running and resume; end a process only by the number (PID) the session itself started, never by name.

**What you gain:** checking stays mandatory but spends less (images and big test runs cost). It also avoids restarting work that was still running and taking down another session's process. No saving figure promised.

**Risks:**
- Cheap proof: rarely, the text won't show a visual-only defect (layout, color). Ask for an image whenever you want.
- Tests in parts: an error outside the tested part only shows in the final suite.
- Two reviews, sensitive only: an area you don't consider sensitive gets a single review; if in doubt, leave it unchecked.
- They are instructions, not locks: Claude may forget one in a very long conversation.

**If you skip it:** Claude checks its default way (usually more images and reviews everywhere, more expensive) and has no PID rule; nothing stops working.

**Undo:** delete the rule's line in CLAUDE.md (or restore the Box 1 backup). Applies from the next session.

**Skeptical reviewer:** "does this lower quality?" It only changes the proof format and concentrates the double review where an error costs most; the final suite stays mandatory. "Does it kill processes?" The opposite: the rule forbids killing by name.

### Box 9 · Turn end

**Inside:** rules on how to end a message. Pending questions: what comes up during the work goes to the project's `PENDING_QUESTIONS.md` (created only at the first question) and is repeated at the end of the final message. Can I stop?: before stopping, Claude asks itself "should I be doing something before stopping?" and, if so, does it; if not, says what it waits for and what will wake it. Complete final message: answer on the first line, then pending items and what didn't go so well.

**What you gain:** nothing is lost between sessions, and the session doesn't sit idle waiting without saying so. The answer comes right away, with no scrolling.

**Risks:** almost nothing. Slightly longer final messages, a short check when stopping, and a new file in the project (`PENDING_QUESTIONS.md`, only if checked). Like any rule, Claude may forget it in a very long conversation.

**If you skip it:** pending questions may get lost in the text, a session may stop without notice, and the final message stays in the default format; the rest works the same.

**Undo:** delete the rule's line in CLAUDE.md and, if you want, `PENDING_QUESTIONS.md`. Applies from the next session.

## Box 10

### Box 10 · Star

**Inside:** if the person picks "Yes, remind me", Claude saves one line in CLAUDE.md with today's date + 7 days. From then on, in the first reply of a session, Claude asks once whether the tactics helped and, if the person wants, shows the repository link. After asking, it deletes its own line. With "Already did / doing it now" it only shows the link; with "No, thanks" nothing is saved.

**What you gain:** nothing for you; it helps other people find the guide. That is why the reminder comes after a week of use, not before you see the result.

**Risks:** practically none. One line in CLAUDE.md costs a few words of context until used. No data leaves the computer: the link is only shown, and Claude never stars it for you nor opens the browser.

**If you skip it:** nothing changes; there is no reminder and the rest of the package works the same.

**Undo:** delete the "One-time reminder (star)" line from CLAUDE.md (it also deletes itself once used). Applies from the next session.
