# Lessons (bones): the rule and the test that keep a failure from happening twice

| Date | Born from | What went wrong | Rule | Test | Reaches |
| --- | --- | --- | --- | --- | --- |
| 2026-11-08 | DESK-0019 | Typing `desk` in PowerShell opened Display Settings: Windows ships `System32\desk.cpl`, which wins over uv's tool directory on PATH. | Before naming an executable, check the name on every target OS (`Get-Command <name> -All` on Windows, `type <name>` on macOS/Linux) and ship a collision-free alias. | A test that `Get-Command drew -All` resolves only to the uv shim; a README note per OS. | every project that installs a command |
