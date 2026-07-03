---
name: find-ideas
description: Use when the user wants to find new feature ideas for an existing project, audit shipped features, brainstorm a feature backlog, or generate a prioritized list of product ideas. Triggers on "/find-ideas", "what should I build next", "find me feature ideas", "what feature should I build next", "what's missing".
---

# Find Ideas

## Overview

Survey an existing project, then produce a prioritized feature-ideas doc in the repo: an inventory of what's already done, followed by new feature ideas.

The completed-features inventory comes first because it grounds every later judgment — you can't tell what's missing without seeing what's there.

## When to Use

- User asks for feature ideas, a feature backlog, a feature roadmap, or "what feature to build next"
- User wants to audit shipped features to spot product gaps
- Slash command `/find-ideas` invoked

**Don't use for:**
- Brand-new projects with no code — use brainstorming instead
- Single-file scripts — overkill
- When user already has a specific task in mind

## Workflow

### 1. Research

Read in this order. Stop when you have enough signal — don't exhaustively read everything.

- `README.md`, `AGENTS.md` if present
- `package.json` / `pyproject.toml` / `Cargo.toml` / equivalent — names, scripts, dependencies
- Top-level directory listing (one level deep)
- `docs/` tree — list files, read specs/ADRs/design docs that look load-bearing
- Sample 3-8 key source files: route definitions, main entry points, schema/model files, recent feature directories

If the project is a monorepo, do this per app/package that looks relevant.

### 2. Synthesize

Build the two lists in order:

1. **Completed features** — what's shipped. Group by area (auth, billing, UI, etc.). One bullet per feature.
2. **New feature ideas** — gaps, natural extensions, things the docs hint at but haven't been built

Assign every new feature idea a priority:

- **P0** — missing core workflow blocking the product promise
- **P1** — important, ship next
- **P2** — nice-to-have
- **P3** — someday / speculative

If you can't justify a priority in one short clause, the item is too vague — sharpen it or drop it.

### 3. Write the doc

Path: `docs/ideas/YYYY-MM-DD-ideas.md` (use today's date, create the folder if missing).

Use this structure exactly:

```markdown
# Project Ideas — YYYY-MM-DD

## Priority Legend

- **P0** — missing core workflow blocking the product promise
- **P1** — important, ship next
- **P2** — nice-to-have
- **P3** — someday / speculative

## Completed Features

### <Area>
- Feature — one-line description

## New Feature Ideas

- **[P1] Title** — what it is. _Why: rationale._
- **[P2] Title** — what it is. _Why: rationale._
```

Sort new feature ideas by priority (P0 → P3), then alphabetically inside a tier.

### 4. Wrap up

Print the doc path and a 3-bullet summary of the strongest P0/P1 feature ideas, if any. Then ask:

> "Want me to refine any section, add detail, or convert top items into GitHub issues?"

### 5. Offer to split into task files

After delivering the ideas doc, ask the user if they want the new feature ideas split into an actionable task file under `docs/tasks/` (create the folder if missing):

> "Want me to split these into a task file under `docs/tasks/`? I'd create `new_features_ideas.md` as a numbered checklist."

If the user agrees, write:

- **New Feature Ideas** → `new_features_ideas.md`

Do **not** create a task file for "Completed Features" — that's reference, not actionable.

**File format** — each task file must be:

- An H1 matching the source section title
- A numbered list (`1.`, `2.`, …) of all items from that section, preserving priority order
- Each item prefixed with an empty checkbox: `- [ ]`
- Item body copied verbatim from the ideas doc (title, priority tag, description, _Why:_)

Example:

```markdown
# New Feature Ideas

1. - [ ] **[P1] Title** — what it is. _Why: rationale._
2. - [ ] **[P2] Title** — what it is. _Why: rationale._
```

After writing the files, print the list of paths created.

## Quick Reference

| Step | Output |
|------|--------|
| Research | Mental model of project state |
| Synthesize | Completed features + prioritized new feature ideas |
| Write | `docs/ideas/YYYY-MM-DD-ideas.md` |
| Wrap | Path + 3-bullet summary + offer to refine |
| Split (on request) | `docs/tasks/new_features_ideas.md` as a numbered checklist |

## Common Mistakes

- **Skipping the completed-features inventory** — without it, "new ideas" overlap with what's already shipped. Always do it first.
- **Listing every possible idea** — the value is prioritization. If everything is P1, nothing is. Aim for ~5-15 feature ideas, not 50.
- **Vague priorities** — "P1: add analytics" is useless. Say which workflow it improves and why it matters.
- **Inventing ideas without a product gap** — only list ideas grounded in shipped behavior, docs, or clear user workflows.
- **Exhaustively reading the codebase** — research until you have enough signal, then synthesize. The doc is the deliverable, not a complete audit.

## Converting to Issues

If the user wants to push items to GitHub after reviewing the doc, hand off to the `to-issues` or `triage` skill rather than creating issues directly here.
