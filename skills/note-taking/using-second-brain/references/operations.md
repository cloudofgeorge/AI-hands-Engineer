# Evidence, Capability Fallbacks, and Migration

Read the relevant section for constrained storage, conflicting or consequential claims, cross-boundary capture, or setup/migration. These procedures supplement the permissions and verification rules in [SKILL.md](../SKILL.md).

## Contents

- [Capability fallback matrix](#capability-fallback-matrix)
- [Source-of-truth and evidence policy](#source-of-truth-and-evidence-policy)
- [Cross-boundary capture](#cross-boundary-capture)
- [Setup or migration](#setup-or-migration)

## Capability fallback matrix

A missing capability is a constraint, not permission to simulate it. Use the strongest available substitute and report its limits:

| Missing capability | Permitted fallback | Required report / stopping rule |
|---|---|---|
| Search or duplicate detection | Use a user-designated destination and stable identifier; inspect direct references that are available. | State that duplicate detection/search coverage was unavailable; never claim uniqueness or absence. |
| Readback | Keep a durable receipt, record/version ID, append-log position, signed acknowledgement, or other storage-native evidence. | Report “written, not independently read back” and the receipt. If there is no evidence of acceptance, do not claim a material write succeeded. |
| Discoverability / links | Return the stable record ID or destination supplied by the storage. | Do not claim the record is discoverable; record the navigation limitation. |
| Targeted edit / version history | Create a clearly scoped addendum or correction rather than overwrite manual content. | Preserve the prior record; state that a non-destructive update was used. |
| Backup / rollback | Produce an inventory/manifest and a dry-run or pilot plan when feasible. | Do not perform an irreversible bulk migration unless the workspace owner explicitly accepts the residual risk and the plan states it. |
| Any write capability | Work in retrieval, proposal, or user-copyable draft mode only. | State that no durable record was created. |

## Source-of-truth and evidence policy

There is no universal source hierarchy. Determine authority **per claim type, scope, and effective date** from the brain contract or workspace policy. Typical mappings are:

| Claim type | Canonical system to identify | Effective date to capture |
|---|---|---|
| Implemented behavior or configuration | The designated live/runtime or versioned implementation source | Observed/deployed/version date |
| Approved intent, policy, or plan | The designated approved decision/policy record | Approval date and validity period |
| Operational state | The designated operational system or signed report | Observation/reporting window |
| Work status and ownership | The designated task/work-tracking record | Last confirmed update |
| External fact | The primary publisher, dataset, or authoritative issuer | Publication/evidence date and retrieval date |

A source has precedence only for the claim it governs; a current implementation does not silently supersede an approved future decision, and a decision does not prove current runtime state.

When two sources disagree:

1. Identify the exact claim, claim type, scope, and effective date.
2. Identify the canonical source for that combination and compare provenance/revisions.
3. Preserve both records; record the conflict with links, dates, and scopes.
4. Mark the retrieval aid as conflicted or stale rather than silently choosing one.
5. Ask the user/owner to decide when evidence cannot resolve a material conflict.

### Independent record dimensions

Use the [field model](record-templates.md#field-model) without imposing a new schema. Do not infer `verified` from a record type such as research, or a decision from a recommendation. When a storage supports only one label, preserve the distinction in explicit prose rather than collapsing the axes.

### Reproducible provenance

For important, mutable, or decision-driving sources, store what the destination can support: stable source ID/URI, revision/version/commit where available, retrieval timestamp, evidence/publication date, precise anchor or quoted range, and a re-check method. A content hash may supplement—not replace—a source identity. If these are unavailable, label the claim as **not fully reproducible** and state why.

## Cross-boundary capture

Before moving or copying material between workspaces, access classes, teams, or systems:

1. Confirm the source’s access/sensitivity class, copying/licensing permission, and the destination’s approval for that class.
2. Remove signed URLs, credentials, sensitive query parameters, hidden metadata, and unnecessary personal data; use a sanitized pointer when possible.
3. Do not copy restricted material into a broader or less-protected destination. If rights, destination approval, or classification are unclear, stop and request a decision.
4. Record only the minimum permitted provenance and access restriction needed for future authorized retrieval.

## Setup or migration

Use when building or substantially reshaping a Second Brain.

1. Inventory existing content, identifiers, navigation, schemas, links, attachments, automations, integrations, owners, permission boundaries, and approximate counts.
2. Draft a migration/integrity plan before broad change: source and destination scope, field/type mapping, old-to-new identifier/link mapping, attachment treatment, exclusions, pilot/dry-run, verification checks, rollback/restore route, owner, and acceptance criteria.
3. Check whether existing user authorization covers the concrete change and its impact. Obtain approval only for scope not already authorized. A general setup request does not authorize moving existing records, external syncing, or integrations. Approval for an irreversible bulk operation must cover the documented residual risk if no backup/rollback exists.
4. Back up or create a reversible checkpoint when the storage permits it. Sync alone does not prove recoverability; verify an independent restore route, including attachments and metadata. If backup/rollback is unavailable, retain a versioned inventory/manifest and run a small pilot or dry run before any irreversible bulk operation. Do not migrate blindly.
5. For a new workspace, implement the smallest design within the authorized destination; for migration, apply the agreed mapping. Include only what is needed: capture location, project/topic hubs, source/research/decision/task records, retrieval method, metadata baseline, templates, review cadence, and archive policy.
6. Establish a source-of-truth policy and a minimal brain contract before adding automation or bulk taxonomy.
7. Implement in small stages. After each stage, reconcile expected vs actual counts, mapped identifiers/links, attachments, navigation, permissions, and a sample of retrievable records; record exceptions and recovery results.

Default to simple, portable primitives: clear names, structured metadata where supported, links/relations, indexes, templates, and search. Do not install a plugin, database, embedding system, agent integration, or automation merely because it may be useful.

**Done when:** the agreed stage meets its acceptance criteria; its inventory, mapping, verification results, exceptions, and recovery/rollback status are documented; and it is usable and navigable for authorized humans and future agents.
