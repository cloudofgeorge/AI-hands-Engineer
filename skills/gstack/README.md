# gstack

A software-factory skill pack for planning, reviewing, testing, browser QA, shipping, and multi-agent workflows.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

For the long-form upstream gstack overview, install notes, and troubleshooting guide, see [UPSTREAM_README.md](./UPSTREAM_README.md).

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- For a new idea, start with `office-hours` or `spec`; for a fully reviewed plan, use `autoplan`.
- For live code, choose `review`, `investigate`, `qa`, or `ship` based on the current stage.
- For browser work, prefer `browse` or `open-gstack-browser`; for remote-agent coordination, use `pair-agent`.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- None in this section.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Planning and product review

- [office-hours](./office-hours/SKILL.md) — YC Office Hours — two modes.
- [spec](./spec/SKILL.md) — Turn vague intent into a precise, executable spec in five phases.
- [autoplan](./autoplan/SKILL.md) — Auto-review pipeline — reads the full CEO, design, eng, and DX review skills from disk and runs them sequentially with auto-decisions using 6 decision principles.
- [plan-ceo-review](./plan-ceo-review/SKILL.md) — CEO/founder-mode plan review.
- [plan-eng-review](./plan-eng-review/SKILL.md) — Eng manager-mode plan review.
- [plan-design-review](./plan-design-review/SKILL.md) — Designer's eye plan review — interactive, like CEO and Eng review.
- [plan-devex-review](./plan-devex-review/SKILL.md) — Interactive developer experience plan review.
- [plan-tune](./plan-tune/SKILL.md) — Self-tuning question sensitivity + developer psychographic for gstack (v1: observational).

### Build, review, safety, and release

- [review](./review/SKILL.md) — Pre-landing PR review.
- [investigate](./investigate/SKILL.md) — Systematic debugging with root cause investigation.
- [codex](./codex/SKILL.md) — OpenAI Codex CLI wrapper — three modes.
- [cso](./cso/SKILL.md) — Chief Security Officer mode.
- [careful](./careful/SKILL.md) — Safety guardrails for destructive commands.
- [freeze](./freeze/SKILL.md) — Restrict file edits to a specific directory for the session.
- [guard](./guard/SKILL.md) — Full safety mode: destructive command warnings + directory-scoped edits.
- [unfreeze](./unfreeze/SKILL.md) — Clear the freeze boundary set by /freeze, allowing edits to all directories again.
- [ship](./ship/SKILL.md) — Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR.
- [landing-report](./landing-report/SKILL.md) — Read-only queue dashboard for workspace-aware ship.
- [land-and-deploy](./land-and-deploy/SKILL.md) — Land and deploy workflow.
- [canary](./canary/SKILL.md) — Post-deploy canary monitoring.
- [benchmark](./benchmark/SKILL.md) — Performance regression detection using the browse daemon.
- [benchmark-models](./benchmark-models/SKILL.md) — Cross-model benchmark for gstack skills.
- [health](./health/SKILL.md) — Code quality dashboard.

### Design, browser QA, and scraping

- [browse](./browse/SKILL.md) — Fast headless browser for QA testing and site dogfooding.
- [open-gstack-browser](./open-gstack-browser/SKILL.md) — Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in.
- [setup-browser-cookies](./setup-browser-cookies/SKILL.md) — Import cookies from your real Chromium browser into the headless browse session.
- [pair-agent](./pair-agent/SKILL.md) — Pair a remote AI agent with your browser.
- [qa](./qa/SKILL.md) — Systematically QA test a web application and fix bugs found.
- [qa-only](./qa-only/SKILL.md) — Report-only QA testing.
- [scrape](./scrape/SKILL.md) — Pull data from a web page.
- [skillify](./skillify/SKILL.md) — Codify the most recent successful /scrape flow into a permanent browser-skill on disk.
- [design-consultation](./design-consultation/SKILL.md) — Design consultation: understands your product, researches the landscape, proposes a complete design system (aesthetic, typography, color, layout, spacing, motion).
- [design-shotgun](./design-shotgun/SKILL.md) — Design shotgun: generate multiple AI design variants, open a comparison board, collect structured feedback, and iterate.
- [design-html](./design-html/SKILL.md) — Design finalization: generates production-quality Pretext-native HTML/CSS.
- [design-review](./design-review/SKILL.md) — Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems, AI slop patterns, and slow interactions — then fixes them.
- [devex-review](./devex-review/SKILL.md) — Live developer experience audit.
- [hackernews-frontpage](./browser-skills/hackernews-frontpage/SKILL.md) — Scrape the Hacker News front page (titles, points, comment counts).

### Documentation, memory, and setup

- [gstack](./SKILL.md) — Top-level gstack browser/QA entry point for fast headless browsing and site dogfooding.
- [document-release](./document-release/SKILL.md) — Post-ship documentation update.
- [document-generate](./document-generate/SKILL.md) — Generate missing documentation from scratch for a feature, module, or entire project.
- [make-pdf](./make-pdf/SKILL.md) — Turn any markdown file into a publication-quality PDF.
- [context-save](./context-save/SKILL.md) — Save working context.
- [context-restore](./context-restore/SKILL.md) — Restore working context saved earlier by /context-save.
- [learn](./learn/SKILL.md) — Manage project learnings.
- [retro](./retro/SKILL.md) — Weekly engineering retrospective.
- [setup-deploy](./setup-deploy/SKILL.md) — Configure deployment settings for /land-and-deploy.
- [setup-gbrain](./setup-gbrain/SKILL.md) — Set up gbrain for this coding agent: install the CLI, initialize a local PGLite or Supabase brain, register MCP, capture per-remote trust policy.
- [sync-gbrain](./sync-gbrain/SKILL.md) — Keep gbrain current with this repo's code and refresh agent search guidance in CLAUDE.md.
- [gstack-upgrade](./gstack-upgrade/SKILL.md) — Upgrade gstack to the latest version.

### iOS QA

- [ios-qa](./ios-qa/SKILL.md) — Live-device iOS QA for SwiftUI apps.
- [ios-fix](./ios-fix/SKILL.md) — Autonomous iOS bug fixer.
- [ios-design-review](./ios-design-review/SKILL.md) — Visual design audit for iOS apps on real hardware.
- [ios-clean](./ios-clean/SKILL.md) — Remove the DebugBridge SPM package and #if DEBUG wiring from an iOS app.
- [ios-sync](./ios-sync/SKILL.md) — Regenerate the iOS debug bridge against the latest upstream gstack templates.

### OpenClaw native skills

- [gstack-openclaw-office-hours](./openclaw/skills/gstack-openclaw-office-hours/SKILL.md) — Use when asked to brainstorm, evaluate whether an idea is worth building, run office hours, or think through a new product idea or design direction before any code is written.
- [gstack-openclaw-ceo-review](./openclaw/skills/gstack-openclaw-ceo-review/SKILL.md) — Use when asked to review a plan, challenge a proposal, run a CEO review, poke holes in an approach, think bigger about scope, or decide whether to expand or reduce the plan.
- [gstack-openclaw-investigate](./openclaw/skills/gstack-openclaw-investigate/SKILL.md) — Use when asked to debug, fix a bug, investigate an error, or do root cause analysis, and when users report errors, stack traces, unexpected behavior, or say something stopped working.
- [gstack-openclaw-retro](./openclaw/skills/gstack-openclaw-retro/SKILL.md) — Weekly engineering retrospective. Analyzes commit history, work patterns, and code quality metrics with persistent history and trend tracking.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
