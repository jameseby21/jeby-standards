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
