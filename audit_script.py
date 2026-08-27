import json

def load_rules(file_path):
    """Load content moderation rules and test cases from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def audit_text(text, categories):
    """Audit text against forbidden keywords and categories."""
    text_lower = text.lower()
    violations = []
    
    for cat in categories:
        for keyword in cat["forbidden_keywords"]:
            if keyword.lower() in text_lower:
                violations.append({
                    "category": cat["category"],
                    "severity": cat["severity"],
                    "matched_keyword": keyword
                })
    
    return violations

if __name__ == "__main__":
    # Load moderation rules
    moderation_data = load_rules("moderation_rules.json")
    categories = moderation_data.get("categories", [])
    test_prompts = moderation_data.get("test_prompts", [])
    
    print(f"Loaded {len(categories)} moderation categories and {len(test_prompts)} test cases.\n")
    
    for test in test_prompts:
        test_id = test["id"]
        content = test["content"]
        
        violations = audit_text(content, categories)
        
        print(f"Test ID: {test_id}")
        print(f"Content: {content}")
        if violations:
            print("Status: 🔴 Flagged for Violations")
            for v in violations:
                print(f"  - Category: {v['category']} | Severity: {v['severity']} | Keyword: '{v['matched_keyword']}'")
        else:
            print("Status: 🟢 Safe / Passed")
        print("-" * 50)
