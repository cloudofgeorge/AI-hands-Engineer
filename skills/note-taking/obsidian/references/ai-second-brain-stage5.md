# AI Second Brain Stage 5 for Obsidian + Hermes

Use this reference after Stage 1 structure/metadata, Stage 2 operational workflows, Stage 3 review automation, and Stage 4 capture/research automation are in place.

## Goal

Add a no-plugin retrieval layer: a protocol for how Hermes finds vault context, prepares focused context packs, and answers from notes without requiring extra Obsidian plugins.

## Design principle

Do not add Obsidian plugins by default. Use:

- Markdown notes;
- YAML/frontmatter;
- wikilinks;
- dashboards/indexes;
- filesystem search;
- explicit context packs;
- verification checklists.

## Stage 5 implementation pattern

1. Inspect existing retrieval/search notes, dashboards, context packs, and cron jobs first.
2. Create a timestamped vault backup before edits.
3. Add retrieval system notes:
   - `70_System/Hermes/Vault Retrieval Protocol.md`
   - `70_System/Hermes/Context Pack Workflow.md`
   - `70_System/Hermes/Retrieval Quality Checklist.md`
   - `70_System/Hermes/Search Query Playbook.md`
4. Add templates:
   - `60_Templates/Context Pack.md`
   - `60_Templates/Retrieval Report.md`
5. Add dashboards/indexes:
   - `10_Dashboards/Retrieval Dashboard.md`
   - `40_Resources/Context Packs/README.md`
6. Add initial context packs:
   - global: `70_System/Hermes/Context Pack - Vault.md`
   - active project: `Projects/<Project>/Context Pack - <Project>.md`
7. Update Home, System Index, Hermes README, Resources, Operating Manual, active project dashboards, and metadata schema with retrieval links and `context-pack` / `retrieval-report` note types.
8. Do not create new cron jobs unless the user explicitly asks for scheduled context-pack refreshes.
9. Verify expected files, YAML/frontmatter, `.base` YAML, wikilinks, and no-plugin markers.

## Retrieval protocol contents

The main protocol should define:

- filesystem-first retrieval order;
- narrow/project/topic/vault-wide scope levels;
- dashboard-first lookup;
- filename search and content search patterns;
- link expansion rules;
- context pack creation/update criteria;
- quality rules for missing/conflicting/stale context;
- explicit statement that no additional Obsidian plugins are required.

## Context pack rules

A context pack is a compact retrieval aid, not a source of truth.

Required sections:

- Scope
- When to use this pack
- Read first
- Current understanding
- Active work / tasks
- Decisions and constraints
- Open questions
- Search terms
- Verification checklist
- Stale or conflicting notes

## Pitfalls

- Do not treat a context pack as authoritative if source notes disagree.
- Do not copy large note bodies; link to source notes.
- Do not include secrets, credentials, API keys, or connection strings.
- Do not create a plugin dependency if markdown/search/context packs are sufficient.
- Do not run scheduled context-pack refreshes unless the user asks; retrieval should usually happen on demand.
- If `[[Home Dashboard]]` is linked but the file is `Home.md`, add an alias rather than creating a duplicate note.
