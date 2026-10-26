# Authentication engineering

Three skills from [better-auth/skills](https://github.com/better-auth/skills/tree/20c9e88a5c007461a703f1c213572b073196113e), pinned on 26 October 2026. The original skill content and directory layout are preserved. Attribution: Better Auth and upstream contributors. No standalone license file is present in this upstream revision; no license is inferred from other Better Auth repositories.

## Model-invoked skills

- [better-auth-best-practices](./better-auth/best-practices/SKILL.md) — Integrate Better Auth and configure its adapters, sessions, and plugins.
- [create-auth](./better-auth/create-auth/SKILL.md) — Scaffold authentication for an application.
- [better-auth-security-best-practices](./security/SKILL.md) — Harden secrets, origins, cookies, sessions, and rate limits.

Verify guidance against the installed Better Auth version and current upstream documentation when applying it. These imports do not install an authentication runtime or configure credentials. None of these manifests disables model invocation.

## Use and updates

Read the selected `SKILL.md` by path and keep its supporting folder intact. This is a portable skill collection; automatic discovery depends on the host's configured skill directories. Refresh discovery or start a new session after updating. No plugin commands, hooks, or native agent registrations are included. External tools and credentials may still require setup.

Update at an explicit revision, retain supporting files and license notices, and refresh the engineering skill count. Validation here covers packaging and file integrity; it does not execute the imported workflows.
