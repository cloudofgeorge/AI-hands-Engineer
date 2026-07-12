# gstack

Software-factory workflows for planning, design, review, browser and iOS QA,
shipping, deployment, security, documentation, performance, and multi-agent
coordination.

This README is a routing index for agents. Keep it short; detailed procedures
belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Start with [gstack](./gstack/SKILL.md) only when you are unsure which gstack
  skill fits — it routes to the right one.
- Planning skills run before implementation; live-audit skills run against a
  running site or device.
- iOS skills (`ios-*`) target a real iPhone and share the same on-device
  StateServer; use them together.
- `qa` finds and fixes bugs; `qa-only` only reports.
- `freeze`/`unfreeze` scope edits; `careful` warns on destructive commands;
  `guard` combines both.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- None in this section.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route
to them automatically.

### Router and meta

- [gstack](./gstack/SKILL.md) — Use when you invoke gstack without a specific skill or ask which gstack skill fits; routes planning, review, QA, shipping, debugging, docs, security, and design to the right skill.
- [upgrade](./gstack-upgrade/SKILL.md) — Use when asked to upgrade, update, or get the latest version of gstack.

### Spec, ideation, and plan review

- [spec](./gstack-spec/SKILL.md) — Use to turn vague intent into a precise spec, file an issue, or make a backlog item.
- [office-hours](./gstack-office-hours/SKILL.md) — Use to brainstorm an idea, decide whether something is worth building, or run YC-style office hours before any plan.
- [plan-ceo-review](./gstack-plan-ceo-review/SKILL.md) — Use to rethink ambition, expand or reduce scope, and find the 10-star product framing for a plan.
- [plan-eng-review](./gstack-plan-eng-review/SKILL.md) — Use to lock in architecture, data flow, edge cases, and test coverage before coding starts.
- [plan-design-review](./gstack-plan-design-review/SKILL.md) — Use to review a design plan (in plan mode, before implementation) and rate each dimension.
- [plan-devex-review](./gstack-plan-devex-review/SKILL.md) — Use to review developer experience for APIs, CLIs, SDKs, docs, and onboarding.
- [autoplan](./gstack-autoplan/SKILL.md) — Use to run the CEO, design, eng, and DX reviews sequentially with auto-decisions and a final approval gate.
- [plan-tune](./gstack-plan-tune/SKILL.md) — Use to tune which AskUserQuestion prompts fire and inspect the developer profile.

### Design

- [design-consultation](./gstack-design-consultation/SKILL.md) — Use to propose a full design system and create `DESIGN.md` for a new project.
- [design-shotgun](./gstack-design-shotgun/SKILL.md) — Use to generate multiple design variants, compare them, and iterate before committing.
- [design-html](./gstack-design-html/SKILL.md) — Use to turn an approved mockup or plan into production-quality HTML/CSS.
- [design-review](./gstack-design-review/SKILL.md) — Use to audit and iteratively fix visual issues on a live site.

### Web QA, browser, and automation

- [browse](./gstack-browse/SKILL.md) — Use to test a feature, verify a deployment, dogfood a flow, take screenshots, or test forms and uploads in a headless browser.
- [qa](./gstack-qa/SKILL.md) — Use to QA test a web app and iteratively fix the bugs found.
- [qa-only](./gstack-qa-only/SKILL.md) — Use to produce a bug report with screenshots and repro steps without changing code.
- [scrape](./gstack-scrape/SKILL.md) — Use to pull read-only data from a web page as JSON.
- [skillify](./gstack-skillify/SKILL.md) — Use to codify a recent scrape flow into a permanent, fast browser-skill.
- [setup-browser-cookies](./gstack-setup-browser-cookies/SKILL.md) — Use to import cookies from your real browser before QA-testing authenticated pages.
- [open-gstack-browser](./gstack-open-gstack-browser/SKILL.md) — Use to launch the visible AI-controlled GStack Browser with the sidebar extension.
- [pair-agent](./gstack-pair-agent/SKILL.md) — Use to pair a remote AI agent with your browser over HTTP.

### iOS QA and instrumentation

