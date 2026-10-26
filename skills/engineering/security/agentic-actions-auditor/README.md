# agentic-actions-auditor

Portable adaptation of Trail of Bits guidance. Read the selected skill by path and keep its references and reusable helpers together. Native plugin manifests, commands, hooks, UI metadata, runtime orchestration, and plugin-only evaluation harnesses have been removed. The analysis methods and supporting material are retained; this version does not inherit the original plugin runtime or benchmark guarantees.

## Skills

- [agentic-actions-auditor](./skills/agentic-actions-auditor/SKILL.md) — Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

## Attribution and use

Derived from [Trail of Bits skills](https://github.com/trailofbits/skills). Local portability adaptations made on 26 October 2026. Retain the [CC BY-SA 4.0 license](../LICENSE-trailofbits) when copying this material. Use the current host's real permissions and capabilities; prompts do not enforce isolation.
