---
name: formalize-it
description: Turn the feedback beside a `$formalize-it` invocation into a rule written for every LLM or agent regardless of context, placed and checkable in the same turn; also the marker James uses to declare something critical to his sanity or efficiency, which then outranks feature quality.
---

# Formalize It

Pairs with `generalize-it`: formalize-it writes the rule precisely from one case; generalize-it carries a proven change across every surface it should hold on. Run formalize-it first; a rule that is not written cannot be generalized.

James's definition (2026-11-08): "$formalize-it should make a rule out of whatever feedback is immediately beside the invocation from the perspective of DEFINING useful rules for ALL LLMs/agents regardless of context. It can also be invoked to double-triple dog dare x a million swear promise that something is extremely important for my own sanity or efficiency and therefore is arguably more important than getting decently acceptable results for a new feature."

Use this skill when James writes `$formalize-it`, and whenever any agent notices feedback, a correction or a repeated ask that should outlive the conversation.

## Workflow

1. **Take the feedback immediately beside the invocation**: the sentences before and after it in the same message. Quote them verbatim with the date. Do not paraphrase into the rule's voice; the quotation is the evidence, the rule is the reading.
2. **Write the rule for all agents regardless of context.** The subject is "an agent" or "every agent", never a project, a person's tool or a model name unless the rule is about that tool. One sentence that prevents the failure, then the check an agent performs before reporting done. A rule that only states an intention is rewritten until it names a check.
3. **Place it in the same turn**: a standards rule when it is jeby-wide (`standards/rules/`), a skill when it is behavior, a project ADR when it is product or architecture, plus a dated `DECISIONS.md` entry and a memory file for the main session. Chat is not a record.
4. **Second mode, the priority marker.** When the invocation marks something as critical to James's sanity or efficiency, record that in the rule's first line. Such a rule outranks feature quality from any model at any effort: an agent stops feature work to satisfy it, and a report that trades it for a better result is a defect (standards rule 00, "Rules over results").
5. **Test it**: the next case that matches the rule is checked against it out loud, and the result is added as an "Applied" line below. A rule that misfires stays in the file, marked as a bad bone with the corrected reading.

## Checks

- The quotation is present, dated and verbatim.
- The rule names no context it does not need (no project, machine, model or person unless essential).
- The rule names a check an agent can run before reporting done.
- The rule exists in a file, not only in chat, by the end of the turn.
- A priority-marked rule says so in its first line.

## Applied

- 2026-11-08: "My rules are unbreakable and drifting from them legitimately puts my status as a client in jeopardy, whereas getting unacceptable results from a high-resource model is almost automatically acceptable due to bad prompting by default." Became the lead of standards rule 00 (precedence) and DECISIONS.md 82. Check: rules touched are verified before result quality.
- 2026-11-08: "Ticket < Track < Project < company < jeby overall, while 'sprint' is more generalized and synced across libraries." Became DECISIONS.md 83, a line in standards rule 10, and the DESK hierarchy tickets. Check: a board or rollup that skips a level, or treats the whole store as "company", is a defect.
