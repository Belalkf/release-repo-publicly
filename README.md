# Release Repo Publicly

Your project works on your machine. Is it ready for someone else?

This skill helps your coding agent turn a local project into a public GitHub repo that people can install and use. It checks the README, setup steps, files and Git history, then helps finish the release you asked for.

## Add it to your agent

Run this from your project:

```sh
npx skills add Belalkf/release-repo-publicly
```

Choose `release-repo-publicly` and your agent. Add `-g` to use it across your projects. You need Node.js 22.20 or newer for the [skills installer](https://github.com/vercel-labs/skills). The command downloads the installer and skill; it does not publish your project.

## Give it a task

For a first check:

> Use release-repo-publicly to get this repo ready for a public release. Keep everything local for now.

When you are ready to publish:

> Use release-repo-publicly to publish this repo on my GitHub account. Check the setup steps and finish the useful repo protections too.

In Codex, you can call it with `$release-repo-publicly`. The skill asks the agent to respect your chosen scope, keep private work safe and report what it actually checked.

## What it helps with

- A short README, clear setup steps and a small example.
- A check for private files and possible secrets in Git history.
- Tests and GitHub settings that fit the project.
- A final report with the release link and any checks still missing.

The optional history helper needs Python 3.9+ and Git. It checks for a few known patterns; a clean report does not prove that a repo is safe to publish. This skill is experimental: we have helper tests, but no full, independent test of an agent following the whole release process.

[Setup and helper](docs/setup.md) · [Checks and limits](VALIDATION.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [MIT licence](LICENSE)
