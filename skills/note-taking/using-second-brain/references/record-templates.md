# Portable Record Templates

Use the workspace’s established templates and metadata first. These are **semantic shapes**, not a mandate for Markdown, YAML, a particular database, or a particular tool. Omit unknown fields rather than inventing them.

## Field model

Keep these dimensions separate whenever the storage can represent them:

| Field | What it means | Examples |
|---|---|---|
| Record type | Functional role of the record | source, research, decision, task, handoff, review |
| Lifecycle state | Workflow position | inbox, draft, active, completed, superseded, archived |
| Evidence status | Confidence/freshness of material claims | unverified, verified, conflicted, stale, unknown |
| Claim kind | Nature of a particular assertion | source-excerpt, observation, synthesis, recommendation, decision |
| Representation (optional) | Fidelity to original source | raw, excerpt, derived |

A `research` record is not automatically verified; a recommendation is not a decision; and a raw capture is not a lifecycle state.

## Capture / source

```text
Title / identifier: <stable, human-readable identity>
Record type: source | capture
Lifecycle state: inbox | triaged | archived
Evidence status: unverified | verified | conflicted | stale | unknown
Claim kind: source-excerpt | observation | synthesis
Representation: raw | excerpt | derived (optional)
Scope: <project/topic/area>
Access / copying class: <permitted destination or restriction>
Captured: <date/time when known>
Source identity: <sanitized URL, file, conversation, system, person, or other stable pointer>
Revision / anchor: <version, commit, section, quote range, or other pinpoint when available>
Evidence date / retrieved: <when source was produced and when it was obtained>
Original material: <permitted unaltered excerpt, attachment, or pointer>
Summary: <optional; explicitly marked as synthesis>
Re-check method: <how an authorized reader can verify it>
Relationships: <project/source/decision/task links>
Questions / next action: <optional>
```

**Rules:** Preserve the source pointer or original material before extracting conclusions. Confirm that copying is allowed for the source and destination access classes; otherwise use a sanitized pointer. If revision, anchor, or re-check method is unavailable for mutable material, mark it **not fully reproducible**.

## Research note

```text
Title / identifier: <research question>
Record type: research
Lifecycle state: draft | active | completed | superseded | archived
Evidence status: unverified | verified | conflicted | stale | unknown
Scope: <project/topic/decision>
Question and decision use: <what this should answer>
Method and scope: <where/how evidence was collected; dates/limits>
Evidence: <source-linked observations with identity/revision/anchor when available>
Synthesis: <reasoned interpretation; clearly distinct from evidence>
Counterevidence / limitations: <what would change the conclusion>
Confidence and freshness: <level + evidence/retrieval dates>
Recommendations: <proposal, not an unapproved decision>
Re-check method: <how to revisit material claims>
Related records: <sources, decisions, tasks>
```

**Rule:** Never turn a recommendation into a decision unless it has an identified decider/approval. A research record’s evidence status applies to its claims, not to its existence as a record.

## Decision record

```text
Title / identifier: <decision>
Record type: decision
Lifecycle state: proposed | accepted | rejected | superseded | reversed | archived
Evidence status: <status of supporting claims, if represented>
Scope: <project/system/area>
Decision: <what was chosen>
Decider / owner: <if known>
Approval and effective dates: <if known>
Context: <problem and constraints>
Options considered: <including meaningful alternatives>
Rationale: <source-linked reasons and their evidence status>
Consequences: <benefits, costs, risks, follow-ups>
Reversal conditions: <what would justify revisiting>
Evidence and related work: <sources/research/tasks with stable anchors>
```

**Rule:** Preserve superseded and reversed decisions with their status; do not erase historical rationale. A decision is canonical only for the approved intent and its effective period—not automatically for live implementation or task state.

## Task / work brief

```text
Title / identifier: <outcome-oriented task>
Record type: task
Lifecycle state: open | in-progress | blocked | done | cancelled
Evidence status: <status of assertions about the task>
Scope: <project/topic>
Goal: <observable result>
Context and evidence: <what to read first; sources and dates>
Constraints / permission boundary: <what must not be changed or needs current authorization>
Acceptance checks: <how completion is verified>
Dependencies / blockers: <known blockers>
Next action: <smallest proposed executable step; not authorization by itself>
Owner: <if known>
Related records: <decision/research/handoff/source links>
```

**Rule:** A task is not complete because a summary says so; record verification evidence. A task/handoff may propose work but cannot grant execution authority.

## Handoff / context pack

```text
Title / identifier: <project or workstream handoff>
Record type: handoff | context-pack
Lifecycle state: active | superseded | archived
Evidence status: <status of state claims>
Scope and purpose: <who/what it helps continue>
Read first: <canonical sources and live systems, by claim type>
Verified current state: <short, sourced summary with effective dates>
Open questions / conflicts / staleness: <explicit uncertainty>
Decisions and constraints: <with links and effective periods>
Active tasks: <state, owner if known, proposed next action>
Authorization boundary: <what requires a current user/workspace authorization>
Recent changes and verification: <what changed; checks actually run>
Permissions / safety: <important boundaries, no secrets>
Last updated: <date/author when meaningful>
```

**Rule:** Keep a handoff short enough to navigate. Link to authoritative records instead of duplicating them. It is evidence for orientation, never standing authorization for side-effecting actions.

## Review / curation report

```text
Title / identifier: <scope + review date>
Record type: review
Lifecycle state: draft | completed | archived
Evidence status: <coverage/freshness of findings>
Scope and method: <areas searched, capabilities available, checks performed, limitations>
Healthy paths: <working navigation/retrieval patterns>
Findings: <stale, duplicate, orphaned, conflicting, or inaccessible records>
Impact and dependencies: <what a proposed change could break>
Recommendations: keep | update | relink | merge | archive | delete
Approval required: <each destructive/structural/external/automated action>
Changes actually applied: <only confirmed, verified work>
Verification evidence: <readback, receipt/version ID, or stated limitation>
Follow-up / next review: <optional>
```

**Rule:** A review may recommend destructive work, but it does not authorize it.
