---
name: obsidian
description: Read, search, create, and edit notes in the Obsidian vault.
platforms: [linux, macos, windows]
---

# Obsidian Vault

Use this skill for filesystem-first Obsidian vault work: reading notes, listing notes, searching note files, creating notes, appending content, and adding wikilinks.

## Vault path

Use a known or resolved vault path before calling file tools.

The documented vault-path convention is the `OBSIDIAN_VAULT_PATH` environment variable, for example from `~/.hermes/.env`. If it is unset, use `~/Documents/Obsidian Vault`.

File tools do not expand shell variables. Do not pass paths containing `$OBSIDIAN_VAULT_PATH` to `read_file`, `write_file`, `patch`, or `search_files`; resolve the vault path first and pass a concrete absolute path. Vault paths may contain spaces, which is another reason to prefer file tools over shell commands.

If the vault path is unknown, `terminal` is acceptable for resolving `OBSIDIAN_VAULT_PATH` or checking whether the fallback path exists. Once the path is known, switch back to file tools.

## Read a note

Use `read_file` with the resolved absolute path to the note. Prefer this over `cat` because it provides line numbers and pagination.

## List notes

Use `search_files` with `target: "files"` and the resolved vault path. Prefer this over `find` or `ls`.

- To list all markdown notes, use `pattern: "*.md"` under the vault path.
- To list a subfolder, search under that subfolder's absolute path.

## Search

Use `search_files` for both filename and content searches. Prefer this over `grep`, `find`, or `ls`.

- For filenames, use `search_files` with `target: "files"` and a filename `pattern`.
- For note contents, use `search_files` with `target: "content"`, the content regex as `pattern`, and `file_glob: "*.md"` when you want to restrict matches to markdown notes.

## Create a note

Use `write_file` with the resolved absolute path and the full markdown content. Prefer this over shell heredocs or `echo` because it avoids shell quoting issues and returns structured results.

## Append to a note

Prefer a native file-tool workflow when it is not awkward:

- Read the target note with `read_file`.
- Use `patch` for an anchored append when there is stable context, such as adding a section after an existing heading or appending before a known trailing block.
- Use `write_file` when rewriting the whole note is clearer than constructing a fragile patch.

For an anchored append with `patch`, replace the anchor with the anchor plus the new content.

For a simple append with no stable context, `terminal` is acceptable if it is the clearest safe option.

## Targeted edits

Use `patch` for focused note changes when the current content gives you stable context. Prefer this over shell text rewriting.

## Wikilinks

Obsidian links notes with `[[Note Name]]` syntax. When creating notes, use these to link related content.

## AI Second Brain / vault organization

When the user asks to organize Obsidian as an AI-assisted second brain, prefer a staged, filesystem-first approach before recommending plugin-heavy workflows.

### Stage 1: structure and metadata baseline

- Inspect current notes and `.obsidian` plugin/config state first.
- Create a timestamped backup before bulk metadata or structure changes.
- Add a minimal PARA-inspired skeleton (`00_Inbox`, `01_Daily`, `10_Dashboards`, `30_Areas`, `40_Resources`, `50_People`, `60_Templates`, `70_System`, `90_Archive`) without moving existing project notes unless explicitly requested.
- Add reusable templates, dashboards, and consistent YAML properties (`type`, `project`, `status`, `created`, `updated`, `tags`).
- Preserve existing plugin frontmatter such as `kanban-plugin: board` when normalizing notes.
- If Bases is enabled, create `.base` overview files and embed them in dashboards.
- Verify all Markdown notes have valid frontmatter plus `type` and `status`, and validate `.base` files as YAML.

### Stage 2: operational layer

After Stage 1 is in place and the user says to proceed with the next stage, add Hermes operating notes and workflows rather than more folder taxonomy:

- Create/update `70_System/Hermes/Hermes Operating Manual.md`, `Hermes Permission Boundaries.md`, and `Vault Metadata Schema.md`.
- Create workflow notes for Inbox triage, research, weekly review, project review, and decision capture.
- Add review/decision index folders where useful, e.g. `01_Daily/Weekly Reviews/`, `Projects/<Project>/Reviews/`, and `40_Resources/Decisions/`.
- Update `70_System/Hermes/README.md`, `70_System/System Index.md`, the Home dashboard, and active project dashboards with links to the new operational notes.
- Add frontmatter `aliases` to README index notes when dashboards link by friendly names such as `[[Veilframe Reviews]]`.
- Verify YAML/frontmatter, required `type`/`status`, `.base` YAML, expected files, and wikilinks. The wikilink check should understand aliases and `.base` embeds.

### Stage 3: recurring review automation

