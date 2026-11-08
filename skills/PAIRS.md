# Skill pairs: yin and yang

James's principle (2026-11-08): his preferred agent skills come in complementary pairs. The two halves are not opposites; each balances the other, and a session that runs one without the other drifts. jRE already declares one pair in its skill hierarchy (`follow-through` and `restraint`, checked by its test suite). This file is the jeby-wide list; the skills catalog and `promoted.txt` follow it.

| Pair | What each half does | Where the skill lives today | Status |
| --- | --- | --- | --- |
| **follow-through** and **restraint** | Authorization starts execution and the increment is finished; scope is held and the smallest reversible alternative is chosen | jRE `.agents/skills/` (both); promoted to every session 2026-11-08 | installed |
| **common-sense** and **imagination** | An explicit requirement has an obvious operational consequence; a completion claim is checked against observable state. Imagination proposes the alternative nobody asked for, including stopping James when a better one exists (decision 25) | `common-sense` in jRE; `imagination` not yet written | half missing |
| **whimsy** and **seriousness** | Whimsy is the ambient layer: optional, unexecuted ideas in workflow communication only, no file access. Seriousness is the counterweight: facts, failures and money are never cute; a red "Not run" is the same in every style (Desk brand sheet) | `whimsy` in jRE; `seriousness` not yet written | half missing |
| **proactivity** and **scope** | Small improvements directly implied by an explicit requirement; tracing a change through every layer before widening it | both in jRE | to promote |
| **chunked-delivery** and **ideal-trajectory** | Broad work lands in reviewable chunks; the SMART queue keeps the trajectory | both in jRE | to promote |

Rules for pairs:
- A promoted half promotes its partner in the same ticket; `sync_skills.py --install` installs both.
- Each half names the other in its text ("pairs with ..."), the way jRE's pair does, and the skill-hierarchy test checks the link.
- Writing a missing half is a `standards` ticket with James's one-line definition as its Context.
