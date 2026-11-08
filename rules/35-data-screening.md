# Data screening: tools that take user data check it first

James's rule (2026-11-08, decision 55). Be extremely proactive about not implicating jeby in anything unlawful: flag questionable material and do not process it, including plain doubt about licensing or ownership. It applies to every jeby tool that takes user data: the free report, real-estate imports, learningLabs, Algo inputs.

## When
Screen before any value is read into a report, a store, a model or a prompt. The first pass looks at column names, field labels and file names, then at a sample of values. A tool that cannot screen does not process.

## Classes
| Class | Examples | Default | Override |
| --- | --- | --- | --- |
| Licensed identifiers | `td_linxID` (a retail-location id owned by a data vendor), D-U-N-S, MLS ids, credit-bureau ids, panel and ratings codes | exclude, say why | the user confirms they hold the rights; recorded in the output |
| Personal data | government ids, dates of birth, card and account numbers, health terms | exclude, say why | none for government ids and card numbers; others only with a stated lawful purpose |
| Minors | age or grade next to names, student records | never processed | none |
| Credentials | passwords, tokens, keys, connection strings | never processed | none |
| Unlawful content | material that is illegal to hold or share | never processed; stop and tell the user | none |

## Default and wording
- Doubt means exclude. The output still builds without the flagged items and names each one: the item, its class, why, and what the user may do.
- The message is plain and short, never an accusation: "Left out: td_linxID looks like a licensed identifier. Confirm you hold the rights to include it."
- Never-process classes have no confirm button. The tool does not echo, log, store or send the values, and the message does not quote them.

## What a user may confirm
Only a rights or ownership question in the licensed-identifier class (and a stated lawful purpose for non-government personal data). The confirmation is the user's, is recorded in the output (the report footer), and is never inferred by the tool.

## One pattern list
The patterns live in one data file, one line per pattern, with a test per class. It is owned by the free report (CONS-0045); other tools read that file or a vendored copy that a test compares to it. This rule names classes and never lists patterns, so it cannot drift from the file. Adding a pattern is a ticket with a test.

## In practice
- Screening runs client-side where the tool is client-side; nothing flagged leaves the machine.
- Real data in tests is replaced by synthetic fixtures that carry the pattern (the venues fixture carries `td_linxID`).
- Related: [privacy boundary](30-privacy-boundary.md), [security work](80-security-agent-rules.md), the `security` Definition of Done module.
