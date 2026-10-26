# Portable skill convention

This repository stores reusable instructions, reference material, templates, and local helpers. It does not register plugins, slash commands, hooks, custom agents, or model-specific UI metadata.

- Read a skill by its `SKILL.md` path. A host may discover it through its own skill-directory configuration; discovery is separate from the content.
- Resolve relative paths from the file containing them. In imported examples, `{baseDir}` means the directory containing the selected `SKILL.md`. Resolve package-level scripts from that actual file location, never by searching a host's private plugin cache.
- Tool names such as Read, Grep, Bash, Task, or AskUserQuestion describe capabilities. Use the host's available file, search, shell, planning, delegation, and question mechanisms. They are not APIs installed by this repository. A task ledger can be a Markdown checklist or JSON file.
- Treat role documents as prompts or checklists. Pass their content to an available reviewer when delegation is appropriate; otherwise perform the stages sequentially. A sequential self-check is not independent review. If independent reviewers or isolation are required and unavailable, retain findings as unverified and state the limitation.
- Model names, concurrent-worker counts, and scheduling patterns in inherited examples are not prerequisites. Use the current host's models and limits. Never invent a missing tool or claim a prompt enforces runtime permissions.
- Keep the narrow task scope and existing invocation policy. `disable-model-invocation: true` continues to mean explicit user invocation.
- External domain tools such as Git, Python, Semgrep, CodeQL, database clients, and browser automation may still be necessary. Check their prerequisites in the selected skill. Portable instructions do not mean every workflow can execute offline or without tools.
- Preserve licenses and attribution. When adapting imported guidance, describe substantive changes; do not claim that adapted content is an unchanged upstream release or inherits its measured performance.

New skills should keep their actual method in Markdown and reserve scripts for reusable, host-independent work. Put review roles in references, not native agent-registration files. Resolve bundled resources relative to the skill and make missing capabilities visible.
