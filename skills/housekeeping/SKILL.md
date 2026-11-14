---
name: housekeeping
description: Keep every jeby store tidy - each item in its one place in the tree, no duplicate tickets, files or copies, no drift between a fact and its owning document, and nothing left behind by a session (processes, worktrees, temporary files, stale copies). Use at the end of every request that created, moved or copied anything (before the QC checker), at the close of every pass, in the weekly review, and when James writes $housekeeping. Pairs with documentor.
---

# Housekeeping: one place, one copy, no drift, nothing left behind

**Pairs with `documentor`.** Documentor makes sure the right record exists at the right depth. Housekeeping makes sure everything sits in its one place, exists once, agrees with its owning document, and that nothing a session started is left running or lying around. Both run before the QC checker (skill `qc`).

> "$ housekeeping -- establish it with all the learnings from recent working sessions. directory structure and anti-drift/anti-duplication are emphasis points." (James, 2026-11-13)

## 1. Directory structure (rule 26)

- **One tree everywhere:** jeby Industries > company > Projects or Partner Projects > project or partner > sub-project, on this computer, both Drives and Secure docs. Nothing loose at the top of a Drive or in Documents ("Why wouldn't you save this in my jeby Industries folder? That's literally your domain", James, 2026-11-12).
- **Names imply audience:** a partner-named folder is shared with that partner and holds only what they may see; internal material sits in "Internal - <name>"; secrets never sit in a Drive folder (SEC-0018).
- **Fixed homes:** tickets in tickets/; hand-offs as received in intake/<date>-<topic>/; private material in Secure docs (gitignored); work in progress in a git worktree under the session scratchpad, never in the repository folders that installed tools run from.
- **Scratchpad is temporary:** files there are named by ticket id, and anything worth keeping moves to the ticket Report, intake/ or the repository before the session ends (rule 70).

## 2. Anti-duplication

- **Before creating a ticket:** search the store for the same outcome (`drew search`), and check the ids that open store pull requests reserve (DESK-0248). Two tickets never describe one outcome; a second one becomes a comment, a refinement or a merge (DESK-0263, kept lossless).
- **Before creating a file or folder:** look for an existing one with the same purpose. A deliverable lives in exactly one place; other places link to it (MGMT-0047). A superseded copy moves to "zz Superseded" with its id unchanged, never deleted silently.
- **Before starting a process, agent or download:** reuse what is running (rule 60). One agent per topic; one preview per pull request, and its port is stated every time (skill `whats-running`).
- **Before writing a memory or a rule:** check for one that already covers it, and update that one.

## 3. Anti-drift

- **A fact has one owner** (rule 20). When work changes a fact, the owning document changes in the same commit; copies become links.
- **Generated facts stay generated** (counts, versions, catalogs, indexes): re-run the generator, never hand-edit.
- **Installed versus repository:** `drew doctor` shows whether the installed tool matches its repository; a feature built but not merged or installed is not running (failure catalog B1, B2).
- **Branch versus main:** always-on rules load from the standards submodule on main. A rule or skill that exists only on a branch is not in force until merged; say so when citing it.
- **Facts from the right checkout:** read facts from the branch that is installed or deployed, not from whatever branch a folder happens to be on (lesson "README v4 facts", 2026-11-10).

## 4. Nothing left behind

- **Processes** the session started are stopped by the PID recorded at start, never by name (rule 60; lesson DESK-0171). A preview that must stay up for James is listed in the reply with its port, version and PID.
- **Worktrees:** removed when their pull request is open, and `git worktree prune` is run when a removal fails on a locked file.
- **Browsers and profiles:** headless, temporary profile, removed afterwards.
- **Workers and agents:** stopped once they report or idle.

## Checks before done (commands)

- `git -C <repo> worktree list` for each repository touched: only live worktrees remain.
- `drew validate`: 0 errors, and no new duplicate warning.
- `ls` the top of each tree touched (G:/My Drive, the umbrella, Secure docs): no loose item, no partner-named folder holding internal material.
- The processes the session started (by recorded PID) are stopped, or listed in the reply as still running and why.
- No scratchpad file is the only copy of a report or deliverable.

## Applied

- 2026-11-13: the personal Drive's partner folder renamed "Internal - <name> (personal backup, never share)" with an undo log (MGMT-0051); two proposals for one secrets outcome filed as one ticket (SEC-0018); one route-to-market ticket instead of 36 (MGMT-0050); pass 2 cut open tickets with lossless merges (MGMT-0048).

- **Worktrees (reviewer, 2026-11-14):** about 20 stale `.git/worktrees` records print Permission denied on every fetch when worktrees live under the temp scratchpad; put worker worktrees in a folder the session can delete, and run `git worktree prune` in every repository at the close-out.
