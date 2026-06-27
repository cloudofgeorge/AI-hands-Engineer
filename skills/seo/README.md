# SEO

SEO and GEO skills for keyword research, technical audits, content, authority, structured data, monitoring, and reporting.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- Use research skills first when the target keywords, competitors, or search intent are unknown.
- Use audit skills when the user brings an existing site, page, or traffic/ranking problem.
- Use monitoring/reporting skills after fixes or when the user asks for ongoing visibility.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- None in this section.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Research and strategy

- [keyword-research](./keyword-research/SKILL.md) — Use when the user asks to "find keywords"; prioritizes volume, difficulty, intent, and clusters from provided or connected data.
- [competitor-analysis](./competitor-analysis/SKILL.md) — Use when the user asks to "compare competitors" or find SEO/GEO gaps.
- [serp-analysis](./serp-analysis/SKILL.md) — Use when the user asks to "analyze SERPs"; reviews ranking factors, features, intent, AI Overviews, and snippets.
- [content-gap-analysis](./content-gap-analysis/SKILL.md) — Use when the user asks to "find content gaps".

### Technical and on-page SEO

- [technical-seo-checker](./technical-seo-checker/SKILL.md) — Use when the user asks to "check technical SEO".
- [on-page-seo-auditor](./on-page-seo-auditor/SKILL.md) — Use when the user asks to "audit on-page SEO".
- [meta-tags-optimizer](./meta-tags-optimizer/SKILL.md) — Use when the user asks to "optimize meta tags".
- [internal-linking-optimizer](./internal-linking-optimizer/SKILL.md) — Use when improving internal link structure, anchor text, orphan pages, crawl depth, site architecture, or link equity flow.
- [schema-markup-generator](./schema-markup-generator/SKILL.md) — Use when the user asks to "generate schema"; creates JSON-LD for FAQ, HowTo, Article, Product, and LocalBusiness rich-result candidates.

### Content quality and AI visibility

- [seo-content-writer](./seo-content-writer/SKILL.md) — Use when the user asks to "write SEO content".
- [content-quality-auditor](./content-quality-auditor/SKILL.md) — Use when auditing content quality, E-E-A-T, publish readiness, or 内容质量/EEAT评分.
- [content-refresher](./content-refresher/SKILL.md) — Use when updating outdated content, fixing traffic/ranking decay, refreshing stats, adding new sections, or improving freshness signals.
- [geo-content-optimizer](./geo-content-optimizer/SKILL.md) — Use when the user asks to "optimize for AI citations".
- [entity-optimizer](./entity-optimizer/SKILL.md) — Use when the user asks to "optimize entity presence".

### Authority, monitoring, and reporting

- [backlink-analyzer](./backlink-analyzer/SKILL.md) — Use when analyzing backlink profiles, link authority, toxic links, link-building opportunities, or competitor link gaps.
- [domain-authority-auditor](./domain-authority-auditor/SKILL.md) — Use when auditing domain authority, trust, citations, or 域名权威/网站可信度.
- [rank-tracker](./rank-tracker/SKILL.md) — Use when the user asks to "track rankings"; monitors keyword/SERP changes from provided exports or connected tools, including AI response checks.
- [alert-manager](./alert-manager/SKILL.md) — Use when the user asks to "set SEO alerts"; configures ranking, traffic, technical, competitor, and notification thresholds.
- [performance-reporter](./performance-reporter/SKILL.md) — Use when generating SEO/GEO reports, traffic summaries, ranking reports, KPI dashboards, stakeholder updates, or monthly reports.
- [memory-management](./memory-management/SKILL.md) — Use when the user asks to "remember project context".

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
