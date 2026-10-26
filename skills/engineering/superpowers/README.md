# Portable Superpowers skills

Fourteen individually addressable skills copied from [obra/superpowers](https://github.com/obra/superpowers) at commit [`2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b), imported on 26 October 2026.

Each skill folder includes its upstream instructions and supporting files. The imported files are unmodified. [UPSTREAM.json](./UPSTREAM.json) records every upstream path, Git blob hash, and executable mode. Redistribution is covered by the included [MIT license](./LICENSE).

## Choose a skill

All fourteen upstream manifests are model-invoked: they have trigger descriptions and do not set `disable-model-invocation: true`. Explicit selection is useful when another installed collection offers a similar workflow.

| Skill | Use when |
| --- | --- |
| [brainstorming](./brainstorming/SKILL.md) | Clarifying a new idea or design before implementation. |
| [writing-plans](./writing-plans/SKILL.md) | Turning agreed requirements into implementation steps. |
| [executing-plans](./executing-plans/SKILL.md) | Implementing a plan in the current agent session. |
| [systematic-debugging](./systematic-debugging/SKILL.md) | Investigating a bug or unexpected behavior. |
| [verification-before-completion](./verification-before-completion/SKILL.md) | Gathering evidence before claiming success. |
| [test-driven-development](./test-driven-development/SKILL.md) | Implementing behavior through a red-green-refactor loop. |
| [requesting-code-review](./requesting-code-review/SKILL.md) | Preparing an independent review of changes. |
| [receiving-code-review](./receiving-code-review/SKILL.md) | Assessing and addressing review feedback. |
| [using-git-worktrees](./using-git-worktrees/SKILL.md) | Preparing an isolated development workspace. |
| [finishing-a-development-branch](./finishing-a-development-branch/SKILL.md) | Verifying and integrating completed work. |
| [subagent-driven-development](./subagent-driven-development/SKILL.md) | Delegating planned implementation with review. |
| [dispatching-parallel-agents](./dispatching-parallel-agents/SKILL.md) | Assigning independent investigations to separate agents. |
| [writing-skills](./writing-skills/SKILL.md) | Creating and evaluating reusable skill instructions. |
| [diagnosing-superpowers](./diagnosing-superpowers/SKILL.md) | Investigating failures in a Superpowers session. |

## Use in this repository

Ask the agent to read a specific file, for example:

```text
Use skills/engineering/superpowers/systematic-debugging/SKILL.md
to investigate this failure. Follow its supporting references as needed.
```

This works through normal file access and does not require a Superpowers plugin. The engineering routing index also points here. These are source copies in this repository's collection; placing them here does not automatically register them in every agent's native skill catalog.

For automatic discovery, install or expose the desired folders through the target agent's documented skill location. Hosts already configured to scan this repository's nested `skills/` tree can rediscover them on their next refresh/session. Other hosts need an explicit copy, symlink, or external-directory configuration. No machine-level installation or agent configuration is changed by this import.

## Portability and dependencies

Skills are separately selectable, but the workflows are not all independent. Keep full folders, including `scripts/`, `references/`, templates, and helper prompts. Keep the sibling layout when following cross-skill references.

| Selected workflow | Supporting skills or resources |
| --- | --- |
| `brainstorming` | Continues into `writing-plans`; its optional visual companion needs Node.js and a local browser/server. |
| `writing-plans` | Refers to `executing-plans`, `subagent-driven-development`, and `using-git-worktrees`. |
| `executing-plans` | Uses sibling subagent-development scripts, TDD, debugging, verification, review, worktree, and branch-finishing guidance. |
| `subagent-driven-development` | Uses review templates and worktree/branch-finishing guidance; requires a real subagent facility. |
| `systematic-debugging` | Refers to `test-driven-development` and `verification-before-completion`. |
| `writing-skills` | Builds on `test-driven-development`; references shared runtime mappings. |
| Review and parallel-agent skills | Independent-review/parallel steps require host subagent support. |
| `diagnosing-superpowers` | Requires access to the relevant session transcript and evidence. |

For a portable subset, include the selected skills plus the transitive dependencies they reference. Copying this whole `superpowers/` directory preserves the included dependency layout; the agent can still read only the selected skill.

Upstream references such as `superpowers:systematic-debugging` identify a sibling skill. Without plugin namespacing, resolve that reference to this collection's `systematic-debugging/SKILL.md`. If another installed plugin has the same skill name, use the explicit repository path to select this pinned copy.

Shared runtime mappings are included under [using-superpowers/references](./using-superpowers/references/). This is a support-only directory: it has no `SKILL.md`. The upstream startup/bootstrap skill, plugin manifests, and session hooks are not installed. Automatic full-plugin workflow activation therefore differs from this portable selection.

Tool mappings are snapshots. Use the host's actual tool schemas, permissions, and user instructions when they differ from upstream guidance. Portability of the instruction files does not guarantee that every host provides subagents, transcript access, Git operations, Node.js, or other required execution tools. The optional visual companion retains upstream behavior; review [its guidance](./brainstorming/visual-companion.md) and scripts before use.

## Updating

Fetch the desired upstream revision into a temporary directory, compare it with `UPSTREAM.json`, and replace only these imported paths after reviewing the changes. Refresh the license, shared references, hashes, and file modes together. Keep this local README and routing entries. The current import is pinned and does not auto-update.

Validation of this import checks file integrity, layout, manifest fields, referenced files, and executable permissions. It is not a cross-host behavioral test of the workflows.
