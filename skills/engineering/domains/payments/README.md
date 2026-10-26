# Payments and API migrations

Two skills from [stripe/ai](https://github.com/stripe/ai/tree/57e355b6b00f54b7a667948b9648cc05bc353e06/skills), pinned on 26 October 2026. Skill instructions and supporting references are retained; host-specific metadata has been removed. Attribution: Stripe and upstream contributors. See the [MIT license](./LICENSE).

## Model-invoked skills

- [stripe-best-practices](./stripe-best-practices/SKILL.md) — Implement payment, billing, subscription, and webhook integrations.
- [upgrade-stripe](./upgrade-stripe/SKILL.md) — Upgrade Stripe API versions, webhook endpoints, and SDKs.

Use current Stripe documentation for version selection; bundled API dates are snapshots. Keep referenced documents with each skill. Applying these skills may require authenticated Stripe tooling and a target application; importing the files does not perform account changes or transactions. None of these manifests disables model invocation.

## Use and updates

Read the selected `SKILL.md` by path and keep its supporting folder intact. This is a portable skill collection; automatic discovery depends on the host's configured skill directories. Refresh discovery or start a new session after updating. No plugin commands, hooks, or native agent registrations are included. External tools and credentials may still require setup.

Update at an explicit revision, retain supporting files and license notices, and refresh the engineering skill count. Validation here covers packaging and file integrity; it does not execute the imported workflows.
