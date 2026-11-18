# Setup and the history helper

## Install scope

`npx skills add Belalkf/release-repo-publicly` adds the skill to the current project. Add `-g` for your user account. Use `--list` to see the skill before installing it. The [installer docs](https://github.com/vercel-labs/skills) explain supported agents, Node.js requirements and telemetry controls.

The installable folder is [skills/release-repo-publicly](../skills/release-repo-publicly/SKILL.md). It includes all the skill's local references and its helper. Installing these instructions does not install Python or Git. Restart or refresh your agent if it does not find the new skill.

For a local checkout, use the installer with its path:

```sh
npx skills add ./ --skill release-repo-publicly
```

Run that command from this repo. Choose your agent and check the proposed destination before accepting it. Keep an existing skill if it has local changes.

## Try the helper

The helper reads committed local Git history. It does not upload files, fetch missing objects or change the repo. Try it on a temporary example first:

```sh
demo="$(mktemp -d)"
git -C "$demo" init -q
git -C "$demo" -c user.name="Example maintainer" -c user.email="fixture@users.noreply.github.com" commit --allow-empty -qm "Example"
python3 skills/release-repo-publicly/scripts/audit_history.py "$demo"
```

Expect `complete: true` and an empty findings list. Remove the temporary folder when you are done. The helper returns a nonzero exit code when it finds a pattern or cannot finish a check. It never prints the possible secret itself.

Pass the repo root, not a folder inside it. Normal repos, bare repos and linked worktrees are supported. A bare repo stores Git data without a working copy. A worktree is another checkout that shares a repo's history.

See [history checks](../skills/release-repo-publicly/references/private-to-public.md) for limits and rejected inputs.

## Run the tests

From this checkout, with Python 3.9+ and Git:

```sh
python3 -m unittest discover -s tests -v
python3 skills/release-repo-publicly/scripts/audit_history.py .
```

Run the history check after making a local commit. Tests use temporary example repos, not private projects. A format check can confirm the skill's metadata; it cannot confirm an agent's decisions.
