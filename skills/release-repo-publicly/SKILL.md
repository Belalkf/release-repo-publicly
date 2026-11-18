---
name: release-repo-publicly
description: Help prepare or publish a project on GitHub so other people can use it. Use for a public release, a clean public copy, or a review of an existing release. Covers setup, private-data checks, tests and repo settings. Do not use for ordinary commits, app deployment or package-registry uploads.
---

# Release Repo Publicly

Help someone else install and use the project. Finish the release the user asked for, and show what was checked. A push alone is not a finished release.

## Agree on what goes public

Read the repo's rules, current Git state and active work notes. Find the source, target account and target repo. Check whether the user asked for local preparation, publication, or both. Installing this skill grants no permission to publish.

Use the connected account and a suitable service tool, signed-in CLI or browser. Keep credentials out of files, logs and commits. Leave unrelated repos and account-wide settings alone. Preserve the original when the user wants a separate public copy.

If the product choice is still open, compare current tools and their licences first. Explain who this helps and what it adds. Prefer improving an existing tool when a new one has no clear benefit. Do not invent claims about speed, popularity or quality.

## Make the first use work

Write a short README: what the project does, how to install it and one small example. Put detailed setup and limits in the right existing docs. Explain needed terms and use examples with no private data.

Try the setup and common task from a fresh checkout outside the author's workspace. Check the oldest supported runtime, packaged files and required tools. As relevant, check bad inputs, cancellation, existing-file safety and clear failure messages. Preserve useful support even when a wider feature is out of scope; state the exact limit.

Add a licence only when the author has the right to use it. Include support and security-reporting routes. Keep test logs in CI or the release report, not a growing diary. Use release notes for changes people will notice.

For tools that build prompts, separate measured facts from model opinions. Write common instructions once. Optional detail can be hidden, but never hide missing safety coverage from the copied request.

For agent skills, read [skill packages](references/skill-packages.md). It covers who the skill helps, installation and evidence for agent behaviour. Use the host's existing skill creator when needed; do not build another one to release this skill.

## Check the public files and history

For a separate public copy, follow [private-to-public](references/private-to-public.md). Review the exact files, reachable Git history, commit names and emails, deleted files, images and archives that will be shared. Preserve licence notices. Use a fresh history only for the new copy the user requested; never invent a past timeline.

Use `python3 scripts/audit_history.py PATH` from this skill folder when useful. It reads local committed history, reports pattern types and object IDs, and never prints possible secret values. It does not fetch, upload, change history or prove that all private data is gone. Review findings locally and check excluded files separately.

If a real secret was published, arrange its removal or rotation first through an approved route. Deleting a commit cannot remove other people's copies. Do not rewrite public history for an ordinary fix.

## Publish and check the result

Read [GitHub hosting](references/github.md). Check current official guidance and recent relevant changes before choosing settings. Compare them with the actual account and repo. Do not turn on every option or add paid services without approval.

Check the destination again just before writing. Stop if it has changed unexpectedly; do not overwrite another person's update. Create a separate public repo when the requested name would otherwise replace an original.

Run useful hosted checks on the supported systems. Set sensible branch rules, secret and dependency checks, private reporting and read-only workflow defaults. A solo maintainer should not need to approve their own changes. Check the saved settings and actual job results; a workflow file or enabled scanner proves no successful scan.

Review task-related dependency updates against the current base and supported runtimes. Merge only suitable changes through the repo's rules. Leave automatic merging off unless requested.

## Finish with evidence

Review the full change and the ordinary first-use journey. Fix in-scope bugs, add regression tests and rerun the affected checks. Keep long-running jobs owned, time-limited and cancellable; clean them up when done.

Report the public link or prepared local folder, exact published commit, checks that ran and concrete missing checks. Separate working behaviour, missing features and things still unverified. Keep going while useful authorized work is ready. Stop at completion or a real access, safety or resource limit, with the smallest next action stated clearly.
