---
name: qa
description: Quality assurance for every jeby request, before and during the work. Use when planning, slicing, briefing a subagent, or writing a ticket, and when James writes $qa. It prevents the known failures (claimed-not-run, wrong instance, unchecked links, private leaks, overridden owner words, quietly shrunk scope) and schedules the independent checker at the end of every request. The partner of qc.
---

# QA: build quality in before it can go wrong

**QA is about the process; QC is about the product.** QA works before and during the work and makes a defect unlikely: the standards, the brief, the ticket's How to validate, the gates, who checks whom. QC works after the work and finds the defects that got through, by inspecting the output against its acceptance (skill `qc`). Every QC finding feeds back here as a rule change, so the same defect cannot pass twice.

> "data quality is not simply a nice-to-have, but rather it can keep you from ever gaining any momentum if you don't take it appropriately seriously, even if you have a 'good' product." (James, 2026-11-12)

## James's requirements (level 1, standards rule 00)

1. **Quality is an independent function.** The person or agent who checks is never the one who built it. In a venture this is a QA branch led by a QA executive, reporting to the CEO and the board, outside delivery (decision 106). In a session it is the independent checker (skill `qc`).
2. **How to validate comes before the work** (rule 45). Every ticket names, before anyone starts, what a person runs or opens and what they must see. A worker who has to write it afterwards reports that as a QA defect.
3. **Claimed is not run** (rule 40). A Report names the command, where it ran and what it printed; anything not run is marked "Not run". A mocked test is coverage, never runtime proof.
4. **Test first, and every failure becomes a rule plus a test** (rule 90), filed in the lessons record the same day.
5. **Rules over results** (decision 82). A strong result that breaks a rule is a trust defect; a weak result is a prompting defect.
6. **What's running is stated every time** (skill `whats-running`). Every link is checked before it is sent; built but not merged counts as not running.
7. **Privacy first** (rule 30). Run the private-strings scan before every commit, including on a worker's report text.
8. **Review gates** (rule 28). Major or commercial work gets legal, financial, security, creative, UX and UI review subtickets.
9. **James's words win.** Text he wrote or chose is kept as he wrote it, unless he says otherwise. A voice or style pass never rewrites it.
10. **Scope is the whole ask.** A request for "any" or "all" workable items is not met by one area of them. Shrinking scope for budget is allowed only when the reply says so plainly, in its first lines.

## Before work starts (the QA checklist)

- **Brief every subagent** with the goal, the exclusions, the files, the effort, the model and the time box (rule 70). Also give it the privacy line ("name roles, never people or companies") and the evidence line ("every claim carries the command and its output").
- **Check the ticket's How to validate before dispatching** (see the `qc` stress test). Is each line runnable by the reader as written? Would it fail if the change were missing? Does it check the outcome rather than a stand-in? Is the expected result specific? Fix weak lines first; it is the cheapest QA there is.
- **Name the instance.** Say where the user will see the change (the installed tool, the live site, the merged branch) and plan the check there, not only in a worktree.
- **Name the not-done in advance.** If a check cannot run here (no browser, no credentials, another OS), the brief says so, and the Report is expected to mark it "Not run".
- **Reuse before create** (rule 60). Check for a running process, an existing ticket, an open PR, a branch that already answers the ask (the "already answered" check).

## During the work

- **One commit per ticket**, and the commit message names it. A worker that bundles two tickets reports it.
- **Look at what you produced.** A screenshot that is taken but not looked at is not evidence. Re-take it after any later change.
- **Write evidence after the command returns**, from its exit code and output.
- **Close what you open**, by the PID you recorded.

## After every request: schedule QC

When the whole request is done and every subagent has reported, launch one independent checker, following skill `qc`, section "The independent checker". It runs once per request, last, on the cheapest model at low effort. Skip it only for a request that changed nothing (pure discussion). Say in the reply that it was skipped and why.

Record each run's outcome in `standards/qc/checker-ledger.md` (see `qc`, section "Is it worth it"). QA owns that ledger. The checker is retired or redesigned when the ledger says it finds nothing the process missed.

## The known failures

`references/failure-catalog.md` lists the most common and the worst failures across the projects so far. Each has the rule that prevents it and the check that catches it. Read it when writing a brief or a How to validate. Add to it whenever a QC finding or a person finds something new.

## Checks before reporting done

- Every touched ticket has a How to validate that was there before the work.
- Every claim in the reply has its evidence or is marked "Not run".
- The private-strings scan printed clean on everything committed.
- The independent checker ran, or the reply says why it did not.
