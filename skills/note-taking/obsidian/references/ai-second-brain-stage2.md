# AI Second Brain Stage 2 for Obsidian + Hermes

Use this reference after Stage 1 has created the vault skeleton, templates, dashboards, and baseline metadata.

## Goal

Add an operational layer so Hermes and Obsidian work as a reliable AI Second Brain: clear rules, permission boundaries, repeatable workflows, review cadences, and verification.

## Stage 2 implementation pattern

1. Confirm the concrete vault path; never pass `$OBSIDIAN_VAULT_PATH` to file tools.
2. Read the existing Stage 1 system notes and dashboards, especially:
   - `70_System/Hermes/README.md`
   - `70_System/System Index.md`
   - `10_Dashboards/Home.md`
   - active project dashboards such as `Projects/<Project>/<Project> Dashboard.md`
3. Create a timestamped backup before edits, e.g. under a sibling backup directory.
4. Create or update these Hermes system notes:
   - `70_System/Hermes/Hermes Operating Manual.md`
   - `70_System/Hermes/Hermes Permission Boundaries.md`
   - `70_System/Hermes/Vault Metadata Schema.md`
5. Create workflow notes in `70_System/Hermes/`:
   - `Inbox Triage Workflow.md`
   - `Research Workflow.md`
   - `Weekly Review Workflow.md`
   - `Project Review Workflow.md`
   - `Decision Capture Workflow.md`
6. Add review/decision index folders where useful:
   - `01_Daily/Weekly Reviews/README.md`
   - `Projects/<Project>/Reviews/README.md`
   - `40_Resources/Decisions/README.md`
7. Update dashboards and indexes with links to the new operational notes:
   - `70_System/Hermes/README.md`
   - `70_System/System Index.md`
   - `10_Dashboards/Home.md`
   - active project dashboards.
8. Add `aliases` to README index notes when dashboards link to them by display name, e.g. `[[Veilframe Reviews]]` should resolve to `Projects/Veilframe/Reviews/README.md` with `aliases: [Veilframe Reviews]`.
9. Verify before reporting completion:
   - expected Stage 2 files exist;
   - all Markdown notes parse as YAML/frontmatter;
   - all Markdown notes have `type` and `status`;
   - `.base` files parse as YAML;
   - wikilinks resolve, including aliases and `.base` embeds.

## Recommended Stage 2 note contents

### Hermes Operating Manual

Should define:

- Obsidian vault as source of truth;
- Hermes as operator/analyst;
- operating principles: preserve first, small structure, decisions as first-class notes, AI output must be auditable;
- working modes: read-only analysis, apply requested change, diff-first mode, research mode, review mode;
- folder destination defaults;
- standard Hermes checklist before/during/after edits;
- common user prompts mapped to workflows.

### Hermes Permission Boundaries

Should define:

- allowed actions when relevant to a user request;
- diff-first/summarize-before-apply cases;
- actions requiring explicit confirmation, especially deletion, archiving active project material, plugin changes, external sending/publishing, credential edits, and sensitive notes;
- external research boundaries;
- safety defaults.

### Vault Metadata Schema

Should define:

- required properties: `type`, `status`, `created`, `updated`, `tags`;
- common fields: `project`, `source_url`, `author`, `topic`, `participants`, `decision_date`, `review_date`;
- note types and status values;
- folder and naming conventions;
- Dataview audit snippets.

### Workflow notes

Create concise, executable process notes for:

- Inbox triage: raw capture → project/resource/area/person/waiting; extract tasks and decisions.
- Research: destination rules, source quality preference, note structure, final report format, quality gate.
- Weekly review: inputs, steps, review note structure, concise Telegram summary format.
- Project review: dashboard/readme/tasks/plans/specs/decisions/research scan, risks vs blockers, top next actions; optionally mention parallel subagent roles for complex reviews.
- Decision capture: context, options, decision, rationale, consequences, follow-up tasks, source notes.

## Verification approach

Use a deterministic script or equivalent checks that parse Markdown frontmatter with YAML, parse `.base` files as YAML, and resolve Obsidian wikilinks. The link resolver should handle:

- direct vault-root paths;
- paths without `.md` suffix;
- links relative to the current note;
- note stems;
- frontmatter aliases;
- non-Markdown embeds such as `.base` files.

Report counts rather than long dumps when clean:

- Markdown files checked;
- `.base` files checked;
- expected Stage 2 files present/missing;
- YAML/frontmatter errors;
- missing `type`/`status`;
- broken wikilinks;
- ambiguous wikilinks.

## Pitfalls

- Do not stop after creating workflow notes; update dashboards/indexes so the system is discoverable.
- Do not treat README index note titles as automatically resolving links; add aliases or link to the concrete path.
- Embedded `.base` files may need concrete paths in wikilinks, e.g. `![[70_System/Bases/Vault Overview.base#All notes]]`.
- Do not archive, delete, move, or rename existing user notes during Stage 2 unless explicitly asked.
- Keep the final report concise: what changed, backup path, verification counts, and recommended next stage.
