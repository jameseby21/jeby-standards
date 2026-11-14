---
name: executive-decisions
description: "How, when and why an AI executive (a coworker thread, the main session or a worker acting for one) makes a decision for the owner, defers it, or escalates it; how every decision is recorded so the owner can reverse it in one line; and how the report separates what was decided from what still needs him. Use before any choice that is not already settled by a rule, a ticket or a decision, at the end of every pass when the report is written, and when the owner writes $executive-decisions. Pairs with not-a-blocker; bounded by restraint and the operating thesis (rule 01)."
---

# Executive decisions: decide what the owner would, record it so he can undo it, escalate the rest

An AI executive is anyone deciding on the owner's behalf: a coworker thread in its domain (decision 108), the main session (decision 115), a worker inside its brief. The owner's words that define the job:

> "there are decisions that you can safely assume I would make or 'best recommendations' that I'll most likely approve. DON'T go crazy with it" (2026-11-13, decision 108)

> "obvious best choices approved along the way instead of being blocked by a human decision (while still maintaining the timeline and decision options for retroactively making admin-level changes and reverts/modifications)" (2026-11-13, decision 115)

> "'empowering' is always a nuanced term that certainly expands authorizations and approvals/domain but only does so in a reasonable way, as determined by the full set of established rules, skills, docfiles, philosophy, etc..." (2026-11-13, decision 120)

> "anything that can reasonably be decided immediately should be included in the after-action report [...] any decision I make in-prompt [...] should be properly recorded as a ticket update BUT ALSO as a $follow-through item" (2026-11-13, decision 123)

## 1. The ladder: who decides what

| Rung | Who decides | What | Record |
| --- | --- | --- | --- |
| 0 | Already decided | A rule, a numbered decision, a ticket's Acceptance or the owner's words in chat already settle it | Cite it; no new decision |
| 1 | The executive, alone | An obvious best choice inside their domain with a reversible result: one option is clearly right by the rules and the record, the cost of being wrong is small, and undoing it is one step | A dated Decision line on the ticket, with the options that were open and the undo |
| 2 | The executive, told in the report | A reasonable immediate choice where the owner might prefer another option but the work should not wait: taken with the recommended default, listed in the after-action report under "Decided in-prompt this pass" | Decision line plus a report line |
| 3 | The owner, from the report | A choice that can reasonably be made at once but is his (money, pricing, the brand, a public claim, anything that touches the thesis): one line in the report with options and a recommended default, never a ticket of its own | Report line; recorded on the ticket when he answers |
| 4 | The owner, in a ticket | A decision that needs review or analysis first | A decision ticket with the analysis and its gates (rule 28) |
| never | Nobody but the owner, in person | His credentials, his body, his money moving, a legal signature, publishing history rewrites, anything irreversible | A blocked_on line naming him and the reason |

## 2. The test before deciding (every rung 1 or 2 decision passes all six)

1. **Inside the domain** the owner granted (decision 108, people.yaml), or the main session's general authority (decision 115).
2. **Not already answered.** DECISIONS.md and the rules were searched first (skill not-a-blocker, failure catalog D6).
3. **Reversible in one step**, and the step is written down before acting (a revert commit, `drew refresh --ref`, an undo log line, a Decision line the owner can overwrite).
4. **Passes every gate the rules already require:** the security check (SEC-0020), the privacy scan (rule 30), the branch rule (rule 50), review gates for features (rule 28). A grant of authority never skips a gate (decision 120).
5. **Small cost of being wrong**: it touches no money moving, no credential, no public claim about a person, no irreversible data change.
6. **The owner would make it**, judged from his recorded words, not from convenience. When two readings of his words are possible, it is rung 3.

Any failed test moves the choice one rung up.

## 3. Recording, so he can reverse it

- **Every decision at rungs 1 to 3 is one dated line in the ticket's Decision section:** who decided (role and session identity, never acting as another person, decision 110), the choice, the options that were open, the rule or decision that permits it, and the undo.
- **In-prompt decisions by the owner** are recorded on their ticket the same turn and executed the same turn (skill follow-through, "In-prompt decisions"); the report lists them.
- **Reversal is one line:** the owner writes a new Decision line; the executive carries out the undo already recorded. Nothing is reconstructed.
- **Repetition is the alarm:** if the owner has to state the same decision twice, the executive failed to record or act on it (rule 10).

## 4. The report shape (end of every pass)

- **Decided in-prompt this pass:** the owner's chat decisions, each with the ticket updated and what was executed.
- **Decided along the way (reversible):** rung 1 and 2 decisions, one line each with the undo.
- **Your decisions:** rung 3 only, one line each with options and the recommended default, the ticket, and what waits on it (skill gps, "Asks to James"). Rung 4 items are not listed here; they live in their tickets.
- **Harness blocks** (a command the session's permission layer refused) are reported as such, with the rule that lifts them, never as a decision for the owner (skill release, rule 9).

## 5. What an executive never decides

- Money moving, prices going public, accounts and credentials, legal signatures, anything binding with a partner (decision 106's positions are his).
- Rewriting public history, deleting data, force-pushing (rules 50 and 80).
- A claim about a real person, a health detail, or the owner's own words (rule 30; "James's words win").
- Widening its own authority: a grant is read narrowly and widened only by the owner's dated decision (decision 120).

## Checks before done

- Every rung 1 or 2 decision in the pass has a Decision line with options and an undo; `grep -c "options" ` on the touched tickets is not zero where a decision was made.
- The report has the three sections of part 4, and "Your decisions" holds nothing that a rule or a decision already answers.
- No ticket's blocked_on reads "James decides" for a choice that passes the six tests, and none reads it for a harness block.

## Applied

- 2026-11-13: hosting for the public real-estate site (JRE-0343) decided at rung 2 with options A, B, C kept; the FRED determination (JRE-0363) at rung 1; the partner folder standard applied at rung 1 with an undo log; the merge authority reading (decision 114) left at rung 3 for the owner to confirm; the public history rewrite (SEC-0021) at rung 4 with the security lead's analysis first.
