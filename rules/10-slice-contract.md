# The slice contract

- A ticket is the unit of work: one project, one outcome, acceptance a test or a human can check, the docs it must touch, size no larger than one focused session. Size `l` is split before it leaves triage.
- A session claims a ticket before touching code (`desk claim`), works only inside its scope, and writes the Report before stopping (`desk report`). The Report names what changed, the exact commands run, what they printed, and open questions.
- Needs a decision mid-ticket? Write the question in the Report, `desk block`, stop. Never guess.
- Effort is a range of hours with a confidence, never points. Every open ticket names the smallest step that still counts on a rough week.
- One ball at a time: one `in_progress` ticket per owner. Pick up another only after dropping the first (review, blocked or done).
- Done means proof plus the owner's own words. "Looks good" in a chat is not approval; `desk decide` is.
- A ticket never restates the Definition of Done. It carries its own Outcome, Acceptance and How to validate, and names the DoD modules that apply; the checks themselves render from the DoD files by reference, and a project's own DoD (declared as `dod_doc:` in its profile) takes precedence for its tickets. The DoD defines doneness; the ticket does not.
- Execution posture comes from two promoted skills: `follow-through` (authorization starts execution; never end on a plan while safe authorized work remains) and `restraint` (hold scope; the smallest reversible alternative; archives untouched). They are a yin/yang pair and load in every session.

## Tests section (James, 2026-11-08)
- Every ticket has a `## Tests` section, even when the test is a person looking at a screen: it names the automated test when one exists and otherwise the exact steps a person performs and what they must see. All failures become tests (rule 90); the Tests section is where the ticket points at them.

## Refinement and scope change (James, 2026-11-08)
- A refinement (the same outcome, a sharper requirement) is recorded on the existing ticket as a dated acceptance line or comment, and the ticket may slip; the slip is noted, not hidden.
- A scope change (a different or larger outcome) is never absorbed. It forces a new ticket with its own details and timeline, a completion decision on the existing ticket (done as scoped, or closed in favour of the new one), and a blocker link between the two (`blocks:` or `depends_on:`), so neither can quietly carry the other.

## Comments are work (James, 2026-11-08)
- A note or question James leaves on a ticket ("why is this like that?") is a bug, a fix or a decision to execute unless he says otherwise. The sweep lists his comments since the last pass; each gets an answer line in that ticket and the ticket or decision it produced, within the hour.

## Visible progress (James, 2026-11-08)
- Every running process a person starts shows visible, helpful progress where they clicked: what is happening, how far along (a bar with steps or a count, not only a spinning circle), and then a plain success or failure sentence a person can read. This is an app-wide rule for every jeby product, and clarifying a ticket to meet it is a refinement, not a scope change.

## Repetition is an emergency (James, 2026-11-08)
- James (2026-11-08): "Repetition should mark absolute failure in meeting my expectation, but cursing should indicate an emergency-level situation." Two signals, two readings: a repeated ask is recorded as an absolute failure of the first delivery (the ticket's Report says so, the triage asks why), and cursing in any message marks an emergency on the spot, before any third ask: priority p0, tag `emergency`, the fix built with present tools now, and the one step only James can do stated in the first line of the reply.
- When James asks for the same thing a second time, the ticket becomes an emergency: priority p0, tag `emergency`, and the session stops everything else to deliver it with the tools already present. A third ask opens a triage ticket (what was asked, when, what Patch did instead, the root cause, the preventative measure) that closes only with a rule or skill change and a lesson.
- A step is handed to James only when it truly needs his credentials, his body or his judgment. Before handing anything over, the session names the tool it lacks and checks whether another tool already present does the job (git can merge what the GitHub CLI would merge). 'Waiting on James' is written in the ticket's blocked_on with the reason, never left implicit.
- Being told once is being told. The sweep, the Needs me list and the ticket's own blocked_on carry the ask forward; forgetting is a defect of the record, not of memory.

## What James says moves tickets (James, 2026-11-08)
James: "In case it wasn't clear: tickets should also be updated and potentially completed based on what I say as well, not just created and added" A statement from James in chat or in a ticket is recorded on the ticket it concerns the same turn: a step he reports done closes his Do ticket with his words as the Decision; a choice he states approves the decision ticket in his words; a verdict moves the ticket to review, changes requested or rejected; a new requirement becomes an acceptance line or a refinement. Creating tickets is the smallest part; keeping the existing ones true to what he said is the duty.

## Dispatch is the job (James, 2026-11-08)
James, when a delivered design sat an hour with its build tickets ready and nobody on them: "that is precisely your job to delegate"
- A ready ticket assigned to Patch whose dependencies are all in review or done is dispatched within the hour: a worker starts, or the ticket says in `blocked_on` why not (one worker per repository is the only accepted reason, and then the ticket names the worker it waits for).
- Every Patch turn ends with the dispatch check: `drew list --status ready --assignee main`, unblocked ones first; anything undispatched for more than an hour is a defect in Patch's log and a `drew validate` warning.
- A design delivery (Chaz's entry with build rows) is not filed until its build worker is named in the build tickets.

## Where a ticket sits (James, 2026-11-08, `$formalize-it`)
> "Ticket < Track < Project < company < jeby overall, while 'sprint' is more generalized and synced across libraries and maybe some other ways of slicing and dicing them."

- Every ticket sits in exactly one track, every track in one project, every project in one company, every company in jeby overall; each level has its own profile, rollup and view (skill `modularity`). Sprints, assignees, tags and types are slices that cut across the levels and never substitute for one. A board, rollup or report that skips a level, or calls the whole store the "company", is a defect. Personal matters are companies too, in business terms only (health for medical items).
