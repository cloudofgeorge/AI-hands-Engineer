# Scheduled Obsidian Project Review Pattern

Use this reference when a scheduled cron prompt asks for an autonomous project review in an Obsidian vault.

## Trigger

- Scheduled/autonomous project review for a named project.
- Prompt provides a vault path, workflow note, automation registry, destination note pattern, and final delivery constraints.
- User explicitly forbids cron changes and broad vault cleanup.

## Workflow

1. Resolve the run date with a tool; use that date in the destination note filename.
2. Read the configured workflow note and automation registry.
3. Read the project dashboard, canonical project note, task board, launch/checklist notes, context pack, architecture index, plans/specs/decisions/research folders, and recent review notes where present.
4. If source repositories are listed in notes, inspect live repo state before making claims:
   - branch/upstream status;
   - recent commits since the prior review;
   - dirty/staged/unstaged summaries;
   - presence/absence of relevant workflow or release files when launch readiness is in scope.
5. Summarize task/checklist counts when useful. A tiny Python script is fine for counting `- [ ]` and `- [x]` lines.
6. Write or update the dated review note with valid frontmatter.
7. Verify by reading the destination note back and checking:
   - file exists;
   - first line is `---`;
   - closing frontmatter delimiter exists;
   - required keys such as `type`, `project`, `status`, `created`, `updated`, `tags` are present;
   - title matches the run date.
8. When the only changed artifact is a Markdown review note and there is no canonical lint/test/build command, run an ad-hoc verifier instead of leaving the workspace unverified:
   - create a temporary script under `/tmp` using `tempfile` with filename prefix `hermes-verify-`;
   - validate frontmatter delimiters, required metadata keys, expected title/sections, unresolved placeholders such as `YYYY-MM-DD`, and guardrail phrases such as no cron changes / no bulk cleanup;
   - run it against the destination note;
   - clean up the temporary script when possible;
   - report this as **ad-hoc verification**, not as suite green.
9. Final external response should be terse and should not include the full review body.

## Review note shape

```markdown
---
type: project-review
project: "[[Project Name]]"
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - project-review
  - project-slug
  - scheduled-review
---
# Project Review - Project Name - YYYY-MM-DD

## Executive summary
## Current status
## Progress
## Open tasks
## Blockers
## Risks
## Decisions needed
## Recommended next actions
## Notes to clean up
## Files inspected
## Verification
```

## Guardrails

- Do not create, update, pause, resume, or remove cron jobs.
- Do not move, delete, archive, rename, or bulk-normalize notes.
- Write only the requested destination review note unless the prompt explicitly allows more.
- Report cleanup opportunities as recommendations only.
- Do not claim macOS/Xcode verification from a Linux cron context; state the blocker plainly.
- Do not expose secrets from env files, deployment scripts, keychains, certificates, or provisioning profiles.

## Final response pattern

Keep the final report under the requested delivery limit. Include only:

```text
Status: yellow.
Note: /absolute/path/to/review.md
Top 3 next actions/blockers:
1. ...
2. ...
3. ...
Decisions needed: ...
```

If nothing material changed, say so briefly and point to the note path. If blocked, report the blocker and any partial note path created.
