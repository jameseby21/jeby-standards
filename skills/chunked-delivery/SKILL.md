---
name: chunked-delivery
description: Deliver broad multi-part work in bounded verified Git checkpoints when context, runtime, merge risk, or user instructions make one continuous change unsafe; the partner of ideal-trajectory.
---

# Chunked Delivery

Pairs with `ideal-trajectory`. Chunked delivery lands broad work as reviewable, verified checkpoints. `ideal-trajectory` keeps the SMART queue and the order those checkpoints follow. Use both: the queue says what comes next, the checkpoint proves it.

Use this skill for broad prompts, concurrent contributors, long-running verification, or any explicit request for incremental commits and pushes.

- Convert the request into a dependency-ordered checkpoint ledger. Each checkpoint has one coherent outcome, affected files, focused proof, and a commit boundary. In jeby repos a checkpoint is usually one ticket, one commit, on the ticket's branch.
- Finish and verify the smallest useful checkpoint before opening the next. Push after each approved checkpoint when requested; stage exact files so concurrent or unrelated work remains untouched.
- Record `commit: required/deferred` and `push: required/deferred` plus the user instruction that establishes them in the checkpoint ledger. Standing authorization persists until the user changes it; an assistant handoff cannot revoke it. Before claiming delivery, inspect branch ahead/behind state and, when a push is required, verify the remote branch contains the checkpoint after a normal push. Report a failed push as incomplete delivery; never replace it with an unsupported permission explanation or a force push.
- Keep command output bounded. Capture verbose success detail in ignored log files, show summaries, and emit a useful tail only on failure. Sample user-provided log walls unless exact parsing is necessary.
- Default to one writer and tester for each checkpoint. Do not use subagents for serial edits or shared database or UI changes; use at most two read-only agents for genuinely independent exploration or review, require concise evidence-only summaries, and keep checkpoint ownership with the writer. Subagents reduce main-thread context pollution only when that benefit outweighs their token, coordination, and merge cost.
- Use focused tests while iterating, then the affected-scope profile at the checkpoint. Reuse still-valid evidence; rerun only dependencies invalidated by later edits.
- Before a likely context compaction or after one occurs, stop expanding scope, record completed evidence and remaining work, and create the next safe Git checkpoint. A summary is recovery help, not a substitute for the requested checkpoints.
- Do not claim an internal platform crash count without observable evidence. Distinguish tool failure, context compaction, process exit, timeout, and credit interruption.
