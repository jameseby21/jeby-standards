---
name: reviewer
description: The structure review inside QA/QC. Use at the end of any request that created or moved structure (folders, the ticket hierarchy, projects, companies, repositories, rules, skills, data layouts), at the close of every pass, and when James writes $reviewer. It compares the established structure with the stated goals and reports what will not scale (skill scalability) and what cannot be redone from the record (skill reproducibility). A subskill of qa and qc.
---

# Reviewer: does the structure serve the goals, at ten times the size?

**Part of QA/QC.** QC asks "is what was delivered true?" (skill `qc`). The reviewer asks "is the shape we built the right shape for where James is going?" It reads structure, not lines of code. Its two lenses are the skills `scalability` and `reproducibility`.

> "let's add a $ reviewer subskill within QA/QC which asseses established structure vs. goals to ensure proper $ scalability." (James, 2026-11-13)

## Inputs

- **The goals, from the record:** the request in James's words; the numbered decisions it touches (DECISIONS.md); the hierarchy words (decision 99: empire, company, project, product); the priorities he stated for the pass.
- **The structure as it is now:**
  - the folder trees (rule 26);
  - the ticket hierarchy (ticket, track, project, company, jeby; decision 83);
  - the project registry (projects/) and the repositories (docs/REPOS.md);
  - the rules and skills (standards/);
  - the people and their roles (people.yaml).

## Rules

1. **Goals first, from the record.** Name the goals the structure must serve before judging it, each with its source (a quotation or a decision number). A structure judged against goals nobody stated is taste, not review.
2. **Observe, do not infer.** Every finding cites a path, a count or a file line that shows the structure as it is (`ls`, `drew stats`, `grep`), not as a document says it is.
3. **Ten times the size.** For each element, ask what breaks at ten times the tickets, projects, companies, coworkers or files (skill `scalability`). A finding names the breaking point and today's count.
4. **Redo from the record.** For each element, ask whether a newcomer could rebuild it from files alone (skill `reproducibility`). A step that lives only in a chat or in one session's memory is a finding.
5. **One place per fact, one owner per level.** Two places holding the same fact, or a level with no owner, is a finding (rules 20, 26 and 27).
6. **Smallest structural fix.** Each finding proposes the smallest change that removes the breaking point (a rule line, a field, a folder move, a generated index), with its cost. A rewrite is proposed only when a stated goal demands it.
7. **Severity by goal.**
   - High: the structure contradicts a stated goal, or fails at the next real step (the next project, coworker or company).
   - Medium: it fails at ten times the size.
   - Low: friction.
8. **Read-only.** The reviewer changes nothing. Findings become tickets or rule changes through QA (skill `qa`).

## When it runs

- **After the independent checker** (skill `qc`), once per request that changed structure, and at the close of every pass.
- **Model:** the strongest model allowed for the request, at high effort, because judging shape is judgment. Never above the ceiling James set for the request (decision 109: Opus at extra-high effort at most, never Fable, for the 2026-11-13 prompt).
- **Time box:** 30 minutes.

## Report

| # | Goal (source) | Structure observed (path, count) | Breaks at | Redoable from the record? | Smallest fix | Severity |
| --- | --- | --- | --- | --- | --- | --- |

Then the three findings James should read first, one line each.

## Checks before done

- Every finding cites an observation (a path, a count or a line).
- Every goal cites its source.
- Each high finding has a ticket or a rule change filed, or the reply says why not.
