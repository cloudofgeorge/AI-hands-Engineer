# Brain Contract

A Brain Contract is a short, human-readable operating agreement for a knowledge workspace. It prevents an agent from guessing locations, authority, storage behavior, or permission boundaries.

Create or update it only when the workspace owner requests setup/maintenance or when an existing contract must be corrected. Do not manufacture a contract for a narrow retrieval request.

## Required fields

| Field | What it answers |
|---|---|
| Workspace identity | What this knowledge workspace is called and who owns it. |
| Root / entry point | Where to start browsing; may be a folder, collection, database, repository, URL, or named home record. |
| Access adapter | Capabilities actually available: read, search, create, targeted edit, relations/links, attachments, and verification evidence (readback, receipt, version ID, append log, acknowledgement). Include known missing capabilities and fallback/reporting rules. |
| Navigation | Canonical indexes/hubs and the preferred route for projects, areas, resources, people, inbox, archive, and reviews. |
| Authority by claim | For each claim type (implemented state, approved intent, operations, work status, external fact), specify its canonical system/record and effective-date rule. |
| Schema and templates | Existing record types, required metadata, naming rules, link/alias convention, templates, and any separate fields for lifecycle, evidence status, and claim kind. |
| Change permissions | What may be edited directly; what current authorization is required for execution-side effects; and which actions require explicit approval. |
| Data boundaries | Sensitivity/access classes, rights to copy, approved destinations, redaction rules, and how restricted sources are safely referenced. |
| Lifecycle | Capture/triage, update, review, archive, retention, stale-content conventions, and recovery/rollback expectations. |
| Automation/external systems | Existing jobs/integrations, owners, boundaries, and the requirement for approval before changes. |
| Migration integrity | Inventory/manifest, ID/link/attachment mapping, pilot/dry-run, reconciliation, recovery/rollback, and residual-risk acceptance requirements. |
| Verification | Readback, receipt/version evidence, metadata/link validation, search/discoverability, and backup/version checks supported by the storage. |

## Minimal portable example

```text
Workspace: <human-readable name>
Owner: <person or team>
Entry point: <stable root, collection, database, or home record>
Access adapter: read; search; create; targeted-edit; verify-by-readback | receipt/version-ID; missing capabilities: <...>
Canonical navigation: <system index>; <project hubs>; <inbox>
Authority by claim: implemented state → <canonical source + date rule>; approved decisions → <...>; task state → <...>; external facts → <...>
Schema: inherit existing fields; record type / lifecycle / evidence status / claim kind are <fields or prose convention>
Permissions: direct content updates in <scope>; current authorization for <execution effects>; confirmation for <structural/destructive/external/automated scope>
Data boundaries: <access classes>; copy allowed from <source classes> to <destinations>; sanitize <URLs/attachments/metadata>; never store secrets
Lifecycle: capture → triage → maintain → review → archive by <policy>
Migration integrity: <manifest + mapping + pilot + reconciliation + rollback/residual-risk policy>
Verification: <readback or durable receipt> + <discoverability if available> + relevant link/metadata checks
```

## Discovery procedure

1. Ask the workspace owner for the entry point if no trustworthy location is discoverable.
2. Read the top-level guidance, navigation records, schemas/templates, and permission policy.
3. Test only non-destructive adapter capabilities that are needed for the requested operation.
4. Record facts, not aspirations: “search is unavailable” is better than claiming an index exists.
5. If a field is unknown, mark it unknown and ask only when it blocks safe progress.
6. Keep the contract compact; link to detailed policies rather than duplicating them.

## Rules

- A contract describes the workspace; it is not authority over the user or a substitute for the user’s request.
- The contract must not contain credentials, tokens, private access URLs, or copied sensitive records.
- Review it after a migration, new integration, schema change, ownership change, or repeated retrieval failure.
- If it conflicts with a higher-precedence current policy or the user’s explicit request, surface the conflict instead of silently following stale text.
