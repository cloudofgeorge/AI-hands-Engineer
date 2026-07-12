# AI Second Brain user guide pattern

Use this reference when an Obsidian vault already has the AI second brain structure, dashboards, operating notes, review automation, capture workflows, and retrieval/context-pack layer, and the missing piece is a user-facing instruction note.

## Goal

Create one concise, practical note that tells the human how to work with the system manually and how to ask Hermes/agents to operate it. This is different from internal operating manuals: it should be written for daily use, not for implementation detail.

## Recommended note

Path: `70_System/Hermes/Second Brain User Guide.md`

Suggested frontmatter:

```yaml
type: guide
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - second-brain
  - hermes
  - workflow
```

## Sections to include

- Purpose: what the second brain is for.
- Manual capture: where to add raw notes, usually `00_Inbox/Captures/`.
- Capture filename convention: timestamp plus short title, e.g. `YYYY-MM-DD HHmm - Topic.md`.
- Minimal note template: frontmatter plus source/context/next-action blocks.
- Links and sources: how to paste URLs, quotes, files, and related wikilinks.
- Tasks: how to record tasks without hiding them in prose.
- Asking Hermes: short command examples such as triage this capture, create a source note, build a context pack, summarize related notes, update a dashboard.
- Manual vs agent mode: when to write directly and when to delegate to the assistant.
- Review loops: where weekly/project/retrieval/capture reports appear and how to use them.
- What not to do: do not over-file, do not create excessive folders, do not install plugins by default, do not rely on unlinked prose for decisions/tasks.

## Link placement

After creating the guide, link it from the main navigation surfaces:

- `10_Dashboards/Home.md`
- `70_System/System Index.md`
- `70_System/Hermes/README.md`
- `10_Dashboards/Capture Dashboard.md`
- `10_Dashboards/Retrieval Dashboard.md`
- `70_System/Hermes/Hermes Operating Manual.md`

Use a stable wikilink such as `[[Second Brain User Guide]]` and add aliases only if the target filename or dashboard label requires it.

## Verification

Before finishing, verify:

- all Markdown frontmatter parses;
- all Markdown notes have required `type` and `status` if the vault enforces them;
- `.base` files parse as YAML;
- wikilinks resolve, including aliases and `.base` embeds;
- the guide is reachable from the home/dashboard/system surfaces.

## Pitfalls

- Do not bury user-facing instructions only inside `Hermes Operating Manual`; that note is for agent/operator detail and becomes too dense for daily use.
- Do not add new Obsidian plugins to solve instruction/discovery problems; prefer dashboards, README notes, and explicit wikilinks.
- Do not make the guide a retrospective narrative of what was implemented. Make it an actionable protocol the user can follow tomorrow.
