# Database engineering

Two skills from [supabase/agent-skills](https://github.com/supabase/agent-skills/tree/c9be0e931b7930f7d02126d04774d904c381e7d7), pinned on 26 October 2026. Skill instructions and supporting references are retained; host-specific metadata has been removed. Attribution: Supabase and upstream contributors. See the [MIT license](./LICENSE).

## Model-invoked skills

- [supabase](./supabase/SKILL.md) — Work with Supabase databases, authentication, storage, realtime, integrations, and troubleshooting.
- [supabase-postgres-best-practices](./supabase-postgres-best-practices/SKILL.md) — Review SQL, indexes, schemas, pooling, locking, and row-level security.

The platform skill relies on current Supabase documentation and the tools appropriate to the target project. Database access, CLI authentication, and MCP connections are separate setup steps. None of these manifests disables model invocation.

## Use and updates

Read the selected `SKILL.md` by path and keep its supporting folder intact. This is a portable skill collection; automatic discovery depends on the host's configured skill directories. Refresh discovery or start a new session after updating. No plugin commands, hooks, or native agent registrations are included. External tools and credentials may still require setup.

Update at an explicit revision, retain supporting files and license notices, and refresh the engineering skill count. Validation here covers packaging and file integrity; it does not execute the imported workflows.