After Stage 2 is in place and the user says to proceed with automation, create a light review loop rather than many noisy jobs:

- Inspect existing review templates, dashboards, and cron jobs first.
- Create a timestamped backup before edits.
- Add `60_Templates/Weekly Review.md`, `60_Templates/Project Review.md`, `10_Dashboards/Review Dashboard.md`, and `70_System/Hermes/Review Automation Schedule.md`.
- Update Home, System Index, Hermes README, workflow notes, and active project dashboards with links to the review system.
- Create recurring Hermes cron jobs only after checking for duplicates; typical initial jobs are weekly vault review and weekly project review.
- Use self-contained cron prompts with absolute vault paths, workflow note paths, destination note paths, guardrails, and verification requirements.
- Record cron job IDs, schedules, next runs, delivery target, write paths, and guardrails in `Review Automation Schedule.md`.
- Verify cron list, expected files, YAML/frontmatter, `.base` YAML, and wikilinks.

### Stage 4: capture and research queue automation

After Stage 3 is in place and the user asks for the next stage, add a conservative capture pipeline:

- Inspect current Inbox, templates, capture workflows, dashboards, and cron jobs first.
- Create a timestamped backup before edits.
- Add capture/source templates: `Inbox Item`, `Source`, `Evergreen`, and `Triage Report`.
- Add capture workflow notes: `Capture Pipeline Workflow`, `Inbox Automation Workflow`, `Research Capture Queue Workflow`, `Capture Routing Rules`, and `Capture Automation Schedule`.
- Add `10_Dashboards/Capture Dashboard.md` plus README/index notes for Inbox captures, triage reports, sources, cross-project research, and evergreen notes.
- Update Home, System Index, Hermes README, Inbox, Resources, Operating Manual, Inbox/Research workflows, and active project dashboards with capture links.
- Create recurring Hermes cron jobs only after checking for duplicates; typical initial jobs are Inbox Triage Digest and Research Capture Queue.
- Scheduled Stage 4 jobs should be conservative: create reports/source notes, keep raw Inbox captures intact, avoid private URLs, and never move/delete/archive/bulk-normalize notes.
- Record cron job IDs, schedules, next runs, delivery target, write paths, and guardrails in `Capture Automation Schedule.md`.
- Verify cron list, expected files, YAML/frontmatter, `.base` YAML, and wikilinks.

### Stage 5: no-plugin retrieval and context packs

After Stage 4 is in place and the user asks to proceed with retrieval, add a no-plugin retrieval layer rather than plugin-based semantic search:

- Inspect existing retrieval/search notes, dashboards, context packs, and cron jobs first.
- Create a timestamped backup before edits.
- Add retrieval system notes: `Vault Retrieval Protocol`, `Context Pack Workflow`, `Retrieval Quality Checklist`, and `Search Query Playbook`.
- Add templates: `Context Pack` and `Retrieval Report`.
- Add dashboards/indexes: `10_Dashboards/Retrieval Dashboard.md` and `40_Resources/Context Packs/README.md`.
- Add initial context packs, typically `70_System/Hermes/Context Pack - Vault.md` and `Projects/<Project>/Context Pack - <Project>.md` for the active project.
- Update Home, System Index, Hermes README, Resources, Operating Manual, active project dashboards, and metadata schema with retrieval links and `context-pack` / `retrieval-report` note types.
- Do not add Obsidian plugins by default. Use Markdown, YAML/frontmatter, wikilinks, dashboards, filesystem search, explicit context packs, and verification checklists.
- Do not create new cron jobs unless the user explicitly asks for scheduled context-pack refreshes.
- Verify expected files, YAML/frontmatter, `.base` YAML, wikilinks, and no-plugin markers.

### Scheduled project review notes

When running a scheduled/autonomous Obsidian project review, the full deliverable belongs in the dated review note, not in the chat/Telegram/local final response. Resolve the run date with a tool, read the configured workflow plus project dashboard/canonical note/task board/checklists/context pack/architecture/plans/specs/decisions/research/recent review notes, and inspect live repo state when source repos are named. The review note should include status color, current status, progress, open tasks, blockers, risks, decisions needed, recommended next actions, notes to clean up, files inspected, and verification. Keep cleanup as recommendations only: do not move, delete, archive, rename, bulk-normalize, or edit unrelated notes. Do not create/update/pause/resume/remove cron jobs from a scheduled review. Verify the destination note reads back and has frontmatter delimiters before the final report. Keep the final external report short: status color, destination note path, top three next actions/blockers combined, and decisions needed; do not paste the full review body.

See `references/scheduled-project-review.md` for the detailed recurring review pattern and verification checklist.

