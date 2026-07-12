# AI Second Brain Stage 3 for Obsidian + Hermes

Use this reference after Stage 1 structure/metadata and Stage 2 operational workflows are in place.

## Goal

Turn the vault from a static knowledge base into a reviewed operating system by adding recurring review loops and scheduled Hermes jobs.

## Stage 3 implementation pattern

1. Inspect current review notes, templates, dashboards, and existing cron jobs first.
2. Create a timestamped vault backup before edits.
3. Add review templates:
   - `60_Templates/Weekly Review.md`
   - `60_Templates/Project Review.md`
4. Add a global review dashboard:
   - `10_Dashboards/Review Dashboard.md`
5. Add an automation registry note:
   - `70_System/Hermes/Review Automation Schedule.md`
6. Update dashboards/indexes with links to the review system:
   - Home dashboard
   - `70_System/System Index.md`
   - `70_System/Hermes/README.md`
   - active project dashboards
7. Create recurring Hermes cron jobs only after checking that equivalent jobs do not already exist.
8. Record job IDs, schedules, next runs, delivery target, write paths, and guardrails in the automation registry.
9. Verify cron list, expected files, valid YAML/frontmatter, `.base` YAML, and wikilinks.

## Recommended initial jobs

Keep the initial automation light. Two jobs are usually enough:

### Weekly Vault Review

- Schedule: Mondays 09:00 UTC unless the user gives a preferred timezone/cadence.
- Writes: `01_Daily/Weekly Reviews/Weekly Review YYYY-WW.md`
- Workflow: `70_System/Hermes/Weekly Review Workflow.md`
- Toolsets: `file`, `terminal`, `skills`
- Skill: `obsidian`
- Delivery: `origin`

### Weekly Project Review

- Schedule: Fridays 16:00 UTC unless the user gives a preferred timezone/cadence.
- Writes: `Projects/<Project>/Reviews/Project Review - <Project> - YYYY-MM-DD.md`
- Workflow: `70_System/Hermes/Project Review Workflow.md`
- Toolsets: `file`, `terminal`, `skills`
- Skill: `obsidian`
- Delivery: `origin`

## Cron prompt requirements

Scheduled prompts must be self-contained because they run in a fresh session.

Each prompt should include:

- absolute vault path;
- exact workflow note path;
- exact destination note path pattern;
- explicit “do not ask questions” instruction;
- explicit “do not create/update/remove cron jobs” instruction;
- guardrails against moving, deleting, archiving, or bulk-normalizing notes;
- verification requirement for created review note and YAML frontmatter;
- concise final Telegram report format.

## Pitfalls

- Do not create duplicate cron jobs; always list existing jobs first.
- Do not overschedule at the start. Daily digests can create notification fatigue.
- Cron jobs run without current chat context, so prompts must not rely on prior conversation.
- Store job IDs in the vault registry note so they can be paused/updated/removed later.
- If cron schedules use UTC, say so clearly; user-local timezone can be changed later.
- Do not run scheduled jobs immediately unless explicitly useful; creation + next-run verification is enough for setup.
