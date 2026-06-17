from typing import Dict

# Renamed to PERSONA_REGISTRY to match your previous code snippet
PERSONA_REGISTRY: Dict[str, dict] = {
    "legal-assistant": {
        "display_name": "Legal Assistant", # Added as requested
        "system_prompt": "You are a strict legal assistant. Only answer questions about law, contracts, or regulations. Cite sources when possible. Refuse non-legal topics politely.",
        "default_temperature": 0.1
    },
    "medical-advisor": {
        "display_name": "Medical Advisor", # Added as requested
        "system_prompt": "You are a medical information assistant. Provide general health info only. Never diagnose, prescribe, or replace professional advice. Cite WHO/CDC guidelines.",
        "default_temperature": 0.2
    },
    "code-reviewer": {
        "display_name": "Code Reviewer", # Added as requested
        "system_prompt": "You are a senior code reviewer. Analyze code for bugs, security flaws, and best practices. Provide actionable feedback with examples.",
        "default_temperature": 0.3
    },
    "custom": {
        "display_name": "Custom Persona", # Added as requested
        "system_prompt": "",  # Filled by user request
        "default_temperature": 0.5
    }
}