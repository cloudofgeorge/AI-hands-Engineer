# AI Second Brain Stage 1 for Obsidian + Hermes

Use this reference when the user asks to organize an Obsidian vault as an AI-assisted second brain.

## Best-practice shape

- Treat Obsidian as the local source of truth: Markdown notes, wikilinks, Properties/YAML, dashboards, decisions, tasks.
- Treat Hermes as the operator/analyst: research, triage, metadata normalization, linking suggestions, project reviews, weekly reviews.
- Add AI plugins only after the vault has enough clean structure; avoid starting with plugin sprawl.
- Base methodology: CODE (Capture, Organize, Distill, Express) + PARA (Projects, Areas, Resources, Archives), organized by actionability.

## Stage 1 implementation pattern

1. Resolve concrete vault path first; do not pass `$OBSIDIAN_VAULT_PATH` to file tools.
2. Inspect current notes and `.obsidian` config:
   - markdown files
   - enabled community/core plugins
   - existing templates/dashboards/properties
3. Create a timestamped backup before bulk edits.
4. Add a light folder skeleton without aggressively moving existing notes:
   - `00_Inbox/`
   - `01_Daily/`
   - `10_Dashboards/`
   - `30_Areas/`
   - `40_Resources/`
   - `50_People/`
   - `60_Templates/`
   - `70_System/`
   - `70_System/Hermes/`
   - `70_System/Bases/`
   - `90_Archive/`
5. For an active project, add subfolders only where useful:
   - `Meetings/`
   - `Decisions/`
   - `Specs/`
   - `Research/`
   - `Assets/`
6. Create templates for common note classes:
   - Project
   - Meeting
   - Decision
   - Spec
   - Research
   - Daily
   - Hermes Task
7. Add frontmatter to existing notes, preserving body content and special plugin fields such as `kanban-plugin: board`.
8. Create dashboards:
   - global `10_Dashboards/Home.md`
   - project-level dashboard, e.g. `Projects/<Project>/<Project> Dashboard.md`
9. If Bases is enabled, create `.base` files for vault/project overview and embed them in dashboards.
10. Update `.obsidian/types.json` for recurring properties if present.
11. Verify:
   - all notes have valid frontmatter
   - all notes have `type` and `status`
   - `.base` files parse as YAML
   - expected folders/templates/dashboards exist

## Minimal metadata schema

```yaml
---
type: project
project: "[[Project Name]]"
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - project
---
```

Common `type` values:

- `project`
- `meeting`
- `decision`
- `spec`
- `research`
- `source`
- `evergreen`
- `person`
- `daily`
- `dashboard`
- `prompt`
- `architecture`
- `plan`
- `task`
- `checklist`

Common `status` values:

- `active`
- `draft`
- `waiting`
- `done`
- `archived`
- `proposed`
- `accepted`
- `rejected`

## Pitfalls

- Do not move a user's existing project notes during Stage 1 unless explicitly asked; metadata + dashboards usually gives enough structure without breaking links.
- If a note already has frontmatter, merge/preserve important plugin fields rather than overwriting blindly.
- Kanban notes may rely on `kanban-plugin: board`; keep it inside the new YAML.
- Do not assume Templater has a configured template folder; creating `60_Templates/` is safe, but plugin settings may still need user-side configuration in Obsidian.
- For AI plugins, recommend Smart Connections/Copilot only after the vault has a stable metadata/linking baseline, unless the user specifically asks to install them immediately.
