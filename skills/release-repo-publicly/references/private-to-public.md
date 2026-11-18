# Make a separate public copy

## Choose the files

When the user asks for a new public edition, use a fresh destination and preserve the original. Copy the chosen source, needed tests and assets, plus licence notices. Leave out `.git`, credentials, caches, private reports, real-project screenshots and workspace-only instructions. Review later fixes before copying them across.

Before the first push, review every branch and tag that will be public. Check root commits, deleted files, commit messages, author and committer emails, shared Git object stores and linked worktrees. An ignored file may still exist in old commits. Review image content and metadata, archives and external large files separately.

Do not change the original repo's remote or visibility. Check both the new public repo and the original after publication. Fresh history in a new repo does not remove the older public repo or copies held by other people.

## Run the local history helper

From the skill folder, run:

```sh
python3 scripts/audit_history.py /path/to/repo
```

The helper uses installed Python and Git. It is read-only, with a 60-second total limit and 10-second Git-call limits. It checks up to 5,000 reachable objects, 2 MiB per content object and 32 MiB of content in total. Git lists the object metadata before the object limit is applied.

It checks UTF-8 file content, commit messages and identities, and annotated-tag text for a few known patterns. Findings show the type and object ID, never the possible secret. Review each finding locally. Public contact details and fake test tokens may need no repair; a real credential does.

### Supported inputs

Pass the selected repo's root. Normal repos, linked worktrees and bare repos are supported. The helper ignores Git replacement objects. A shallow repo has missing earlier history, so the report is incomplete.

The helper rejects legacy graft files because they can hide earlier commits. It also rejects partial-clone settings, including included config files. Partial clones can download Git objects later; this helper disables that download route and all Git transports as an extra guard. It never repairs the input. Use a separately approved full clone or review an unsupported case manually.

### What remains outside the check

Only local reachable Git objects are read. The check excludes remote-only objects, old server refs, pull-request caches, forks, other people's clones, Git reflogs and unreachable objects. File names in Git trees also need a separate review.

Unsaved files, submodule content and external Git LFS files are outside this pass. Binary, oversized or unreadable objects remain marked as unreviewed. A completed pass means only that the supported check finished; it is not permission to publish or proof that no secret exists. This helper expects trusted local Git settings and is not a sandbox for hostile repos.

## If a secret was shared

Revoke or rotate the credential through the approved account route first. History cleanup needs its own permission and coordination. A deleted commit cannot recall copies. Follow [GitHub's sensitive-data guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

Git references: [partial clones](https://git-scm.com/docs/partial-clone), [repo layout and grafts](https://git-scm.com/docs/gitrepository-layout), and [Git transport controls](https://git-scm.com/docs/git).
