# Design

Design, visual prototyping, image generation, brand systems, frontend taste, and UI critique skills.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- Use `impeccable` for broad UI direction, critique, polish, and design quality audits.
- Use `design-taste-frontend` as the default frontend taste workflow for public pages and app screens, with separate directions and checks for each.
- Use the legacy taste and style skills only when explicitly called by name; `design-taste-frontend-v2-experimental` preserves the previous single-file workflow.
- Use `huashu-design` for HTML prototypes, demos, slides, animations, and visualizations, starting with three design directions; production apps with backends are outside its scope.
- Use `imagegen-frontend-*` for screen or website-reference images, or `brandkit` for brand boards that create a new identity or build on supplied brand assets.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- [design-taste-frontend-v1](./design-taste-frontend-v1/SKILL.md) — Use only when a project depends on the original v1 frontend taste behavior for backward compatibility.
- [design-taste-frontend-v2-experimental](./design-taste-frontend-v2-experimental/SKILL.md) — Use when explicitly requested for the previous single-file, dial-driven frontend taste workflow.
- [high-end-visual-design](./high-end-visual-design/SKILL.md) — Use when explicitly requested for a calm, polished style with soft contrast, generous whitespace, and spring motion.
- [gpt-taste](./gpt-taste/SKILL.md) — Use for elite UX/UI pages with strong AIDA structure, editorial typography, GSAP motion, bento layouts, and large section spacing.
- [stitch-design-taste](./stitch-design-taste/SKILL.md) — Use to generate Google Stitch-friendly `DESIGN.md` files for premium semantic design systems.
- [minimalist-ui](./minimalist-ui/SKILL.md) — Use for clean editorial interfaces with warm monochrome palettes, typographic contrast, flat bento grids, and muted pastels.
- [industrial-brutalist-ui](./industrial-brutalist-ui/SKILL.md) — Use for raw mechanical, Swiss-print, military-terminal interfaces such as data dashboards, portfolios, or editorial sites.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Core UI design and critique

- [impeccable](./impeccable/SKILL.md) — Use for frontend interface design, redesign, critique, polish, motion, color, UX quality audits, and design-system refinement.
- [huashu-design](./huashu-design/SKILL.md) — Use for HTML prototypes, demos, slides, animations, visualizations, three-direction design exploration, and expert review.
- [redesign-existing-projects](./redesign-existing-projects/SKILL.md) — Use when upgrading an existing website or app to premium visual quality without breaking current functionality.

### Frontend taste and implementation direction

- [design-taste-frontend](./design-taste-frontend/SKILL.md) — Use the default frontend workflow with researched direction draws, separate page and app-screen rules, source linting, and browser screenshot review.
- [image-to-code](./image-to-code/SKILL.md) — Use when a visually important web implementation should first generate and analyze design images, then code the site to match.

### Image, brand, and visual-system generation

- [imagegen-frontend-web](./imagegen-frontend-web/SKILL.md) — Use to generate separate premium website design-reference images for each landing-page or marketing-site section.
- [imagegen-frontend-mobile](./imagegen-frontend-mobile/SKILL.md) — Use to generate premium mobile app screen concepts and flows for iOS, Android, or cross-platform products.
- [brandkit](./brandkit/SKILL.md) — Use for brand-guidelines boards, logo systems, identity decks, and mockups, preserving supplied brand assets unless a refresh is requested.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
