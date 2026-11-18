# GitHub hosting

Choose settings for this project, then check that they are saved and working. A docs-only skill and an app do not need the same setup.

## Check current options

At each release or hosting review, read GitHub's current [security guide](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository), [repo settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features) and relevant [changelog](https://github.blog/changelog/) entries. Check changes that affect this account, code language, runner, runtime or install route. Follow useful findings to current feature and billing docs.

Compare that guidance with actual repo settings. In the release report or pull request, note the date, source, useful coverage and what was enabled or left off. Check costs and data access. Keep lasting policy in maintainer docs; avoid a new dated report unless someone needs it for a real review requirement.

Public repos often have standard hosted tests and security tools available. Verify the actual option before claiming it is free. Do not add a VM, service, paid AI feature or account-wide setting without a clear benefit and permission. A code scanner that uses AI can help ordinary code too; judge it by coverage, privacy and cost.

## Verify the destination

Check the owner, URL, visibility and remote commit just before writing. Preserve an original repo when the user asked for a separate copy. Use a public identity chosen for this release and review both author and committer email. Do not invent earlier development history.

Test setup from a fresh checkout and any installed command outside the source folder. Use standard hosted runners for the supported systems. Read actual job results, commit IDs and scanner findings. Separate passing tests from visual quality, human acceptance and release readiness.

## Keep contributions practical

Use active branch rules that block deletion and force pushes. Require pull requests, the right status checks against the current base, and resolved review conversations. Connect required checks to their real service when supported. Do not require a solo owner to approve their own change. Avoid a broad bypass that defeats the rule. Read back the active settings after saving.

Enable useful dependency alerts, security updates, secret scanning, push protection, private reporting and supported code scanning. Check malware-alert coverage where available. Keep workflow tokens read-only by default; do not let workflows approve their own pull requests. Require suitable approval for outside fork workflows. Pin reviewed actions, limit job duration and allow cancellation.

Use extra controls only for a real need. Deployment rules need a deployment; signed commits need a working signing route. Generic secret patterns may add noise, validity checks can contact providers, and AI repair may cost money. Leave automatic merging off unless requested.

## Review findings and updates

A green scanner job can still have alerts. Read the affected code and decide whether the issue is real. Fix bugs with regression tests. For a fake test token or an intentional local path, record why the finding is safe and when to revisit it. Never disable a query, language or merge check just to clear the dashboard.

Review task-related dependency requests, upstream changes and the oldest supported runtime. Newer build tools can drop old runtime support. Inspect and test the combined change against the current base, then merge suitable updates through the repo's rules. Explain an unsuitable update rather than merging it because it is newer. Do not touch unrelated requests.

After merging, check the remote commit, default-branch jobs, active rules and alerts. Preserve unrelated work and report real remaining limits.

References: [branch rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), [dependency review](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review), [CodeQL setup](https://docs.github.com/en/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configure-code-scanning), [malware alerts](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-malware-alerts), and [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions).
