# Skills

Routing index for the skill sections in this repository.

Start here when an agent needs to choose which section README to open. Each section README then routes between user-invoked, model-invoked, and imported nested skill bundles.

## Routing principles

- Prefer the narrowest section and skill that directly matches the task.
- Open the section README first; open individual `SKILL.md` files only after a likely match is found.
- Treat `User-invoked` skills as explicit commands; do not auto-select them unless the user asked for that named flow.
- Imported bundles can be nested deeper than `skills/<section>/<skill-name>`; open their bundle README when the section points to one.
- Keep section READMEs short and trigger-oriented so future agents can scan them quickly.

## Sections

| Section | Skills | Use when |
| --- | ---: | --- |
| [Design](./design/README.md) | 16 | Design, visual prototyping, image generation, brand systems, frontend taste, and UI critique. |
| [Engineering](./engineering/README.md) | 85 | Research, code review, wayfinding, planning, debugging, architecture, implementation, security, platform, CI, deploy, human-guided manual operations, web/mobile performance, and UltraSkills and Superpowers process workflows. |
| [Forthright](./forthright/README.md) | 1 | High-compression internal communication mode for agent-to-agent work. |
| [Marketing](./marketing/README.md) | 45 | Growth, positioning, acquisition, conversion, lifecycle, and revenue workflows. |
| [Note-taking](./note-taking/README.md) | 2 | Second Brain retrieval, capture, handoffs, reviews, and Obsidian vault note work. |
| [Personal](./personal/README.md) | 3 | User-specific writing, notes, and cookbook workflows. |
| [Productivity](./productivity/README.md) | 5 | General workflow, handoff, teaching, grilling, and skill-writing discipline. |
| [SEO](./seo/README.md) | 20 | SEO/GEO research, technical audits, content, authority, monitoring, and reporting. |
| [Tools](./tools/README.md) | 4 | Concrete tool-operation workflows for documents, PDFs, Obsidian, and browser automation. |

## Maintenance

- Add a row here whenever a top-level skill section is added, removed, or renamed.
- Keep the skill counts in this table aligned with real `SKILL.md` files; ignore test fixtures.
- Update the relevant section README in the same change as any skill move or rename.
