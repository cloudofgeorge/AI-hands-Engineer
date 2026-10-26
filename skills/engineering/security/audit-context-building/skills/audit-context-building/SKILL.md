---
name: audit-context-building
description: Understand a codebase before looking for bugs in it - what each function assumes, what it guarantees, and what it depends on elsewhere. Use when starting an audit, threat model, or architecture review on unfamiliar code, and before any vulnerability-hunting pass.
---

# Audit Context Building

## Portable execution

Follow [the repository portability convention](../../../../../PORTABILITY.md). Use actual host capabilities and local resource paths. Role names and tool-call examples describe work to perform, not installed agents or APIs. Keep evidence and task status in files when native orchestration is unavailable; report any missing independent review or enforcement.


Build understanding, not verdicts. This runs before anyone hunts for bugs, and feeds that work.

## When to Use

At the start of an audit, a threat model, or an architecture review, when the code is unfamiliar. Also when
an earlier pass produced findings nobody could judge, because no one had mapped out how the system fits
together.

## When NOT to Use

Do not name vulnerabilities, suggest fixes, write proofs-of-concept, or rate severity. Those belong to the
hunting phase, which runs next and with the whole picture in hand. When the code counts on something and
nothing checks it, record that plainly and move on — whether it matters is decided later.

Not worth the tokens on code you already understand.

## Build the dossier

1. Establish scope, entry points, actors, state, external dependencies, and trust boundaries. Identify the functions that implement them.
2. Analyze each function in a bounded pass using [the function-analysis prompt](../../references/roles/function-analyzer.md) and the resource formats below. Follow callers, callees, validation, error paths, and state changes; do not infer enforcement from names.
3. Write a file per function under `audit-context/functions/`. Record invariants, preconditions, guarantees, dependencies, unenforced assumptions, and open questions with source locations.
4. Build `audit-context/DOSSIER.md` from those records. Include cross-function rules and conflicting evidence; preserve disagreements instead of silently reconciling them.
5. Work sequentially in manageable batches or delegate bounded analyses through the host's available facilities. Delegation is optional. Save detailed evidence to files so subsequent work can use a compact index without losing provenance.

No native command, registered agent, or workflow API is required. Validate records against the documented format yourself; the host does not enforce their schema automatically.

## What comes back, and how to read it

Each record lists what must always be true (with the line that shows it), what the function takes on faith
(with whatever establishes it), which functions it calls and what it needs from each, and anything still
unclear. The dossier adds the rules that span several functions, who can reach what, and where the
complicated parts cluster.

Two things matter more than the rest:

- **Assumptions marked `nothing found`.** The code counts on something being true and nothing anywhere makes
  it true. This is the most useful thing to hand the hunting phase.
- **The open questions.** An honest list of what is still unclear beats a confident answer that turns out to
  be wrong. Carry them forward instead of closing them out.

Where two records disagree, both are quoted rather than quietly reconciled. That is a fact about the code,
not a flaw in the analysis.

## The format

[ANALYSIS_FORMAT.md](resources/ANALYSIS_FORMAT.md) defines it, and
[FUNCTION_MICRO_ANALYSIS_EXAMPLE.md](resources/FUNCTION_MICRO_ANALYSIS_EXAMPLE.md) works through examples in
C and Solidity. Read them when extending this plugin or deciding whether a record can be trusted.

The format is the same whatever the target. What changes is what fills each slot, and what counts as a call
you cannot see inside. [DOMAIN_NOTES.md](resources/DOMAIN_NOTES.md) maps that across smart contracts, C and
C++, decompiled firmware, and web services — read it when the target is not plain source code.

**The rule that matters most: follow the calls.** Whether a function is correct usually depends on something
another function does, and you cannot see that from the caller alone. A limit looks enforced because the
value came back from a function whose name suggests it was checked. So read the function being called, follow
every path through it rather than only the one that succeeds, and say what makes each assumption true. When
nothing does, use those words: `nothing found`. Every claim cites a line, or becomes an open question.