### Project task capture / Hermes task notes

When the user asks to "make a task for second brain", "запиши задачу в Obsidian", or capture future AI/Hermes work for a project, create a project-level task brief rather than a bare checkbox when context matters.

- Inspect the referenced project files and existing project task board/dashboard before writing.
- If the task depends on prior work or a previous conversation, use session recall/search when available before asking the user to repeat it.
- Create a standalone note under the project `Tasks/` area using the Hermes Task shape: goal, context, files/notes to inspect, required synthesis/steps, output path, constraints, required checks, and permission boundary.
- Add a wikilink to the standalone task note in the project's `Task board.md` or equivalent dashboard.
- Verify the note reads back, has valid frontmatter with `type`, `status`, `created`, `updated`, `tags`, and that the task-board link resolves by note title or alias.
- See `references/ai-second-brain-project-task-capture.md` for the detailed pattern and pitfalls.

### Project source-of-truth consolidation

When the user asks to make Obsidian the source of truth for a software/product project, especially one split across multiple repos, create a project-level knowledge area rather than a loose summary note:

- First inspect existing vault navigation, dashboards, context packs, and project folders so the update fits the current system.
- Treat the user's product/project boundary as authoritative. If two repos are parts of one product, create one canonical project note with aliases for repo/product names; do not split them into separate Obsidian projects unless asked.
- Create/update a compact but navigable set of notes: canonical project note, project dashboard, context pack, architecture index, component architecture notes, API/contracts, data models, operations/deployment, spec, roadmap, task board, launch checklist, and review/decision/research indexes as appropriate.
- Include source repo paths, important source docs, current inspection snapshot, product summary, architecture boundaries, critical flows, integrations, data/privacy boundaries, risks, and update protocol.
- Preserve no-plugin retrieval: use Markdown, YAML/frontmatter, aliases, wikilinks, dataview/tasks blocks if already used by the vault, and explicit context packs.
- For generated markdown written from Python, avoid large f-strings containing literal braces such as `{provider}` or JSON/schema examples. Use plain strings plus placeholder replacement, or escape braces as `{{...}}`, so note creation does not fail before writing.
- Verify after writing: count expected files, validate frontmatter delimiters and required keys, check no placeholders remain, and resolve wikilinks against note names, paths, and aliases.

See `references/project-source-of-truth-consolidation.md` for the Veilframe-style two-repo consolidation pattern and verification checklist.

### Stage 6: user-facing guide and adoption layer

After the vault has structure, workflows, automation, capture, and retrieval, add a concise user-facing guide so the human can operate the system without reverse-engineering the dashboards or Hermes notes:

- Create/update `70_System/Hermes/Second Brain User Guide.md`.
- Explain manual capture, filename conventions, minimal note/frontmatter patterns, links/sources, task capture, and when to ask Hermes instead of editing manually.
- Include example prompts/commands for triage, source capture, context packs, dashboard updates, and reviews.
- Link the guide from Home, System Index, Hermes README, Capture Dashboard, Retrieval Dashboard, and Hermes Operating Manual.
- Keep it practical and action-oriented; avoid turning it into an implementation changelog.
- Verify YAML/frontmatter, required metadata, `.base` YAML, wikilinks/aliases, and reachability from the main navigation surfaces.

See `references/ai-second-brain-stage1.md` for the detailed Hermes + Obsidian Stage 1 implementation pattern, metadata schema, and pitfalls.
See `references/ai-second-brain-stage2.md` for the Stage 2 operational layer: Hermes operating manual, permission boundaries, metadata schema, repeatable workflows, dashboard/index updates, alias/link cleanup, and verification checks.
See `references/ai-second-brain-stage3.md` for the Stage 3 recurring review automation pattern: templates, review dashboard, automation registry, cron jobs, prompts, guardrails, and verification checks.
See `references/ai-second-brain-stage4.md` for the Stage 4 capture/research automation pattern: capture templates, Inbox triage reports, source/research queues, capture dashboard, cron jobs, prompts, guardrails, and verification checks.
See `references/ai-second-brain-stage5.md` for the Stage 5 no-plugin retrieval pattern: retrieval protocol, context pack workflow, query playbook, quality checklist, context-pack templates, dashboards, and verification checks.
See `references/project-source-of-truth-consolidation.md` for the project source-of-truth consolidation pattern: multi-repo inspection, canonical project notes, context packs, architecture/operations notes, f-string brace pitfalls, and verification checks.
See `references/ai-second-brain-user-guide.md` for the Stage 6 user-facing guide/adoption pattern: daily-use instructions, manual capture protocol, Hermes prompt examples, dashboard links, and verification checks.
