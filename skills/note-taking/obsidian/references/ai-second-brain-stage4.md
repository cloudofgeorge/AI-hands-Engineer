# AI Second Brain Stage 4 for Obsidian + Hermes

Use this reference after Stage 1 structure/metadata, Stage 2 operational workflows, and Stage 3 review automation are in place.

## Goal

Turn the vault into a live capture system: raw Inbox capture, safe triage, source capture, and research queue processing.

## Stage 4 implementation pattern

1. Inspect current Inbox, templates, capture workflows, dashboards, and cron jobs first.
2. Create a timestamped vault backup before edits.
3. Add capture/source templates:
   - `60_Templates/Inbox Item.md`
   - `60_Templates/Source.md`
   - `60_Templates/Evergreen.md`
   - `60_Templates/Triage Report.md`
4. Add capture workflow notes:
   - `70_System/Hermes/Capture Pipeline Workflow.md`
   - `70_System/Hermes/Inbox Automation Workflow.md`
   - `70_System/Hermes/Research Capture Queue Workflow.md`
   - `70_System/Hermes/Capture Routing Rules.md`
   - `70_System/Hermes/Capture Automation Schedule.md`
5. Add dashboards/index folders:
   - `10_Dashboards/Capture Dashboard.md`
   - `00_Inbox/Captures/README.md`
   - `00_Inbox/Triage Reports/README.md`
   - `40_Resources/Sources/README.md`
   - `40_Resources/Research/README.md`
   - `40_Resources/Evergreen/README.md`
6. Update Home, System Index, Hermes README, Inbox, Resources, Operating Manual, Inbox/Research workflows, and active project dashboards with capture links.
7. Create recurring Hermes cron jobs only after checking for duplicates.
8. Record job IDs, schedules, next runs, delivery target, write paths, and guardrails in `Capture Automation Schedule.md`.
9. Verify cron list, expected files, valid YAML/frontmatter, `.base` YAML, and wikilinks.

## Recommended initial jobs

Keep Stage 4 conservative and non-destructive.

### Inbox Triage Digest

- Schedule: Tuesdays and Thursdays 08:30 UTC unless user prefers another cadence.
- Writes: `00_Inbox/Triage Reports/Inbox Triage - YYYY-MM-DD.md` only when useful.
- Workflow: `70_System/Hermes/Inbox Automation Workflow.md`
- Toolsets: `file`, `terminal`, `skills`
- Skill: `obsidian`
- Delivery: `origin`
- Guardrail: do not modify original Inbox captures in scheduled mode.

### Research Capture Queue

- Schedule: Wednesdays 10:00 UTC unless user prefers another cadence.
- Writes: source notes under `40_Resources/Sources/` and/or digest notes under `40_Resources/Research/`.
- Workflow: `70_System/Hermes/Research Capture Queue Workflow.md`
- Toolsets: `file`, `terminal`, `skills`, `web`
- Skill: `obsidian`
- Delivery: `origin`
- Guardrail: process at most 5 public URLs per run; skip private/authenticated links.

## Cron prompt requirements

Scheduled prompts must be self-contained because they run in a fresh session.

Each prompt should include:

- absolute vault path;
- exact workflow note paths;
- exact destination note path pattern;
- explicit “do not ask questions” instruction;
- explicit “do not create/update/remove cron jobs” instruction;
- guardrails against moving, deleting, archiving, overwriting, or bulk-normalizing notes;
- instruction to keep original Inbox captures intact;
- verification requirement for created notes and YAML frontmatter;
- concise final Telegram report format.

## Pitfalls

- Do not over-automate capture. Scheduled jobs should suggest routing or create new notes, not silently reorganize the user's vault.
- Do not modify raw Inbox captures from cron jobs; preserving originals makes automation auditable.
- Do not fetch private/authenticated URLs automatically.
- Do not create source notes for URLs that already exist in the vault with the same `source_url`.
- Avoid daily notification fatigue; start with 2x/week Inbox triage and 1x/week research queue.
- Store job IDs in the vault registry note so they can be paused/updated/removed later.
