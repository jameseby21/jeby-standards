---
name: reproducibility
description: Make every result redoable by someone else from the record alone - the inputs, the exact commands, the versions, the environment and the expected output are written where the result lives. Use when reporting a number, a test result, a build, a data pull, a model run, a folder move or a decision, and when James writes $reproducibility. Pairs with scalability; the reviewer subskill of QA/QC applies both.
---

# Reproducibility: someone else gets the same result from the record alone

**Pairs with `scalability`.** Reproducibility makes a result redoable; scalability makes it still work at ten times the size. The `reviewer` subskill of QA/QC applies both.

> "Success for any of my individual projects will at least partially be scored by finding solutions to repeatable and periodic processes, with or without user acceptance." (James, 2026-11-09, decision 94)
>
> "want you to confirm that all these, plus $ reproducibility, are all official skills with non-trivial definitions and rules." (James, 2026-11-13)

## Rules

1. **Inputs are named and pinned.** A file by path and commit or hash; a dataset by source, date and version; a tool by version (`drew doctor`, `python --version`).
2. **The exact command, where it ran, and what it printed** (rule 40). A paraphrase of a command is not a command.
3. **Randomness is seeded, and the seed is recorded.** Large jobs run a seeded random sample before the whole job (rule 90).
4. **The baseline is reproduced before anything changes.** Re-run the original, match it, then change it (failure catalog E4).
5. **Every move has an undo log:** old path, new path and time, in an order that can be replayed backwards.
6. **No step lives only in a chat or a session's memory.** If a newcomer would have to ask "how did you get that?", the record is missing a line (rule 20: write for the reader who was not in the conversation).
7. **Environment differences are stated.** The machine, OS and folder are named; a Windows run does not prove macOS (rule 40).
8. **Generated facts are generated.** Counts, versions and inventories come from a script that can be re-run, never typed by hand (rule 90).

## Check before done

- Pick one result in the reply and redo it from the record alone, in a fresh shell, from the stated inputs. It matches, or the reply marks it "Not reproduced".

## Applied

- 2026-11-13: pass 2 recorded its baseline (`drew stats`: 1,514 open of 1,743) before filing any ticket; its candidate finder is a re-runnable script (intake/2026-11-13-pass-2/tools/prepare.py); the Drive rename has an undo log.
