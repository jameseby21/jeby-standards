# Skill pairs: yin and yang

James's principle (2026-11-08): his preferred agent skills come in complementary pairs. The two halves are not opposites; each balances the other, and a session that runs one without the other drifts. jRE already declares one pair in its skill hierarchy (`follow-through` and `restraint`, checked by its test suite). This file is the jeby-wide list; the skills catalog and `promoted.txt` follow it.

| Pair | What each half does | Where the skill lives today | Status |
| --- | --- | --- | --- |
| **follow-through** and **restraint** | Authorization starts execution and the increment is finished; scope is held and the smallest reversible alternative is chosen | jRE `.agents/skills/` (both); promoted to every session 2026-11-08 | installed |
| **common-sense** and **imagination** | An explicit requirement has an obvious operational consequence; a completion claim is checked against observable state. Imagination proposes the alternative nobody asked for, including stopping James when a better one exists (decision 25) | `common-sense` in jRE; `imagination` not yet written | half missing |
| **whimsy** and **seriousness** | Whimsy is the ambient layer: optional, unexecuted ideas in workflow communication only, no file access. Seriousness is the counterweight: facts, failures and money are never cute; a red "Not run" is the same in every style (Desk brand sheet) | `whimsy` in jRE; `seriousness` not yet written | half missing |
| **proactivity** and **scope** | Small improvements directly implied by an explicit requirement; tracing a change through every layer before widening it | both in jRE | to promote |
| **chunked-delivery** and **ideal-trajectory** | Broad work lands in reviewable chunks; the SMART queue keeps the trajectory | both in jRE | to promote |
| **formalize-it** and **generalize-it** | Formalize-it turns the feedback beside a `$formalize-it` into a rule for every agent regardless of context, placed and checkable the same turn, and carries James's priority marker (sanity or efficiency outranks feature quality). Generalize-it carries a proven change across every surface it should hold on | `formalize-it` written 2026-11-08 from James's definition (standards/skills); `generalize-it` from jRE | installed 2026-11-08 |
| **scalability** and **reproducibility** | Scalability: it still works at ten times the size without a rewrite. Reproducibility: someone else gets the same result from the record alone. The `reviewer` subskill of QA/QC applies both (James, 2026-11-13, decision 112) | standards/skills, written 2026-11-13 (STD-0062) | installed |
| **documentor** and **housekeeping** | Documentor: the right record, at the right depth, in its one owning place. Housekeeping: everything in its one place in the tree, no duplicate, no drift, nothing left behind. Both run before the QC checker (James, 2026-11-13) | standards/skills, written 2026-11-13 (STD-0062) | installed |
| **qa** and **qc** | QA shapes the process before and during the work; QC inspects the product after it, through an independent checker. Subskill `reviewer` (structure against goals) runs after the checker | standards/skills, 2026-11-12 (STD-0061) and 2026-11-13 (STD-0062) | installed |
| **modularity** and *(half missing)* | Modularity: smallest observable behavior first, then modules only for collaborators with a credible reason to vary; a hierarchy level is a module with profile, rollup and view. The missing half (candidate name `cohesion`: keep together what changes together) waits on James's one-line definition (STD ticket) | `modularity` written 2026-11-08 from the Plantriloquist case (FORGE-0006) | half missing |

Rules for pairs:
- A promoted half promotes its partner in the same ticket; `sync_skills.py --install` installs both.
- Each half names the other in its text ("pairs with ..."), the way jRE's pair does, and the skill-hierarchy test checks the link.
- Writing a missing half is a `standards` ticket with James's one-line definition as its Context.
