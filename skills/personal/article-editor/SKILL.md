---
name: article-editor
description: "Use when writing or editing articles and explainers."
---

# Article Editor

Create a coherent text that answers the reader's question. Prioritize accuracy and logic → necessary explanations → clarity → brevity. Shortening helps only when meaning is preserved.

## When to Use

Writing, rewriting, shortening, and editing explanatory, workplace, and analytical articles. Triggers include "write an article," "make this clearer," "cut the fluff," and "check the logic." Do not apply this process to short chat replies, creative fiction, or requests to fix typos only. Follow the user's requested language and format.

## Process

1. **The reader's task.** Infer the audience, main question, prior knowledge, and intended reading outcome from the context. Use information already provided. Ask only about a gap that changes the content or conclusion; otherwise, proceed with a reasonable interpretation. This step is complete when it is clear what belongs in the article and what does not.

2. **Content outline.** Identify each section's main point and value to the reader. Arrange explanations in the order needed for understanding: introduce necessary concepts before using them and provide grounds before drawing conclusions. In a practical article, give the main answer early. If the user asks to approve the outline, stop at the outline. Otherwise, keep the outline internal and deliver the article.

3. **Draft.** Develop one idea per paragraph. When editing, preserve the author's meaning and tone; correct unsupported certainty rather than amplifying it. Use lists for steps or enumerations and tables for comparisons. Add examples where an abstraction would otherwise remain unclear.

4. **Check logic and support.** Build an internal reverse outline: the idea and function of each paragraph. Fix leaps in reasoning, contradictions, and unsupported conclusions. Distinguish observation from causation, assumptions from facts, and local results from generalizations. Check key claims against the supplied material; verify external facts with tools when the task allows research. Acknowledge missing information rather than filling gaps with invented data or references. When sources conflict, preserve the distinctions: if the conflict prevents a usable instruction, ask for the current source or explicitly label the text as partial. Do not choose the most convenient version.

5. **Edit.** Explain necessary terms clearly at first use. Remove generic introductions, empty judgments, and digressions. For a short practical article, use this structure: main answer → necessary grounds and conditions → next step. Put each supporting point in one place; check for semantic repetition even when the wording differs. If the next step is already given, end the article: a separate conclusion repeating the answer or limitation is unnecessary. Add a caveat only when there is genuine uncertainty; do not turn an explicit condition into an unnecessary question. Follow the user's length requirements; do not impose your own word quotas, character limits per paragraph, or percentage reductions.

6. **Verify meaning.** After editing, check numbers, dates, terms, actors, action order, conditions, exceptions, and degree of certainty. Add an explanation where a logical connection is missing. This step is complete when the text meets the original need and remains accurate after shortening.

## Output

By default, deliver the finished article without internal outlines, checklists, self-assessments, or editing reports. Explicitly disclose any real limitation that prevents the article from being used. If analysis is requested, identify the specific passage, defect, and correction.

## Common Mistakes

- Polished wording does not prove a claim true: check its support separately.
- A shorter text is not necessarily clearer: preserve necessary connections and limitations.
- When the user requests finished text, do not substitute approval of an obvious outline.
- Use meaningful paragraphs for this process, not mechanical splitting borrowed from other templates.

Use `references/examples.md` to calibrate editing decisions.
