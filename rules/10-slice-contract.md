# The slice contract

- A ticket is the unit of work: one project, one outcome, acceptance a test or a human can check, the docs it must touch, size no larger than one focused session. Size `l` is split before it leaves triage.
- A session claims a ticket before touching code (`desk claim`), works only inside its scope, and writes the Report before stopping (`desk report`). The Report names what changed, the exact commands run, what they printed, and open questions.
- Needs a decision mid-ticket? Write the question in the Report, `desk block`, stop. Never guess.
- Effort is a range of hours with a confidence, never points. Every open ticket names the smallest step that still counts on a rough week.
- One ball at a time: one `in_progress` ticket per owner. Pick up another only after dropping the first (review, blocked or done).
- Done means proof plus the owner's own words. "Looks good" in a chat is not approval; `desk decide` is.
- A ticket never restates the Definition of Done. It carries its own Outcome, Acceptance and How to validate, and names the DoD modules that apply; the checks themselves render from the DoD files by reference, and a project's own DoD (declared as `dod_doc:` in its profile) takes precedence for its tickets. The DoD defines doneness; the ticket does not.
