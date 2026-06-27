# Engineering

Code-work skills for planning, debugging, architecture, delivery, platform domains, and engineering review.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- Start with the narrowest domain skill that matches the request: security, macOS, CI, deployment, or web-game work before broad engineering skills.
- Use `diagnose`/`diagnosing-bugs` for root-cause work; use `tdd` once the target behavior is understood and ready to implement.
- Use `to-prd` → `to-issues` → `implement` for explicit planning-to-execution flows.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- [implement](./implement/SKILL.md) — Implement a piece of work based on a PRD or set of issues.
- [improve-codebase-architecture](./improve-codebase-architecture/SKILL.md) — Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- [prototype](./prototype/SKILL.md) — Build a throwaway prototype to flesh out a design — a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route.
- [to-issues](./to-issues/SKILL.md) — Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices.
- [to-prd](./to-prd/SKILL.md) — Turn the current conversation into a PRD and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed.
- [triage](./triage/SKILL.md) — Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Planning and architecture

- [find-ideas](./find-ideas/SKILL.md) — Use when the user wants to find what to work on next in an existing project, audit progress, brainstorm a backlog, surface bugs and tech debt, or generate a prioritized list of ideas.
- [grill-with-docs](./grill-with-docs/SKILL.md) — Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise.
- [domain-modeling](./domain-modeling/SKILL.md) — Build and sharpen a project's domain model.
- [codebase-design](./codebase-design/SKILL.md) — Shared vocabulary for designing deep modules.

### Debugging, testing, and code flow

- [diagnose](./diagnose/SKILL.md) — Disciplined diagnosis loop for hard bugs and performance regressions.
- [diagnosing-bugs](./diagnosing-bugs/SKILL.md) — Diagnosis loop for hard bugs and performance regressions.
- [tdd](./tdd/SKILL.md) — Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests.
- [resolving-merge-conflicts](./resolving-merge-conflicts/SKILL.md) — Use when you need to resolve an in-progress git merge/rebase conflict.

### Optimization and simplification

- [ponytail](./optimization/ponytail/ponytail/SKILL.md) — Forces the laziest solution that actually works, simplest, shortest, most minimal.
- [ponytail-review](./optimization/ponytail/ponytail-review/SKILL.md) — Code review focused exclusively on over-engineering.
- [ponytail-audit](./optimization/ponytail/ponytail-audit/SKILL.md) — Whole-repo audit for over-engineering; ranks what to delete, simplify, or replace with stdlib/native equivalents.
- [ponytail-debt](./optimization/ponytail/ponytail-debt/SKILL.md) — Harvest `ponytail:` comments into a debt ledger for deliberate shortcuts and deferred cleanup.
- [ponytail-help](./optimization/ponytail/ponytail-help/SKILL.md) — Quick-reference card for all ponytail modes, skills, and commands.

### Security

- [security-best-practices](./security/security-best-practices/SKILL.md) — Perform language and framework specific security best-practice reviews and suggest improvements.
- [security-threat-model](./security/security-threat-model/SKILL.md) — Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model.
- [security-ownership-map](./security/security-ownership-map/SKILL.md) — Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership.

### GitHub, CI, build, and deploy tools

- [github-ticket-intake](./tools/github-ticket-intake/SKILL.md) — Draft or create GitHub issues from messy request text.
- [gh-fix-ci](./tools/gh-fix-ci/SKILL.md) — Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions.
- [turborepo](./tools/turborepo/SKILL.md) — Turborepo monorepo build system guidance.
- [vercel-deploy](./tools/vercel-deploy/SKILL.md) — Deploy applications and websites to Vercel using the bundled `scripts/deploy.sh` claimable-preview flow.

### macOS domain skills

- [macos-development](./domains/macos/macos-development/SKILL.md) — Comprehensive macOS development guidance including Swift 6+, SwiftUI, SwiftData, architecture patterns, AppKit bridging, and macOS 26 Tahoe APIs.
- [macos-design-guidelines](./domains/macos/macos-design-guidelines/SKILL.md) — Apple Human Interface Guidelines for Mac.
- [macos-app-design](./domains/macos/macos-app-design/SKILL.md) — Use when designing or building native macOS applications with SwiftUI or AppKit.
- [macos-accessibility](./domains/macos/macos-accessibility/SKILL.md) — Expert in macOS Accessibility APIs (AXUIElement) for desktop automation.
- [app-planner](./domains/macos/macos-development/app-planner/SKILL.md) — Plans new macOS apps or analyzes existing projects.
- [appkit-swiftui-bridge](./domains/macos/macos-development/appkit-swiftui-bridge/SKILL.md) — Expert guidance for hybrid AppKit-SwiftUI development.
- [architecture-patterns](./domains/macos/macos-development/architecture-patterns/SKILL.md) — Deep dive into software architecture for macOS.
- [coding-best-practices](./domains/macos/macos-development/coding-best-practices/SKILL.md) — Reviews macOS Swift 6+ code for modern idioms, SOLID principles, SwiftData patterns, and concurrency best practices.
- [macos-capabilities](./domains/macos/macos-development/macos-capabilities/SKILL.md) — Expert guidance on macOS platform capabilities.
- [macos-tahoe-apis](./domains/macos/macos-development/macos-tahoe-apis/SKILL.md) — Guide to macOS 26 Tahoe APIs and features.
- [swiftdata-architecture](./domains/macos/macos-development/swiftdata-architecture/SKILL.md) — Deep dive into SwiftData design patterns and best practices.
- [ui-review-tahoe](./domains/macos/macos-development/ui-review-tahoe/SKILL.md) — Comprehensive UI/UX review for macOS Tahoe apps.

### Web domain skills

- [develop-web-game](./domains/web/develop-web-game/SKILL.md) — Use when Codex is building or iterating on a web game (HTML/JS) and needs a reliable development + testing loop: implement small changes.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
