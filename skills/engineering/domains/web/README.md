# Web and mobile engineering

## Model-invoked skills

- [develop-web-game](./develop-web-game/SKILL.md) — Build and verify browser games.
- [vercel-react-best-practices](./vercel-react-best-practices/SKILL.md) — Review React and Next.js performance; existing project copy retained.
- [vercel-react-native-skills](./vercel-react-native-skills/SKILL.md) — Build React Native and Expo applications; existing project copy retained.
- [vercel-composition-patterns](./composition-patterns/SKILL.md) — Design reusable component APIs and composition patterns.
- [web-design-guidelines](./web-design-guidelines/SKILL.md) — Review interface behavior and accessibility against current guidelines.
- [react-view-transitions](./react-view-transitions/SKILL.md) — Implement React view transitions.
- [vercel-optimize](./vercel-optimize/SKILL.md) — Investigate deployed cost and performance using production metrics.
- [writing-guidelines](./writing-guidelines/SKILL.md) — Review documentation against Vercel's writing guidelines.

## Nested groups

- [Next.js workflows](./nextjs/README.md) — Six skills for runtime verification, bundles, caching, and prefetching.

## Source and portability

The five newly added Vercel skills come from [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278), pinned on 26 October 2026. The two pre-existing Vercel skills are reused without replacement. Vercel and upstream contributors retain attribution. License declarations inside the imported files are preserved; this upstream revision has no standalone license file, so no repository-wide license is inferred here.

`vercel-optimize` requires Node.js 20+, Vercel CLI v53+, an authenticated linked project, and Observability Plus for route-level recommendations. The web and writing guideline skills fetch their current rule documents during use, so they are not fully offline. View-transition and React 19 patterns require compatible application versions. None of the five new manifests disables model invocation.

## Use and updates

Read the selected `SKILL.md` by path and keep its supporting folder intact. This is a portable skill collection; automatic discovery depends on the host's configured skill directories. Refresh discovery or start a new session after updating. No plugin commands, hooks, or native agent registrations are included. External tools and credentials may still require setup.

Update at an explicit revision, retain supporting files and license notices, and refresh the engineering skill count. Validation here covers packaging and file integrity; it does not execute the imported workflows.
