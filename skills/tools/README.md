# Tools

Concrete tool-operation skills for documents, PDFs, Obsidian CLI, and browser automation.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- Use these when the user asks to operate a specific external artifact or tool rather than choose a broader domain workflow.
- Prefer `playwright-cli` for browser automation and visual QA; prefer `doc`/`pdf` when layout fidelity matters.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- None in this section.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Tool operators

- [doc](./doc/SKILL.md) — Use for reading, creating, or editing `.docx` documents where formatting or layout fidelity matters.
- [pdf](./pdf/SKILL.md) — Use for reading, creating, or reviewing PDF files where rendering and layout fidelity matter.
- [obsidian-cli](./obsidian-cli/SKILL.md) — Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, tasks, properties, and more.
- [playwright-cli](./playwright-cli/SKILL.md) — Use for browser automation, form filling, screenshots, visual QA, and web data extraction.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
