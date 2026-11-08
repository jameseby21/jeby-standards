# Reuse first, create only if necessary, close what you open

James's global rule (`~/.claude/CLAUDE.md`) applies in every repo: reuse running processes, windows and installs; start new ones only when the task needs them; stop everything you started by its recorded process ID; leave the user's own things alone; tests use temporary folders and clean up; report what was opened and that it is closed.

Code reuse follows the same rule: before writing a module, look for it in the standards skills library, the umbrella's shared code and the sibling repos. One source of truth per project, `main` is it, and paid editions depend on the free edition instead of forking it (umbrella `docs/EDITIONS.md`).
