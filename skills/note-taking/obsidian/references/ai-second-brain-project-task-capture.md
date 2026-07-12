# AI Second Brain project task capture pattern

Use this when the user asks to "make a task for second brain" or capture a future Hermes/AI task inside the Obsidian vault, especially for an active software/product project.

## Trigger examples

- "Сделай задачу для second brain"
- "Запиши задачу в Obsidian"
- "Создай Hermes task для проекта"
- "Нужно потом сделать X на базе файла/работы Y"

## Workflow

1. Load the Obsidian skill and resolve the vault/project path from known memory or `OBSIDIAN_VAULT_PATH` if needed.
2. Inspect the referenced project files and existing project notes/task board before writing. For Veilframe-style projects, check the canonical project folder and `Tasks/Task board.md`.
3. If the user references "all prior work" or "we did this before", use session search when available before asking them to repeat context.
4. Create a standalone task note, not just a one-line task, when the future work needs context, constraints, source files, output requirements, checks, and permissions.
5. Use the existing `Hermes Task` template shape where appropriate:
   - Goal
   - Context
   - Files / notes to inspect
   - Required synthesis or steps
   - Output format/path
   - Constraints
   - Required checks
   - Permission boundary
6. Add the task to the project task board/dashboard with a wikilink to the standalone task note.
7. Verify the created note reads back correctly, frontmatter has `type`, `status`, `created`, `updated`, `tags`, and the task board link resolves by note title/alias.

## Frontmatter pattern

```yaml
---
aliases:
  - Human Friendly Task Alias
type: prompt
project: "[[Project Name]]"
status: todo
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - hermes
  - prompt
  - task
---
```

Use `type: prompt` for a reusable Hermes task brief unless the vault has a more specific task type.

## Pitfalls

- Do not create a generic note in Resources when the task is clearly project-specific; put it under the project `Tasks/` area and link it from the task board.
- Do not blindly copy an old script or runbook into the task; call out whether it is authoritative, deprecated, or only useful as a phase list.
- Do not run production deploys, connect to live infrastructure, or read real secrets when the user only asked to create a planning/task note.
- Avoid stale implementation logs. Capture source paths, acceptance checks, and permission boundaries instead.
