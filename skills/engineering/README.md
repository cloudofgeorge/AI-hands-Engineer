# Engineering

Code-work skills for research, planning, debugging, architecture, delivery, platform domains, and engineering review.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- Start with the narrowest domain skill that matches the request: security, infrastructure, macOS, CI, deployment, web, or mobile work before broad engineering skills.
- Use `diagnosing-bugs` for root-cause work; use `tdd` once the target behavior is understood and ready to implement.
- Use `wizard` only when a human must complete manual dashboard, credential, provisioning, migration, or cutover steps; do not use it for work the agent can perform directly.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- [grill-with-docs](./grill-with-docs/SKILL.md) — Challenge a plan or design while creating ADR and glossary documentation as decisions crystallise.
- [retro](./retro/SKILL.md) — Review a coding session and suggest improvements to the agent environment, navigation, checks, and guidance.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Planning and architecture

- [find-ideas](./find-ideas/SKILL.md) — Find new feature ideas, audit shipped features, or generate a prioritized product backlog for an existing project.
- [domain-modeling](./domain-modeling/SKILL.md) — Clarify codebase terminology in `GLOSSARY.md` (or glossaries reached through `GLOSSARY-MAP.md`) and record architectural decisions in ADRs.
- [codebase-design](./codebase-design/SKILL.md) — Shared vocabulary for designing deep modules.
- [research](./research/SKILL.md) — Delegate high-trust primary-source investigation and capture cited findings as Markdown in the repo.

### Debugging, testing, and code flow

- [diagnosing-bugs](./diagnosing-bugs/SKILL.md) — Diagnosis loop for hard bugs and performance regressions.
- [tdd](./tdd/SKILL.md) — Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests.
- [prototype](./prototype/SKILL.md) — Build a throwaway prototype to answer a design question before committing to a product or implementation direction.

### Human-in-the-loop operations

- [wizard](./wizard/SKILL.md) — Generate an interactive Bash guide for manual credential, dashboard, provisioning, migration, or cutover steps that only a human can perform.

### Security

- [security-best-practices](./security/security-best-practices/SKILL.md) — Perform language and framework specific security best-practice reviews and suggest improvements.
- [security-threat-model](./security/security-threat-model/SKILL.md) — Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations.
- [security-ownership-map](./security/security-ownership-map/SKILL.md) — Analyze git repositories to build a security ownership topology, bus factor, and sensitive-code ownership map.

### GitHub, CI, build, and deploy tools

- [pr](./pr/SKILL.md) — Write a PR body with a visual summary, before/after evidence, and merge risk.
- [ci-cd](./tools/ci-cd/SKILL.md) — Use when investigating or changing GitHub Actions or GitLab CI workflows, deployment gates, runners, artifacts, secrets, triggers, or rollbacks.
- [github-ticket-intake](./tools/github-ticket-intake/SKILL.md) — Draft or create GitHub issues from messy request text.
- [gh-fix-ci](./tools/gh-fix-ci/SKILL.md) — Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions.
- [turborepo](./tools/turborepo/SKILL.md) — Turborepo monorepo build system guidance.
- [vercel-deploy](./tools/vercel-deploy/SKILL.md) — Deploy applications and websites to Vercel using the bundled `scripts/deploy.sh` claimable-preview flow.

### macOS domain skills

- [macos-development](./domains/macos/macos-development/SKILL.md) — Comprehensive macOS development guidance including Swift 6+, SwiftUI, SwiftData, architecture patterns, AppKit bridging, and macOS 26 Tahoe APIs.
- [macos-design-guidelines](./domains/macos/macos-design-guidelines/SKILL.md) — Apple Human Interface Guidelines for Mac.
- [macos-app-design](./domains/macos/macos-app-design/SKILL.md) — Use when designing or building native macOS applications with SwiftUI or AppKit.
- [macos-accessibility](./domains/macos/macos-accessibility/SKILL.md) — Expert in macOS Accessibility APIs (AXUIElement) for desktop automation.
- [app-planner](./domains/macos/macos-development/app-planner/skill.md) — Plans new macOS apps or analyzes existing projects.
- [appkit-swiftui-bridge](./domains/macos/macos-development/appkit-swiftui-bridge/skill.md) — Expert guidance for hybrid AppKit-SwiftUI development.
- [architecture-patterns](./domains/macos/macos-development/architecture-patterns/skill.md) — Deep dive into software architecture for macOS.
- [coding-best-practices](./domains/macos/macos-development/coding-best-practices/skill.md) — Reviews macOS Swift 6+ code for modern idioms, SOLID principles, SwiftData patterns, and concurrency best practices.
- [macos-capabilities](./domains/macos/macos-development/macos-capabilities/skill.md) — Expert guidance on macOS platform capabilities.
- [macos-tahoe-apis](./domains/macos/macos-development/macos-tahoe-apis/skill.md) — Guide to macOS 26 Tahoe APIs and features.
- [swiftdata-architecture](./domains/macos/macos-development/swiftdata-architecture/skill.md) — Deep dive into SwiftData design patterns and best practices.
- [ui-review-tahoe](./domains/macos/macos-development/ui-review-tahoe/skill.md) — Comprehensive UI/UX review for macOS Tahoe apps.

### Infrastructure domain skills

- [troubleshooting-kubernetes](./domains/infrastructure/troubleshooting-kubernetes/SKILL.md) — Use when investigating Kubernetes incidents, failing workloads, Service connectivity, NetworkPolicies, permissions, or rollout health.
- [terraform](./domains/infrastructure/terraform/SKILL.md) — Use when reviewing Terraform plans, state locks, workspaces, backends, drift, imports, or infrastructure-change proposals.
- [observability](./domains/infrastructure/observability/SKILL.md) — Use when investigating metrics, logs, traces, alerts, dashboards, SLI/SLO behavior, alert noise, or monitoring changes.
- [gitops](./domains/infrastructure/gitops/SKILL.md) — Use when investigating or changing Argo CD or Flux reconciliation, desired-state drift, sync status, GitOps rollbacks, or Git-managed Kubernetes delivery.
- [aws-finops](./domains/infrastructure/aws-finops/SKILL.md) — Use when investigating AWS cost or usage, Cost Explorer, CUR, Budgets, allocation, spend anomalies, Savings Plans, Reserved Instances, or optimization proposals.

### Web and mobile domain skills

- [develop-web-game](./domains/web/develop-web-game/SKILL.md) — Use when Codex is building or iterating on a web game and needs a reliable development and testing loop.
- [vercel-react-best-practices](./domains/web/vercel-react-best-practices/SKILL.md) — Use when writing, reviewing, refactoring, or optimizing React/Next.js code for Vercel-style performance patterns.
- [vercel-react-native-skills](./domains/web/vercel-react-native-skills/SKILL.md) — Use when building React Native or Expo apps, optimizing mobile performance, implementing animations, or working with native modules.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
