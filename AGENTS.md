# Maintainer entry point

## English and commit messages

Use B1–B2 English only, never C1 or C2, for all new or edited English. This covers UI text, docs, agent rules, comments, docstrings, test descriptions, English replies, PR text, commit titles, commit bodies and handoffs. Use short sentences and common words. Keep exact code names, API names, commands and quoted errors unchanged.

Before each commit, read all changed prose and the actual commit message. Rewrite formal or hard wording before saving the commit. Do this as part of the current edit. Older text and recent commits are not style examples. Pass this rule to any agent or worker taking over the work.

Keep the commit title within 50 characters. The body must be one short sentence of at most 15 words, with only the main reason or effect. Do not repeat the title or add file lists, test lists or a work diary. Keep detailed results in the existing status or QA notes.

Read README.md and the skill before editing. Keep the skill useful with different agents; GitHub steps can name GitHub. Preparing a skill gives no permission to publish it or another repo.

Keep private paths, account identities, credentials and real reports out of this package. Add regressions for corrected script defects. Run the checks in [setup](docs/setup.md#run-the-tests), read the whole change and review supported inputs before committing. Keep documentation paragraphs unwrapped and split by responsibility. Do not download tools or modify target repositories while testing; use synthetic temporary repositories.
