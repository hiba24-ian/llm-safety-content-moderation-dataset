# LLM Safety & Content Moderation — Rule-Based Demo

A small Python portfolio exercise that scans sample text against configurable moderation keywords and categories. It demonstrates a basic, explainable rule-based workflow relevant to content quality and Trust & Safety review.

## What it demonstrates

- Loading sample moderation rules and test prompts from JSON
- Scanning text for configured keyword matches
- Reporting matched keywords, category, and severity label
- Keeping example rules separate from the Python audit script

## Run locally

```bash
python audit_script.py
```

## Repository files

- `audit_script.py` — keyword-matching audit logic
- `moderation_rules.json` — illustrative categories, keywords, and test prompts

## Limitations

This is a **keyword-matching demonstration**, not a production moderation system or a complete safety classifier. It does not understand meaning, intent, context, or policy nuance. It may miss harmful content expressed with different wording and may flag harmless content when a configured keyword appears in a benign context. Human review is required for nuanced decisions.

## Related portfolio work

- [AI Quality Lab — English & Arabic](https://github.com/hiba24-ian/i-quality-lab-english-arabic)
- [AI Output Evaluator Engine](https://github.com/hiba24-ian/AI--Output-Evaluator-Engine)

## Author

Hiba Almamoori
