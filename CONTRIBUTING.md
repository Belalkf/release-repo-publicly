# Contributing

Keep changes small enough to review. Use clear English and explain what a person will notice first. Keep each subject in one place and documentation paragraphs on one line.

Test with temporary example repos. Never add real credentials or private reports. Add a regression test for each bug fix: it should fail for the old bug and pass with the fix. The helper needs Python 3.9+ and installed Git, with no extra Python packages.

Run the checks in [setup](docs/setup.md#run-the-tests). GitHub repeats them with Python 3.9 and 3.14 on Linux, and Python 3.14 on macOS and Windows. These jobs test the helper and package, not the quality of an agent's choices.

Keep every local reference inside the installable skill folder. Put test logs in the pull request or GitHub Actions, and user-facing changes in [Changes](CHANGELOG.md).

## Hosting policy

Use pull requests and wait for the required test jobs. Resolve review comments before merging. Protect main from deletion and force pushes. A solo maintainer should not need their own approval to merge. Published release tags should stay fixed.

Keep workflow tokens read-only by default. Pin actions to reviewed commits, set job time limits and allow newer runs to cancel older ones. Enable useful secret and dependency checks where supported. Review alerts rather than treating a green job as proof that none exist. Do not enable paid features or account-wide changes without approval.

The tests place fake token strings in temporary repos and clean them up. A scanner may flag those strings. Check their use before closing an alert; never use real credentials as fixtures or disable a query just to hide a result.

Before changing settings, read current [GitHub security guidance](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository) and [branch rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets). Check what is actually enabled after saving. This policy is a goal, not a claim that a setting has been verified on a new repo.
