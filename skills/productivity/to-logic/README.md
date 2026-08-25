# To Logic (formal logic)

**Purpose**: Provides the agent with a classical formal-logic framework based on G. Chelpanov's textbook («Учебник логики»). It enables the model to review and fix the logic of Russian texts, perform rigorous logical analysis, construct and evaluate syllogisms, detect logical fallacies, and apply inductive reasoning methods. All reference material is in Russian, distilled from the source book.

## Modes

| Mode | How to invoke | What it does |
|------|---------------|--------------|
| **Review** (`to-logic:review`) | `/to-logic:review <текст>` (plugin command), or ask: «проверь логику», «логическое ревью», «найди логические ошибки» | Analysis-only report: argument structure, every fallacy named (Russian + Latin), why it is an error, how to fix. The text is **not** rewritten. |
| **Fix** (default) | `/to-logic` + text, or ask: «исправь логику», «поправь аргументацию» | Short diagnosis, then the text rewritten with corrected reasoning (author's style preserved, minimal edits) + a list of changes. |
| **Problems** | Give a logic textbook problem | Step-by-step solution: check a syllogism, convert a judgment, find the figure/mood, identify Mill's method, restore an enthymeme. |
| **Benchmark** | Only for explicit BQA (yes/no) / MCQA (A/B/C/D) tasks | Single JSON object `{"reasoning": ..., "answer": ...}` for automated grading. |

**When to use**

- Reviewing or fixing the argumentation of a (Russian) text.
- Analyzing arguments or checking the validity of inferences.
- Classifying concepts, judgments, or logical forms; checking definitions and divisions.
- Building or reducing syllogisms, proving statements, or identifying logical errors.
- Applying the laws of thought (identity, non-contradiction, excluded middle, sufficient reason).
- Performing inductive reasoning using Mill's methods, analogies, or hypothesis evaluation.

**Core workflow**

1. Identify the argument structure: thesis, premises, conclusions.
2. Determine the form of each inference (syllogism, conditional, disjunctive, immediate, induction, analogy).
3. Load the appropriate reference files from `references/` and verify each step against the rules.
4. Name every error (Russian + Latin) and produce the mode-specific output: report, fixed text, or solution.

**Reference files** (in Russian, terminology per Chelpanov)

- `references/concepts.md` — понятия: классификация, определение, деление.
- `references/judgments.md` — суждения: A/E/I/O, логический квадрат, распределённость, непосредственные умозаключения.
- `references/syllogism.md` — силлогизм: фигуры и модусы, сведение, условные/разделительные, энтимемы и сориты.
- `references/induction.md` — индукция: методы Милля, гипотеза, аналогия, классификация.
- `references/errors.md` — каталог логических ошибок, софизмы и паралогизмы.
- `references/laws.md` — четыре закона мышления.

**Docs**

- `docs/konspekt.md` — постатейный конспект всех 26 глав учебника Челпанова: суть, ключевые понятия, приёмы с современными примерами, чек-листы.

**Why it matters**

Embedding a structured logical reasoning skill allows the agent to go beyond heuristic pattern matching and produce traceable, rule-based arguments. This improves reliability for tasks that require precise logical validation, such as reviewing argumentative texts, educational tutoring, formal debate assistance, or error-checking of analytical writing.

## Install

Copy or symlink this directory into a skill root (its `SKILL.md` lives at the directory root):

| Tool          | Path                          |
|---------------|-------------------------------|
| Claude Code   | `~/.claude/skills/to-logic/`      |
| Cursor        | `~/.cursor/skills/to-logic/`      |
| OpenAI Codex  | `~/.codex/skills/to-logic/`       |
| Kimi Code CLI | `~/.kimi/skills/to-logic/`        |

The directory name must match the `name` field in `SKILL.md`.

## How to invoke

- **Slash command** — type `/to-logic` in agent chat; `/to-logic:review` runs the analysis-only mode.
- **`@` context** — attach the skill folder or `SKILL.md` to ground the message in these instructions.
- **Automatic** — the agent may load the skill on its own when your request matches the `description` in `SKILL.md`.
