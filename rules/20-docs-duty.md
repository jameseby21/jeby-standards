# Docs duty

- Docs change in the same commit as the code they describe, or the commit says why not: trailer `Docs: none - <reason>`.
- Each repo keeps `docs/doc-ownership.yaml` (glob -> doc#section). A changed file's owning section is updated or regenerated in the same change. Generated blocks are never hand-edited.
- One owner per fact. Link to it; never restate it. An unreachable doc is a defect.
- Dated records (audits, hand-offs, sprint logs) preserve evidence and never pose as current instructions.
- A passing validator is not proof the docs are true. Check computable facts (versions, counts, routes) against code before reporting.

## Quickstart and commands
- Every repo has `docs/QUICKSTART.md` (a stranger reaches a running state on a clean machine, or stops at one actionable message) and `docs/COMMANDS.md` (every command a person or agent runs, with what it does and when), both from `standards/templates/`, linked from the README. James's rule, 2026-11-08.
- Subagents apply it: a worker that adds or changes a command updates COMMANDS.md in the same change; a worker that changes setup updates QUICKSTART.md. The docs module of the Definition of Done checks both.
