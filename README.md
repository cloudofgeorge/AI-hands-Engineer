# AI Hands

AI Hands is a personal collection of agent skills and reusable engineering rules.
It is meant to be read by coding agents, copied into agent environments, and used
as a shared operating manual for recurring product, engineering, and workflow
tasks.

The repository is intentionally lightweight: the Markdown files are the product.
There is no application runtime, build step, or package manager setup for the
root repository.

## Repository Layout

```text
.
├── README.md
├── rules/
│   ├── main.md
│   ├── context7.md
│   ├── folders.md
│   ├── git.md
│   └── web/
└── skills/
    ├── README.md
    ├── design/
    ├── engineering/
    ├── forthright/
    ├── marketing/
    ├── note-taking/
    ├── personal/
    ├── productivity/
    ├── seo/
    └── tools/
```

## Skills

Most skills live under `skills/<section>/<skill-name>/SKILL.md`. Nested skill
sets can live deeper; for example, UltraSkills uses
`skills/engineering/UltraSkills/skills/<skill-name>/SKILL.md`, while Superpowers
uses `skills/engineering/superpowers/<skill-name>/SKILL.md`. A skill can also
include nearby reference documents, templates, assets, or scripts when the
workflow needs more than one file.

Start with [`skills/README.md`](skills/README.md), then open the relevant section
README:

| Section | Use when | Index |
| --- | --- | --- |
| Design | Design critique, high-fidelity prototypes, interactive demos, slides, animations, image generation, brand systems, or frontend taste workflows. | [`skills/design/README.md`](skills/design/README.md) |
| Engineering | Research, code review, wayfinding, code planning, architecture, debugging, implementation, TDD, security, CI, deployment, macOS, web, UltraSkills staged research/review workflows, or Superpowers process workflows. | [`skills/engineering/README.md`](skills/engineering/README.md) |
| Forthright | Agent-to-agent handoffs and compact internal operational writing. | [`skills/forthright/README.md`](skills/forthright/README.md) |
| Marketing | Growth, positioning, acquisition, conversion, lifecycle, revenue, and launch work. | [`skills/marketing/README.md`](skills/marketing/README.md) |
| Note-taking | Second Brain retrieval, capture, handoffs, reviews, and Obsidian vault note work. | [`skills/note-taking/README.md`](skills/note-taking/README.md) |
| Personal | User-specific writing, Obsidian, and recipe/cookbook workflows. | [`skills/personal/README.md`](skills/personal/README.md) |
| Productivity | General workflow control: handoffs, teaching, grilling, and writing better skills. | [`skills/productivity/README.md`](skills/productivity/README.md) |
| SEO | SEO/GEO research, technical audits, content, schema, authority, monitoring, and reporting. | [`skills/seo/README.md`](skills/seo/README.md) |
| Tools | Direct operation of documents, PDFs, Obsidian CLI, and Playwright/browser automation. | [`skills/tools/README.md`](skills/tools/README.md) |

### Skill routing convention

Each section README separates:

- **User-invoked** skills — reachable only when explicitly called
  (`disable-model-invocation: true`).
- **Model-invoked** skills — model- or user-reachable, with trigger-oriented
  descriptions so agents can select them automatically.
- **Imported or nested skill sets** — collections such as UltraSkills or
  Superpowers; use their linked paths plus the section README when a skill name
  overlaps with another installed skill.

### Hermes installation note

For Hermes Agent, install or point `skills.external_dirs` at this repository's
`skills/` directory. Hermes users should reload/start a new session after the
repo update so nested `SKILL.md` files, including UltraSkills and Superpowers,
are discoverable.
If a nested skill has the same `name` as another installed skill, use the linked
README path to choose the intended version.

## Rules

Rules are reusable implementation guidance for agents. They are broader than
skills: a skill defines a workflow, while a rule defines standing project
preferences or architecture patterns.

| File | Purpose |
| --- | --- |
| [`rules/main.md`](rules/main.md) | Entry point that lists the rule set agents should load. |
| [`rules/context7.md`](rules/context7.md) | Requires Context7 for current library, framework, SDK, API, CLI, and cloud-service documentation. |
| [`rules/folders.md`](rules/folders.md) | Keeps new project code in subfolders instead of the repository root. |
| [`rules/git.md`](rules/git.md) | Defines default Git and GitHub workflow expectations. |
| [`rules/credits-and-limits.md`](rules/credits-and-limits.md) | Architecture guidance for credits, limits, account balances, and spend reservations. |

Web-specific rules live in [`rules/web/`](rules/web/):

| File | Purpose |
| --- | --- |
| [`rules/web/analytics.md`](rules/web/analytics.md) | Consent-aware analytics setup with Plausible, Google Tag Manager, and Yandex.Metrika. |
| [`rules/web/api.md`](rules/web/api.md) | API implementation guidance. |
| [`rules/web/async-jobs-and-workers.md`](rules/web/async-jobs-and-workers.md) | Background job, worker, retry, idempotency, and observability patterns. |
| [`rules/web/auth.md`](rules/web/auth.md) | Google OAuth authentication architecture and security requirements. |
| [`rules/web/frontend.md`](rules/web/frontend.md) | Frontend stack and design expectations. |
| [`rules/web/lemonsqueezy.md`](rules/web/lemonsqueezy.md) | Lemon Squeezy checkout, webhook, entitlement, and local data model guidance. |
| [`rules/web/testing.md`](rules/web/testing.md) | Full-stack testing strategy with Vitest and Playwright expectations. |

## Using This Repository

Use the repository as a source of truth for agent behavior:

1. Start at [`skills/README.md`](skills/README.md) when choosing a skill section.
2. Open the chosen section README to choose between related skills.
3. Point the agent at the relevant `SKILL.md` once a match is clear.
4. Load `rules/main.md` when starting a project that should follow these defaults.
5. Copy or symlink selected skills and rules into the agent environment if your
   tool expects skills in a specific local directory.
6. Keep section README files updated whenever you add, rename, move, or remove a
   skill.

## Adding A Skill

Use the [`writing-great-skills`](skills/productivity/writing-great-skills/SKILL.md)
workflow. At minimum, every skill should include:

- A `SKILL.md` file.
- Frontmatter with `name` and `description`.
- A description that says exactly when the agent should use the skill.
- Concise instructions in the main file.
- Supporting references, templates, assets, or scripts only when they keep the
  main skill easier to read.

Recommended structure:

```text
skills/<section>/<skill-name>/
├── SKILL.md
├── references/
├── templates/
└── scripts/
```

## Maintenance Notes

- Keep instructions concrete and current.
- Prefer short skill files with links to focused references.
- Keep section README files as routing indexes, not full manuals.
- Avoid time-sensitive claims unless the skill also tells the agent how to verify
  them.
- Do not commit or push changes unless the user explicitly asks for it.
- When a rule depends on current third-party documentation, use Context7 instead
  of relying on memory.
