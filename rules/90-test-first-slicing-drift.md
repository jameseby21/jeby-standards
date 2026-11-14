# How code gets written here: test first, errors become tests, thin slices, no drift

Adopted 2026-11-08 from James's existing practice in jRE (AGENTS.md, the Definition of Done, the `testing`, `validator`, `scope`, `chunked-delivery` and `appforge-trainer` skills) and the AppForge cases in Plantriloquist. This is the short form; the Definition of Done modules carry the checks.

## Test first
- Write or name the focused acceptance test before the implementation when practical, and watch it fail for the missing behavior. Every regression test carries one line saying what it protects.
- Tests assert outcomes, not that lines executed. Success checks validate payload or state; failure checks validate status, detail, preserved state and recovery.
- A mocked test is test coverage, never runtime proof. Runtime proof is the real stack, named in the Report.
- Change-aware inspection on every ticket (the persistent baseline plus every test for the touched scope); full inspection at milestone, shared-contract and release gates.

## Errors become tests (the bone)
- Every failure that reaches a human produces three things: a documented case (what happened, the evidence), a rule (the sentence that prevents it), and a test that proves the rule. Filed in `standards/lessons/` or the project's lessons doc, linked from the ticket.
- A rule that turns out wrong stays in the file, marked as a bad bone with the corrected reading, so nobody buries it again.
- AppForge is this loop made reusable: the case, the rule and the test are what it would generate for someone else.

## Thin slices
- A slice is one outcome, one project, acceptance a test or a person can check, sized to one focused session. Size `m` is split in triage; `l` never leaves it.
- Slices exist to keep context small: one slice per session, `/clear` between slices, logs to files, briefs that state goal, exclusions, pointers, scope, effort and model.
- Large jobs follow the staged protocol: unit test, one record end to end, a seeded random sample, then the whole job, with dry-run and sample controls first. Process one file or table at a time; stream and release. Long-running scripts print progress and a final summary.
- Safety comes from the slice boundary: a session that needs a decision mid-slice writes the question in the Report, marks `blocked`, and stops.

## Drift-proofing
- Docs change in the commit that changes the code, or the commit says why not. The owning doc for every file is in `docs/doc-ownership.yaml`; a pre-commit hook enforces it where one is installed (today only jeby Real Estate's `.pre-commit-config.yaml`; planned for the other repos).
- Computable facts (schema head, versions, counts, routes, script inventories) are generated blocks, never typed. A passing validator is not proof the docs are true; check the facts against code before reporting.
- One owner per fact; link, never restate. Dated records keep evidence and never pose as current instructions. A new chat resumes from the records, never from an earlier chat.
- Claimed is not run. Anything not run is marked not run.

## Comments and documentation
- A comment says why, not what; the code says what. A docstring on a test names the behavior it protects; a header `Docs:` line names the owning doc section.
- Documentation has four destinations: product (what we are building), reference (how it works), guides (how to work on it), records (what happened, dated). A document earns its place by owning facts no other document owns.
- Write for the reader who was not in the conversation: the clean-clone reader, the reviewer, the interviewer. If they cannot follow it to a running state or a verified claim, it is not documented.
