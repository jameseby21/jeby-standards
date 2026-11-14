---
name: windows-pitfalls
description: "The traps met on this Windows computer and the check for each: Python text mode rewrites line endings, the name desk opens Display Settings (the tool is drew), quotes inside bash heredocs, relative interpreter paths in subprocess, locked git worktrees, paths over 260 characters, PowerShell 5.1 having no && operator, a running exe that cannot be reinstalled under itself, windows opened by servers, and headless browser profiles that must be removed by their recorded path. Use before running a command or script on this machine, before committing files written by a script, and when a command fails in a way that works elsewhere. Also useful when James writes $windows-pitfalls."
---

# Windows pitfalls: the traps already met on this computer, and how to see each one before it bites

Each trap below cost a session time or left a mess. Each has a check an agent can run. Related and not restated here: rule 60 and `housekeeping` (stop what you started by the recorded PID, remove temporary profiles and worktrees), `whats-running` (name the server, port and PID), `restraint` (deleting is a held step: print the exact path first), and `reproducibility` (a Windows run does not prove macOS).

**Case record:** these were met between 2026-11-08 and 2026-11-13. Rows for DESK-0019, DESK-0095, DESK-0132 and DESK-0171 are in `standards/lessons/LESSONS.md`; the other rules below come from those same sessions and still need their own lesson rows, which is the follow-up for this draft (rule 90: a failure becomes a rule and a test).

## Rules

1. **Python text mode rewrites LF as CRLF.** A script that writes a file with `open(path, "w")` on Windows turns every `\n` into `\r\n`, and the whole file shows as changed. Open files in binary mode (`"rb"`, `"wb"`) or with `newline=""` when you read and write, so line endings are kept as they were. PowerShell 5.1 `>`, `Out-File` and `Set-Content` can also add a byte-order mark or use another encoding; pass `-Encoding utf8` and check for it.
   **Check:** before every commit of a script-written file, `git ls-files --eol <file>` shows the same `i/` and `w/` ending (`i/lf w/lf` for a repository that stores LF), `git diff --cached --stat` shows a line count that matches the intended change (not the whole file), and `head -c 3 <file> | od -An -tx1` does not print `ef bb bf` unless the file always had one.
2. **`desk` on PATH opens Display Settings, so the tool is `drew`.** Windows ships `System32\desk.cpl`, which wins over the tool directory (lesson DESK-0019). Documents, briefs and commands use `drew`.
   **Check:** `Get-Command drew -All` resolves only to the uv shim; a search of the text you are about to send for a bare `desk ` command (`grep -n "desk board\|desk next"`) finds none outside a quoted old ticket. Before naming any new executable, `Get-Command <name> -All`.
3. **Single quotes inside a bash `'...'` string break the command.** A heredoc body or a string with an apostrophe, written inside single quotes, ends early. Use a quoted heredoc (`<<'EOF'`) so the body is taken as written, or write the file with the file tool and pass its path.
   **Check:** after the command runs, read the file or output back and confirm the line with the apostrophe is whole; for a script, `bash -n <script>` prints nothing.
4. **`subprocess` needs the full interpreter path.** A bare `python` or a relative `.venv\...` path resolves against whichever folder the process started in, or finds another install on PATH. Use `sys.executable` from Python, or the absolute path to the project's interpreter (for example the umbrella's `desk/.venv/Scripts/python.exe`).
   **Check:** run the script once from a different working folder; it still finds the interpreter. `grep -n "subprocess" <script>` shows no call whose first element is a bare `python`, `pip` or `uv`.
5. **`git worktree remove` can fail with Permission denied on locked `.git/worktrees` entries.** Do not delete the main repository or the `.git` folder to get past it. Leave the entry, run `git worktree prune` later, once the lock is gone, and remove the working folder only by its recorded path (rule 60).
   **Check:** `git -C <main repo> worktree list` after the clean-up shows only live worktrees, and `git -C <main repo> status --short` still works, so the main repository is intact. The report lists any worktree left behind and why.
6. **Paths over 260 characters fail to delete.** A deep scratchpad or checkout folder cannot be removed by an ordinary delete. From PowerShell, use the `\\?\` prefix with an explicit full path (`Remove-Item -LiteralPath '\\?\C:\...\the\exact\folder' -Recurse -Force`), only after printing that path and confirming it is under the session scratchpad or a path you recorded, never from a variable that could be empty, never with a wildcard.
   **Check:** print the path and `Test-Path -LiteralPath <path>` before; after the delete, `Test-Path -LiteralPath '\\?\<path>'` prints `False`, and the parent folder still exists.
7. **PowerShell 5.1 has no `&&` or `||`.** A command line with `&&` is a parse error there. Chain with `;` and test `$?`, for example `A; if ($?) { B }`, or run the line in the Bash tool.
   **Check:** search the PowerShell command you are about to run for `&&` and `||`; none. If the command was written for Bash, run it in Bash.
8. **A running exe cannot be reinstalled under itself.** Reinstalling a tool while its server runs leaves old modules under new templates (lesson DESK-0095) or an uninstalled tool (lesson DESK-0132, `uv tool install --force` run from the exe inside the folder uv removes). Updates go through `drew upgrade` or `drew refresh`, which hand the install to a detached process outside the folder; the owner's own running Desk is stopped by an agent only to install a change he asked for (skill `release`, rule 1), with the rollback written first and the restart named in the report (rule 60 otherwise).
   **Check:** before an upgrade, find what is running by recorded PID or by port (`Get-NetTCPConnection -LocalPort 8765`), and say whose it is. After, `drew doctor` exits 0 and names the commit. A failed update prints the one command that restores the old install, and the Report quotes it.
9. **A server or browser an agent starts runs windowless.** One hidden process (`-WindowStyle Hidden` or `pythonw`), serving what it can from one process, PID written down, stopped by that PID (lesson of 2026-11-08: two preview servers in two console windows). A visible window is opened only when the owner must type into it.
   **Check:** before ending the turn, list console windows owned by processes the session started: zero, or each named with why it stays (`housekeeping`, `whats-running`).
10. **A headless browser profile is removed by its recorded path.** A test or check that starts a headless browser uses a temporary profile whose name carries the starter's own PID, records the path when it starts, and deletes that exact path afterwards, even when the test fails. It never matches by name prefix (lesson DESK-0171).
   **Check:** the recorded profile path no longer exists (`Test-Path -LiteralPath <path>` is `False`), no browser process whose PID the session recorded is alive, and the commands contain no `Stop-Process -Name` or `taskkill /IM`.

## Check before done

- Every script-written file passed rule 1's check before it was committed.
- No command in the reply uses `desk` (the tool is `drew`), `&&` in PowerShell, or a bare interpreter name in `subprocess`.
- `git worktree list` shows no stale entry from this session, or the report names it and the `git worktree prune` step.
- Each deletion by a long path or a profile path names the exact path and was confirmed gone.
- Nothing the session started on a port, in a window or as a headless profile remains, except what the reply lists with PID, port and reason.

## Applied

- 2026-11-08: the `desk` collision (DESK-0019) gave the tool its `drew` alias; the upgrade that removed the running exe (DESK-0132) gave the detached hand-off; the preview servers in two windows gave the windowless rule.
- 2026-11-13: this skill gathers those and the later traps (line endings, quotes, relative interpreters, locked worktrees, long paths, `&&`) in one place so a session checks them before the command, not after the damage.
