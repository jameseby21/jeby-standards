---
name: release
description: "Built is not delivered. A change the owner asked for reaches the instance he actually uses within one day of being built, or its ticket's blocked_on says what stops it and who acts. Covers the merge backlog in every pass report, retargeting stacked pull requests, the revert command written before the merge, the live check after it, website changes shipping behind the basic security check and nothing else, and a feature asked for three times being an emergency. Use whenever a pull request is opened, reviewed, merged or installed, at the close of every pass, and when James writes $release. Pairs with delegation."
---

# Release: built is not delivered

**Pairs with `delegation`.** Delegation gets the work built by a worker with a time box; release gets what was built onto the screen the owner looks at. A worker that reports "pull request opened" has finished its half, not the whole. Related and not restated here: `whats-running` (naming what is running and checking links), `housekeeping` (installed versus repository, failure catalog B1 and B2).

> "So is a visual way of seeing a ticket's timeline and events within it" (James, 2026-11-13, listed among the things to fix immediately; the third ask for it, after decisions 75 and 86)

> "website changes should be purposefully less stringent and "ship immediately" type of changes (within reason, and always passing at least a basic $security check -- which is to be defined by [the security owner] to be extremely safe but not all-blocking)" (James, 2026-11-13, SEC-0020)

**Case:** the ticket timeline was asked for on 2026-11-08 (decision 75), again on 2026-11-09 (decision 86, "second ask"), and a third time on 2026-11-13. It was built the first day. Its pull request was stacked inside another, then more pull requests were stacked on top, and each pass report listed the chain for the owner to merge. His installed Desk never showed it; only a preview on another port did (MGMT-0053, lessons B1 and B2). By 2026-11-13 there were 37 open pull requests across the repositories.

## Rules

1. **One day from built to where the owner looks.** A change the owner asked for is on the instance he uses (his installed Desk on port 8765, the live site, the installed tool) within one day of being built. If not, the ticket's `blocked_on` names what stops it and who acts (a credential, a merge he reserved, a failing review gate), per skill `not-a-blocker`. "Built, in review" is not a reason.
   **Check:** for each ticket the owner asked for that is in `review` or `done`, compare the build date with the date the owner's instance first showed it (`drew doctor` for the installed commit; `curl` for the live site). Older than a day with an empty `blocked_on` is a defect, listed in the pass report.
2. **The merge backlog is a number in every pass report.** State, per repository, how many pull requests are open and the date of the oldest. The rule that every pass report carries it lives in `whats-running`; this is how to count it.
   **Check:** `gh pr list --repo <repo> --state open --json number,createdAt --jq 'length, (min_by(.createdAt)|.createdAt)'` for each repository the store touches. The report's numbers equal the command's output, and the oldest date is under seven days or has a stated reason.
3. **Stacked pull requests are retargeted to main as soon as their base merges.** A base branch is not deleted on merge in these repositories, so GitHub does not retarget the pull requests above it, and they keep pointing at a branch that already merged.
   **Check:** after every merge, `gh pr list --repo <repo> --state open --json number,baseRefName --jq '.[]|select(.baseRefName!="main")'` prints nothing, or each line is a stack the report names with the order it will merge in. Retarget with `gh pr edit <n> --base main`; where `gh` is missing, use `git` (rule 10, tool check first).
4. **The revert command is written before the merge.** The ticket's Report holds the line "Rollback:" with the exact command and the commit it returns to, taken from `git rev-parse origin/main` before the merge (Desk: `drew refresh --ref <that sha>`; a site: `git revert -m 1 <merge sha>`).
   **Check:** the ticket has a Rollback line written before the merge time, and `git cat-file -e <sha>` succeeds for the commit it names.
5. **The live or installed instance is checked after the merge, not the branch.** A merge is not proof that the thing runs.
   **Check:** website, `curl -s -o /dev/null -w "%{http_code}" <live url>` prints the expected code and the page contains the changed text (`curl -s <url> | grep -c "<new text>"` is not 0); Desk, `drew doctor` exits 0 and names the merged commit, then open the changed page on http://127.0.0.1:8765. The Report states which instance was checked and its commit (lesson DESK-0082).
6. **Website changes ship behind the basic security check (SEC-0020) and nothing else that rule 28 does not already require.** A copy, style or content change needs only the check; a new user-facing feature still has its design ticket and review gates (rule 28), which were opened when the feature was filed, not at ship time. No added review round, preview approval or waiting step on top of those. The check blocks only real danger and lets everything else ship. Until the security owner signs it, the provisional check in SEC-0020 is in force.
   **Check:** the ticket carries the check's output (the diff scanned, the result), and no other open review ticket is named as the reason a website change has not shipped. A website change older than a day with a clean check output is a defect.
7. **A feature asked for three times is an emergency, and a second ask already is (rule 10).** The second ask makes the ticket p0 with tag `emergency` and the delivery goes ahead with what is present; the third opens triage that closes only with a rule or skill change.
   **Check:** before closing any pass, `drew search` the owner's request wording and `grep` DECISIONS.md for the same feature; a second hit with the ticket not p0, or a third hit with no triage ticket, is a defect.
8. **Merges that need none of the owner's credentials are the main session's to make once the review gate passes; the owner reviews after, and everything is revertible.** This reading of his words of 2026-11-13 is recorded as decision 114 and awaits his confirmation; until he confirms or narrows it, it applies to website changes he asked to see live and to the three-times-asked timeline (MGMT-0053), and rule 50 (branch per ticket, no force-push to main) holds throughout. Anything that does need his credentials, body or judgment is a `blocked_on` line with that reason.
   **Check:** each merge in the report names the review gate that passed and the Rollback line of rule 4.

9. **A harness refusal is named as such.** When the session's own permission layer refuses a publish or merge command, the report names the command, says it was the harness, and gives the permission rule that lifts it (for example a Claude Code Bash allow rule for `gh repo edit`). It is never worded as a decision for the owner, because the decision was already made (lesson JRE-0363, 2026-11-13).
   **Check:** no ticket's `blocked_on` reads "James decides" when the cause was a refused command.

## Check before done

- The pass report opens with the backlog line of rule 2, then lists any change built more than a day ago and not on the owner's instance, each with its one step.
- Every merge in the report has a Rollback line and a post-merge check output (rules 4 and 5).
- `gh pr list --state open` shows no pull request whose base branch has merged.
- No ticket the owner asked for sits in `review` with an empty `blocked_on` for more than a day.

## Applied

- 2026-11-13: MGMT-0053 opened as the third-ask triage for the ticket timeline. Its planned fix is to merge the Desk chain to main in order, retarget the pull requests above it, run `drew refresh`, and confirm the timeline on the owner's own port, with `drew refresh --ref ec6bcfd` as the written rollback; at the time of writing those steps are planned, not run. The 37 open pull requests on 2026-11-13 is the first backlog figure this skill asks for.