- [ios-qa](./gstack-ios-qa/SKILL.md) — Use to run live-device vision-driven QA on a SwiftUI iPhone app.
- [ios-fix](./gstack-ios-fix/SKILL.md) — Use to autonomously fix a bug found by `ios-qa` and verify the fix on the device.
- [ios-design-review](./gstack-ios-design-review/SKILL.md) — Use to visually audit an iOS app on real hardware against Apple HIG and `DESIGN.md`.
- [ios-clean](./gstack-ios-clean/SKILL.md) — Use to remove the DebugBridge SPM package and its `#if DEBUG` wiring.
- [ios-sync](./gstack-ios-sync/SKILL.md) — Use to regenerate the iOS debug bridge against the latest gstack templates.

### Code review, debugging, and health

- [review](./gstack-review/SKILL.md) — Use for pre-landing PR review: SQL safety, LLM trust boundaries, and structural diff issues.
- [investigate](./gstack-investigate/SKILL.md) — Use for systematic debugging with root-cause analysis before any fix.
- [health](./gstack-health/SKILL.md) — Use to run type checker, linter, tests, and dead-code detection and get a composite code-quality score.
- [devex-review](./gstack-devex-review/SKILL.md) — Use to live-test developer experience: docs, getting-started, TTHW, and CLI help.

### Shipping, deployment, and release

- [ship](./gstack-ship/SKILL.md) — Use to run tests, bump VERSION, update CHANGELOG, commit, push, and create a PR.
- [land-and-deploy](./gstack-land-and-deploy/SKILL.md) — Use to merge the PR, wait for CI and deploy, and verify production health.
- [setup-deploy](./gstack-setup-deploy/SKILL.md) — Use to detect and configure the deploy platform, URL, health checks, and status commands for `land-and-deploy`.
- [landing-report](./gstack-landing-report/SKILL.md) — Use to see which VERSION slots and sibling workspaces have WIP work about to ship.
- [canary](./gstack-canary/SKILL.md) — Use for post-deploy canary monitoring of console errors, performance, and page failures.
- [retro](./gstack-retro/SKILL.md) — Use for a weekly engineering retrospective of commit history and code quality.

### Safety and edit scope

- [careful](./gstack-careful/SKILL.md) — Use to get warnings before `rm -rf`, `DROP TABLE`, force-push, and other destructive commands.
- [freeze](./gstack-freeze/SKILL.md) — Use to restrict edits to a specific directory for the session.
- [unfreeze](./gstack-unfreeze/SKILL.md) — Use to clear the freeze boundary and allow edits everywhere again.
- [guard](./gstack-guard/SKILL.md) — Use for maximum safety: combines `careful` warnings with `freeze` scoping.

### Documentation and artifacts

- [document-release](./gstack-document-release/SKILL.md) — Use to sync docs to what shipped, update README/ARCHITECTURE/CHANGELOG, and surface doc debt.
- [document-generate](./gstack-document-generate/SKILL.md) — Use to generate missing documentation for a feature or project using the Diataxis framework.
- [make-pdf](./gstack-make-pdf/SKILL.md) — Use to turn any Markdown file into a publication-quality PDF with margins, TOC, and page numbers.
- [diagram](./gstack-diagram/SKILL.md) — Use to turn an English description or Mermaid source into an editable diagram triplet.

### Performance, security, and second opinions

- [benchmark](./gstack-benchmark/SKILL.md) — Use for web performance regression detection: page load, Core Web Vitals, bundle size.
- [benchmark-models](./gstack-benchmark-models/SKILL.md) — Use to run the same prompt across Claude, GPT, and Gemini and compare latency, tokens, cost, and quality.
- [cso](./gstack-cso/SKILL.md) — Use for infrastructure-first security audits, threat modeling, OWASP, and supply-chain scanning.
- [claude](./gstack-claude/SKILL.md) — Use to get a Claude Code second opinion: independent review, adversarial challenge, or read-only consult.

### Context, learning, and gbrain

- [context-save](./gstack-context-save/SKILL.md) — Use to save git state, decisions, and remaining work for a future session.
- [context-restore](./gstack-context-restore/SKILL.md) — Use to restore a saved context and pick up where you left off.
- [learn](./gstack-learn/SKILL.md) — Use to review, search, prune, and export project learnings across sessions.
- [setup-gbrain](./gstack-setup-gbrain/SKILL.md) — Use to install and configure gbrain (CLI, PGLite/Supabase, MCP, trust policy) for an agent.
- [sync-gbrain](./gstack-sync-gbrain/SKILL.md) — Use to re-index this repo into gbrain and refresh agent search guidance in `AGENTS.md`.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
