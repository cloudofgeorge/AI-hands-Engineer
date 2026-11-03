# Skill Rationale and Validation

This file is a maintenance reference, not a required step for every article.

## Method Sources

- Google, the reader's task and document scope: https://developers.google.com/tech-writing/one/documents
- UW–Madison, reverse outlining paragraphs: https://writing.wisc.edu/handbook/processandstructure/reverseoutlines/
- GOV.UK, clear language and explaining terms: https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language
- Purdue, conciseness is not the same as minimum length: https://owl.purdue.edu/owl/general_writing/academic_writing/conciseness/index.html
- Anthropic, minimal instructions, examples, and baseline comparisons: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Hermes, skills and supporting materials: https://hermes-agent.nousresearch.com/docs/guides/work-with-skills

These are editorial and technical recommendations, not proof that the skill is universally effective. Do not mechanically transfer English-language length limits to Russian.

## Regression Scenarios

After a substantial skill change, test the following in fresh contexts:

1. **False causality:** a pilot in one group, training and a new tool introduced simultaneously, fewer complaints, and no measurement of time spent working. Expected: neither a causal effect nor a benefit for everyone is declared proven; the conclusion stays within the data; the next step is framed as a recommendation.
2. **Conditions preserved when shortening:** an action is permitted for the owner, while an administrator only assigns the owner; there are restrictions on the period and link lifetime. Expected: roles, time limits, order, and exceptions are preserved; generic wording is removed.
3. **Conflicting sources:** two undated policies with different thresholds. Expected: no arbitrary choice; a clarification question or an explicitly partial article; shared requirements are preserved.
4. **Excessive caution and repetition:** a condition is already unambiguous, and a requirement is repeated at the beginning and end. Expected: the condition is preserved without artificial doubt; repetition is removed if it serves no new function.

Use the same source data and model with and without the skill. Evaluate accuracy, logic, necessary completeness, clarity, and unnecessary content separately. Read every response; automatically measured length does not prove quality. Do not count a successful baseline as an improvement caused by the skill. Instructional scenarios do not replace testing on the user's articles.

Test discovery separately from application: explicitly loading SKILL.md proves only application. Being listed in the catalog does not guarantee automatic selection for every request. For explicit invocation, the user can write: "Use article-editor."
