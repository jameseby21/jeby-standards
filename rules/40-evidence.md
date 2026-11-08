# Evidence

- Claimed is not run. A Report names the command, where it ran (machine, OS, directory) and what it printed. Anything not run is marked "Not run", in red on screen, never silently omitted.
- A mocked test is test coverage, not runtime proof. A 200 response proves transport. A Windows run does not prove macOS. A schema does not prove a feature.
- Stop on a red gate. Do not build on a failing suite or report evidence that was not produced.
- Every fix buries a bone: the rule that prevents the failure and the test that proves the rule, recorded in `standards/skills/` or the project's lessons doc, so the next ticket that smells the same finds it.
