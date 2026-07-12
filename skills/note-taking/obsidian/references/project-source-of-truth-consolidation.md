# Project source-of-truth consolidation pattern

Use this reference when a user asks to update Obsidian so one project area becomes the canonical source of truth for a software/product effort, especially when the implementation spans multiple repos.

## Trigger example

User says two folders/repos are parts of one larger project and asks to update the Obsidian Second Brain so future retrieval treats it as a unified source of truth.

## Workflow

1. Load the Obsidian skill and inspect current vault navigation:
   - Home dashboard
   - Retrieval dashboard
   - Review dashboard
   - Hermes/project review workflows
   - Existing project folder or matching notes
2. Inspect both repos enough to extract durable facts:
   - README and AGENTS/project instruction files
   - architecture/system design docs
   - package manifests/build files
   - API contracts/endpoints
   - data models/schema files
   - CI/deployment/infra files
   - task/bug/tech-debt docs
   - git branch, short HEAD, and dirty/untracked status for an inspection snapshot
3. Create one canonical project area when the user says the repos belong to one project:
   - `Projects/<Project>/<Project>.md`
   - `Projects/<Project>/<Project> Dashboard.md`
   - `Projects/<Project>/Context Pack - <Project>.md`
   - `Projects/<Project>/Architecture/INDEX.md`
   - component architecture notes, e.g. app/client and web/API platform
   - `API Contracts.md`, `Data Models.md`, `Operations and Deployment.md`
   - spec, roadmap, task board, launch checklist
   - review/decision/research/meeting index notes as useful
4. Make retrieval robust:
   - Add aliases for product names, repo names, old names, and component names.
   - Link from the dashboard and context pack to all major notes.
   - Include absolute repo paths and important source files.
   - Record explicit project rules, e.g. “repo X is a component, not a separate Obsidian project.”
5. Write notes with full markdown content using `write_file` or a small script that calls `write_file`.
6. Verify the result before reporting completion.

## Content checklist

The canonical project note should include:

- identity and repo map
- product summary
- architecture diagram or text map
- main user/product surfaces
- monetization or business model if relevant
- current inspection snapshot
- important source docs
- durable project rules/update protocol

Architecture notes should include:

- system boundary and privacy/data boundary
- technology stack
- composition/root modules
- services/integrations
- critical flows
- endpoint/API contract map
- data persistence model
- operations/deployment commands and risks

Context pack should include:

- one-paragraph context
- retrieval priority
- key source files/directories
- search queries
- known risks/cleanup items
- update protocol

## Python generation pitfall

When generating markdown from Python, do not use large f-strings if the markdown contains literal braces, JSON examples, schema examples, or key templates such as:

```text
veilframe.apikey.{provider}
{ status, currentPeriodEnd }
[{ role: system|user|assistant }]
```

Python will treat `{...}` as interpolation and may fail with `NameError` before writing any files. Safer patterns:

- Use normal triple-quoted strings and replace a sentinel such as `__UPDATED__`.
- Or escape literal braces as `{{...}}` inside f-strings.
- Or build small variables separately and avoid embedding JSON-like examples in f-strings.

## Verification checklist

After writing:

- List `Projects/<Project>/**/*.md` and confirm expected files exist.
- Check every new note starts and ends frontmatter with `---`.
- Check required keys: `type`, `status`, `created`, `updated`; include `project` where appropriate.
- Search for unresolved placeholders such as `__UPDATED__`.
- Parse wikilinks and verify targets by note stem, relative path, vault path, and aliases.
- Read the canonical note and context pack back to verify legibility and navigation.
- Re-check repo branch/HEAD/dirty status if the notes include an inspection snapshot.

## Reporting pattern

Keep the final report concise:

- Explain any interruption/fix if relevant.
- List where the source-of-truth project area lives.
- Name the key entry points.
- Report verification counts: files written, frontmatter issues, placeholder hits, wikilinks checked/unresolved.
- Mention notable repo dirty/untracked state as risks, not as changes made.
