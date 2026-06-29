# Design

Design, visual prototyping, image generation, brand systems, frontend taste, and UI critique skills.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- Use `impeccable` for broad UI direction, critique, polish, and design quality audits.
- Use `design-taste-frontend` as the default premium frontend taste workflow; use `design-taste-frontend-v1` only for backward compatibility.
- Use `huashu-design` when the deliverable should be a high-fidelity HTML prototype, interactive demo, slide, animation, or design exploration.
- Use `imagegen`, `imagegen-frontend-*`, or `brandkit` when the task is actual image, screen, website-reference, or brand-board generation.
- Layer style-specific skills such as `minimalist-ui` or `industrial-brutalist-ui` only when the brief calls for that aesthetic.
- Use `full-output-enforcement` only when the task requires exhaustive, unabridged code or artifact output.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- None in this section.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Core UI design and critique

- [impeccable](./impeccable/SKILL.md) — Use for frontend interface design, redesign, critique, polish, motion, color, UX quality audits, and design-system refinement.
- [huashu-design](./huashu-design/SKILL.md) — Use for high-fidelity HTML prototypes, interaction demos, slides, animations, design variants, and expert design review.
- [redesign-existing-projects](./redesign-existing-projects/SKILL.md) — Use when upgrading an existing website or app to premium visual quality without breaking current functionality.

### Frontend taste and implementation direction

- [design-taste-frontend](./design-taste-frontend/SKILL.md) — Use as the default anti-generic frontend workflow for landing pages, portfolios, product pages, and redesigns.
- [design-taste-frontend-v1](./design-taste-frontend-v1/SKILL.md) — Use only when a project depends on the original v1 frontend taste behavior for backward compatibility.
- [high-end-visual-design](./high-end-visual-design/SKILL.md) — Use when a website needs agency-grade typography, spacing, shadows, cards, animations, and premium visual standards.
- [gpt-taste](./gpt-taste/SKILL.md) — Use for elite UX/UI pages with strong AIDA structure, editorial typography, GSAP motion, bento layouts, and large section spacing.
- [image-to-code](./image-to-code/SKILL.md) — Use when a visually important web implementation should first generate and analyze design images, then code the site to match.
- [full-output-enforcement](./full-output-enforcement/SKILL.md) — Use when a generation task must produce complete unabridged code or artifacts with no placeholders.

### Image, brand, and visual-system generation

- [imagegen](./imagegen/SKILL.md) — Use for OpenAI Image API generation, editing, inpainting, background changes, product shots, concept art, covers, and batch variants.
- [imagegen-frontend-web](./imagegen-frontend-web/SKILL.md) — Use to generate separate premium website design-reference images for each landing-page or marketing-site section.
- [imagegen-frontend-mobile](./imagegen-frontend-mobile/SKILL.md) — Use to generate premium mobile app screen concepts and flows for iOS, Android, or cross-platform products.
- [brandkit](./brandkit/SKILL.md) — Use for high-end brand-guidelines boards, logo systems, identity decks, mockups, and visual-world presentations.
- [stitch-design-taste](./stitch-design-taste/SKILL.md) — Use to generate Google Stitch-friendly `DESIGN.md` files for premium semantic design systems.

### Style-specific UI aesthetics

- [minimalist-ui](./minimalist-ui/SKILL.md) — Use for clean editorial interfaces with warm monochrome palettes, typographic contrast, flat bento grids, and muted pastels.
- [industrial-brutalist-ui](./industrial-brutalist-ui/SKILL.md) — Use for raw mechanical, Swiss-print, military-terminal interfaces such as data dashboards, portfolios, or editorial sites.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
