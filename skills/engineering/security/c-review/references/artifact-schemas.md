# Artifact schema reference

Data-shape definitions retained from the original review implementation. These are reference notation, not an executable host workflow. Read alongside the Python validator and assembler when producing machine-readable artifacts.

```javascript
const DETECT_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: [
    'is_cpp', 'is_posix', 'is_windows', 'platform_evidence', 'purpose', 'entry_points',
    'trust_boundaries', 'existing_hardening', 'state_structs', 'class_evidence',
    'units_ok', 'units_summary', 'assignment_ids',
  ],
  properties: {
    is_cpp: { type: 'boolean', description: 'C++ translation units are compiled, not merely C headers guarded by extern "C"' },
    is_posix: { type: 'boolean', description: 'the code actually calls POSIX APIs on the build path being audited' },
    is_windows: { type: 'boolean', description: 'the code actually calls Win32 APIs on the build path being audited' },
    platform_evidence: { type: 'string', description: 'one line per flag set true, each citing a path:line that shows real API usage' },
    purpose: { type: 'string' },
    entry_points: { type: 'array', items: { type: 'string' }, description: 'where untrusted data enters, as path:line plus one phrase' },
    trust_boundaries: { type: 'array', items: { type: 'string' } },
    existing_hardening: { type: 'array', items: { type: 'string' }, description: 'fuzzers, sanitizers, assertions, privilege separation actually present in the tree' },
    state_structs: {
      type: 'array',
      description:
        'long-lived mutable structs threaded through the code whose fields carry rules across function boundaries. One entry per struct as "path:line StructName — what it is for". Empty is a valid answer for code with no such struct.',
      items: { type: 'string' },
    },
    class_evidence: {
      type: 'array',
      description: 'one entry per bug class you were asked about',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['bug_class', 'has_candidates', 'citation'],
        properties: {
          bug_class: { type: 'string' },
          has_candidates: { type: 'boolean', description: 'true only if you can cite a real candidate site in the source' },
          citation: { type: 'string', description: 'path:line of one candidate site, or the concrete reason there is none' },
        },
      },
    },
    units_ok: { type: 'boolean', description: 'enumerate_units.py exited 0 and wrote units.json' },
    units_summary: { type: 'string', description: 'the totals block the script printed, or its error text' },
    assignment_ids: { type: 'array', items: { type: 'string' }, description: 'the assignment ids the script produced, e.g. unit-01' },
  },
}

const LEDGER_ROW = {
  type: 'object',
  additionalProperties: false,
  required: ['unit_id', 'question', 'verdict', 'sites_accounted', 'evidence'],
  properties: {
    unit_id: { type: 'string', description: 'copied exactly from your assignment file' },
    question: { type: 'string', description: 'one of the question ids listed for that unit' },
    verdict: {
      type: 'string',
      enum: ['clean', 'finding', 'needs-human', 'not-applicable'],
      description:
        'clean means you accounted for every counted site and none is a bug. finding means at least one is, AND you still accounted for the rest. not-applicable is only valid when the counted population is empty.',
    },
    sites_accounted: {
      type: 'array',
      items: { type: 'integer' },
      description:
        'the line numbers of this question\'s sites in this unit, as you found them by reading the source. They are deliberately NOT in your assignment file, which gives only the count. Every verdict except not-applicable must list ALL of them, needs-human included — a gate compares this against the parse, not against your description of what you did.',
    },
    evidence: { type: 'string', description: 'what you found at those sites, including at the ones you did not file' },
  },
}

const FINDING_PROPERTIES = {
  bug_class: { type: 'string', description: 'one of the class ids listed in the prompt, or the closest one if the bug is outside them' },
  title: { type: 'string' },
  file: { type: 'string', description: 'repo-relative path, no markdown link, no absolute path' },
  line: { type: 'integer', minimum: 1 },
  function: { type: 'string', description: 'the single enclosing function, or (file-level)' },
  unit_id: { type: 'string', description: 'the unit id this bug sits in, copied from your assignment file; empty if it is outside your units' },
  confidence: { type: 'string', enum: ['High', 'Medium', 'Low'] },
  description: { type: 'string', description: 'the broken invariant and what the attacker controls' },
  code: { type: 'string', description: 'the real snippet, copied not paraphrased' },
  data_flow: { type: 'string', description: 'source, sink and what validation exists between them; N/A for a file-level finding' },
  reachability: { type: 'string', description: 'call chain from an entry point, or the honest limit of what you traced' },
  impact: { type: 'string' },
  mitigations_checked: { type: 'string', description: 'each mitigation you looked for, with the path:line where you found it or the statement that it is absent' },
  recommendation: { type: 'string' },
  outside_assigned_classes: { type: 'boolean', description: 'true when this bug is outside the units or classes you were assigned' },
  // Severity is the reporter's job. There is no judge downstream to assign it,
  // so an omitted severity becomes MEDIUM by default rather than being reviewed.
  severity: { type: 'string', enum: ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW'], description: 'against the table in your prompt, relative to this threat model' },
  attack_vector: { type: 'string', enum: ['Remote', 'Local', 'Both'] },
  exploitability: { type: 'string', enum: ['Reliable', 'Difficult', 'Theoretical'] },
  severity_rationale: { type: 'string', description: 'one line: what makes it this level and not the one above or below' },
}

const FINDING_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['bug_class', 'title', 'file', 'line', 'function', 'confidence', 'description', 'code', 'impact', 'recommendation'],
  properties: FINDING_PROPERTIES,
}

const REVIEW_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['part_written', 'findings', 'ledger'].concat(
    BENCHMARK_MODE ? ['external_sources_consulted', 'external_sources_detail'] : []
  ),
  properties: {
    part_written: { type: 'boolean', description: 'true once you have written your part file to the path given in the prompt' },
    findings: { type: 'array', items: FINDING_SCHEMA },
    ledger: { type: 'array', items: LEDGER_ROW },
    external_sources_consulted: {
      type: 'boolean',
      description:
        'true if you read anything outside this repository while working — upstream sources, a git history, a changelog, an advisory, a CVE record, a search result. Declaring it is expected and carries no penalty; it exists so benchmark runs can be scored honestly.',
    },
    external_sources_detail: { type: 'string', description: 'what you consulted and why, or the single word "none"' },
    pointers: {
      type: 'array',
      description:
        'bugs you noticed OUTSIDE your assigned units. One line each, no write-up: the owner of those lines will do that. Promoted to a finding only if the owner files nothing there.',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['file', 'line', 'note'],
        properties: {
          file: { type: 'string', description: 'repo-relative' },
          line: { type: 'integer', minimum: 1 },
          note: { type: 'string', description: 'one sentence: what looks wrong' },
        },
      },
    },
    notes: { type: 'string', description: 'anything a human should know: units you could not finish, files you could not read, areas that need a person' },
  },
}

const DEDUP_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['merges'],
  properties: {
    merges: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['primary', 'duplicates', 'rationale'],
        properties: {
          primary: { type: 'string', description: 'the candidate key that survives' },
          duplicates: { type: 'array', items: { type: 'string' } },
          rationale: { type: 'string', description: 'one phrase naming the single shared source construct' },
        },
      },
    },
  },
}

const ASSEMBLE_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  // `artifacts_written` is REQUIRED and answered from the DIRECTORY, not the exit code:
  // optional, a gate-rejection return would read as "artifacts were not written" over a
  // complete report.
  required: ['ok', 'artifacts_written'],
  properties: {
    ok: { type: 'boolean', description: 'the script exited 0' },
    artifacts_written: {
      type: 'boolean',
      description:
        'true only if findings.json, REPORT.md and REPORT.sarif are all present in the output directory after the command ran. List the directory; do not infer it from the exit code.',
    },
    reported: { type: 'integer' },
    raw_findings: { type: 'integer' },
    // The assembler runs the ledger gate in-process, so these come back from it directly.
    checks_required: { type: 'integer' },
    checks_completed: { type: 'integer' },
    checks_satisfied: { type: 'integer', description: 'answered AND accepted by the gate' },
    // Part files no assembler rule reads — each is an agent's whole output dropped on
    // the floor, usually a misnamed stem.
    unrecognised_parts: { type: 'integer' },
    error: { type: 'string' },
  },
}


```
