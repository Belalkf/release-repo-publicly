# Checks and limits

The tests cover the history helper and the files people install. They check removed example secrets, tag messages, normal and linked repos, rejected inputs, incomplete history, byte limits and local links. They also copy the skill outside this checkout and run its helper there.

Run the commands in [setup](docs/setup.md#run-the-tests). The [GitHub checks](https://github.com/Belalkf/release-repo-publicly/actions/workflows/checks.yml) show results for each tested commit.

## What these tests do not show

A passing helper test does not show that an agent makes good choices, follows every instruction or completes a real release. Independent testing of that full process is still missing. Installing a skill only makes its instructions available to an agent.

The helper checks known patterns in local committed Git objects. It does not cover unsaved files, other people's clones, external Git LFS files or the contents of submodules. Git LFS stores large files outside normal Git objects; a submodule is a separate repo linked by the parent project. Binary files and other skipped content need a separate review. See the [history reference](skills/release-repo-publicly/references/private-to-public.md).

A clean report is useful evidence, not permission to publish or proof that no secret exists.
