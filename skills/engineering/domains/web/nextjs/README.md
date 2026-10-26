# Next.js workflows

Six official skills from [vercel/next.js](https://github.com/vercel/next.js/tree/23a1f0cb692fd55b665efde5fa3c0c88364ade16/skills), pinned from `canary` on 26 October 2026. Skill instructions and supporting references are retained; host-specific metadata has been removed. Attribution: Vercel and Next.js contributors. See the [MIT license](./license.md).

## Model-invoked skills

- [next-dev-loop](./next-dev-loop/SKILL.md) — Verify changes against a running development server and browser.
- [next-bundle-optimizer](./next-bundle-optimizer/SKILL.md) — Reduce browser startup work and bundle costs.
- [next-cache-components-adoption](./next-cache-components-adoption/SKILL.md) — Adopt Cache Components with runtime verification.
- [next-cache-components-optimizer](./next-cache-components-optimizer/SKILL.md) — Improve cached shells and rendering behavior.
- [next-partial-prefetching-adoption](./next-partial-prefetching-adoption/SKILL.md) — Introduce partial prefetching.
- [next-partial-prefetching-optimizer](./next-partial-prefetching-optimizer/SKILL.md) — Optimize navigation prefetch work.

## Compatibility

These are version-sensitive workflows from the framework's canary branch. Check the selected skill's requirements against the target project before using it. At this pin, `next-dev-loop` requires Next.js 16.3+ with Turbopack, a running `next dev` server exposing `/_next/mcp`, and `agent-browser` 0.31.1+. Importing these documents does not upgrade projects or install browser tooling. None of the six manifests disables model invocation.

## Use and updates

Read the selected `SKILL.md` by path and keep its supporting folder intact. This is a portable skill collection; automatic discovery depends on the host's configured skill directories. Refresh discovery or start a new session after updating. No plugin commands, hooks, or native agent registrations are included. External tools and credentials may still require setup.

Update at an explicit revision, retain supporting files and license notices, and refresh the engineering skill count. Validation here covers packaging and file integrity; it does not execute the imported workflows.
