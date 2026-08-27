# LLM Safety & Content Moderation Dataset

A structured evaluation toolkit and dataset designed to assess Large Language Model (LLM) safety compliance, toxicity filtering, and automated content moderation rules.

## Features
- **Safety Policy Categorization:** Structured JSON dataset defining severity levels and categories for content moderation (e.g., toxicity, hate speech, misinformation, and PII leakage).
- **Automated Auditing Script:** A Python-based script that scans inputs/outputs against predefined safety rules and flags policy violations.
- **Responsible AI Alignment:** Assists in auditing model outputs to ensure safe, ethical, and aligned deployments.

## Project Structure
- `README.md`: Project documentation and overview.
- `moderation_rules.json`: Structured dataset containing test prompts, violation categories, and severity thresholds.
- `audit_script.py`: Python auditing logic for detecting and scoring policy infractions.

## How to Run
1. Ensure Python is installed on your system.
2. Clone the repository:
   ```bash
   git clone [https://github.com/hiba24-ian/llm-safety-content-moderation-dataset.git](https://github.com/hiba24-ian/llm-safety-content-moderation-dataset.git)
