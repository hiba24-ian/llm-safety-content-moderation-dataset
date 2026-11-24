# LLM Safety & Content Moderation — Rule-Based Demo

A small Python demonstration of checking text against a configurable list of moderation keywords and categories.

## What it demonstrates
- Loading moderation categories and sample cases from JSON
- Scanning text for configured keyword matches
- Reporting the category, severity label, and matched keyword

## Run
```bash
python audit_script.py
```

## Important scope and limitations
This is a simple keyword-matching demonstration, not a production moderation system or a complete safety classifier. It can miss harmful content that uses different wording and can flag harmless text when a keyword appears in a benign context. It does not understand meaning, intent, context, or policy nuance.

## Files
- `audit_script.py` — keyword audit logic
- `moderation_rules.json` — sample categories, keywords, and test prompts

## Author
Hiba Almamoori
