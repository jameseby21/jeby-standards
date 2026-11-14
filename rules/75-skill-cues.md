# Skill cues: `$name` invokes a skill or asks for one

James's rule (2026-11-08): "I will use the dollar sign '$' to invoke a skill or cue you to create one if a similar one doesn't already exist. This will require you to explicitly look up the skill rules and often refine them based on what's next, or at the very least treat them as a test case for whether or not the skills system and definitions work."

- `$name` in a message from James means: load that skill's rules and apply them to what is being discussed, out loud: name the rule that applies and the check it produces. If no skill of that name or a close one exists, write it (a `standards` ticket, Context = his one-line definition, then the SKILL.md) before continuing.
- Every `$` invocation is a test of the skill system: if the rules did not produce the check James expected, the skill is refined in the same turn (an "Applied" line with the case, or a sharper rule), and the refinement rides to the standards repo on a branch.
- Skills exist to improve development and to prevent unclarified or suboptimized issues; a skill that only restates good intentions is rewritten until it names a check.
- Applied cases are kept short in the skill file (one line each, dated) and in full in `standards/lessons/` when they came from a failure.
