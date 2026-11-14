---
name: qc
description: Quality control after the work, and the independent checker. Use at the end of every request that changed something, once all subagents have reported, and when James writes $qc. A minimal-model subagent, separate from the builders, checks the delivered outputs by a different route than the checks already run, and stress-tests each ticket's How to validate (is it runnable, and would it fail if the change were missing). The partner of qa.
---

# QC: find what got through, by a route nobody used yet

**QC inspects the product; QA shapes the process** (skill `qa`). QC runs after the work, compares what was delivered with what was asked, and reports the gaps. It fixes nothing. Each finding goes back to QA as a rule change, or to the ticket as a defect.

## James's requirements for QC

- **Independent.** The checker is a separate subagent that did not build, brief or report the work. It never takes a worker's or Patch's word as evidence.
- **Not a repeat.** It must not re-run the calculations and commands the existing process already ran (the same test suite, the same grep, the same build). It finds a different route to the same claim: a different entry point, the instance the user runs, the live artifact, the base branch, a negative case, a fresh look at a cited screenshot.
- **It tests the test.** It treats each ticket's How to validate as a possible route, not as truth, and reports whether the procedure is sound.
- **Last and once.** It runs after the whole request is finished and every other subagent has reported, once per request.
- **Proportionate.** Sonnet at high effort by default, a 25-minute time box, read-only. James, 2026-11-13: "let's ramp UP their model a little bit because that's how important is is. You may use any model/effort combination that you think is appropriate but do NOT use Fable or higher." Judgment-heavy checks (the reviewer, data-loss checks) may use Opus, up to the ceiling James set for the request; never Fable.
- **The broadest skills.** QA and QC cover every request, code or not. QC's verdict is the gate before the main session reports a request complete; a ticket is done only on its owner's decision (rule 10), and QC never approves one (decision 112).

## The independent checker

**Launch** (main session, after the request's last report): one subagent, model sonnet, effort high, time box 25 minutes (before 2026-11-13: haiku, low, 15 minutes). Give it the brief in `references/checker-brief.md`, filled in with:

- the request in James's words;
- the tickets touched, with their ids;
- the commits, PRs and live URLs;
- the checks already run, so it can avoid them.

**What it does, in order:**

1. **Claims.** List every claim in the final reply and the ticket Reports, for example "PR X adds Y", "tests pass", "link Z answers", "James's line restored".
2. **Pick by risk.** Choose the five claims that would hurt most if false, using the `qa` failure catalog: wrong instance, unchecked link, private leak, overridden owner words, quietly shrunk scope, acceptance not literally met.
3. **Re-check each by a different route.** For example:
   - read the file at the PR head rather than the worker's diff summary;
   - request the URL rather than trusting a status code in a Report;
   - run a single validation line against the base branch;
   - grep the committed text for a quoted owner line;
   - open a cited screenshot;
   - count the delivered items against the request's own list.
4. **Stress-test How to validate** on each touched ticket (up to five). Mark each line:
   - **runnable**: the commands exist, the paths resolve, the URLs answer, the prerequisites are stated;
   - **discriminating**: it would fail on the base branch or the old version; try it on one line per ticket where cheap;
   - **outcome, not a stand-in**: it checks what the user gets, not that a file merely changed;
   - **specific**: it names the expected text, number or state, not "looks right";
   - **covering**: every acceptance line has a matching validation line.
5. **Asks to James.** Check every ask in the final reply against skill `gps`, section "Asks to James": meaning, his step, the ticket with its title and link, by when, checked against reality. A missing part is a medium finding; an unchecked click path or command is high.
6. **Report** in the format below. No fixes, no ticket moves. One comment per ticket with its findings, posted under the checker's own identity, never as anyone else: `DESK_ACTOR=qc-checker DESK_ACTOR_KIND=subagent drew comment <ID> "<text>"` (decision 110; `--as` another person is refused once DESK-0261 is installed). Until personal keys exist (DESK-0262), that identity is claimed, not verified.

**Report format** (the checker's final message, also saved as `qc-<date>-<request>.md` in the scratchpad):

| # | Ticket or claim | Route used (and why it differs from the checks already run) | Result | Severity |
| --- | --- | --- | --- | --- |

- Result is one of: confirmed, contradicted, unverifiable here.
- Severity: high (a false claim, a leak, the wrong instance), medium (a weak or untestable validation step), low (wording).

Then a How-to-validate table: ticket, verdict (sound, or weak with the reason: not runnable, passes on base, stand-in, vague, gaps), and the line that needs rewriting.

## Fixers: a finding with a test gets a minimal fixer (James, 2026-11-13)

> "WAY MORE SIGNIFICANT QA/QC checks that are proactive in establishing minimal "fixer" subagents that develop based on the main agents' pre-defined tests" (James, 2026-11-13)

- Every reviewer and checker finding names, where it can, the test that would prove the fix (a command and the output expected). That test is written down before any fixer starts.
- For each confirmed finding with such a test, the main session starts one minimal fixer: the smallest model that can do it, one branch, one commit, the test red then green, no scope beyond the test. A finding without a test gets a ticket, not a fixer.
- Fixers run in parallel, one per finding, never two on one file. Their reports paste into the ticket, and the checker's next run re-checks the fixed claim by a different route.
- A fixer that cannot make the test green within its time box stops and reports; it never widens the change to force the test.

## Around the checker: documentor and housekeeping before, reviewer after

- **Before:** the `documentor` subagent (lightest model) makes sure every item of the request is recorded at the depth it needs, and `housekeeping` puts things in their one place and clears what the request left behind, so the checker reads the final state.
- **After:** when the request created or moved structure, the `reviewer` subskill compares the structure with the stated goals, through the lenses of `scalability` and `reproducibility`.
- **Order at the end of a request:** workers report, then documentor and housekeeping, then the checker, then the reviewer, then the reply.

## Is it worth it (QA owns this ledger)

After each run, the main session adds one row to `standards/qc/checker-ledger.md`:

| Date | Request | Tokens | Findings | Real and new | False alarms | Weak How-to-validate found |
| --- | --- | --- | --- | --- | --- | --- |

From 2026-11-13 each row also names the model and effort, because the checker moved from haiku to sonnet; compare runs only within one model.

"Real and new" counts the findings that were true and that no earlier check had caught; that number is the checker's whole value.

**Decision rule:**

- **Keep** if, after five runs, real-and-new findings average at least one per run.
- **Narrow the brief** if they average below one.
- **Retire** if three runs in a row find nothing real.

James sees the ledger in the weekly review.

**Verdict after five runs (2026-11-14):** keep. Runs 1 to 5 found 8, 11, 6, 6 and 3 real and new findings with no false alarm; the checker stays, on Sonnet at high effort, with the fixer pattern feeding its findings straight to minimal fixers.

## Checks before the main session reports done

- The checker ran after the last subagent report, or the reply says why it did not.
- Its high-severity findings are in the reply, in plain words, before anything else.
- The ledger has a row for this run.
