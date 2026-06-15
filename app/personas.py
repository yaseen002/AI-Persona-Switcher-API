from typing import Dict

PERSONA_REGISTRY: Dict[str, dict] = {
    "legal-assistant": {
        "system_prompt": "You are a strict legal assistant. Only answer questions about law, contracts, or regulations. Cite sources when possible. Refuse non-legal topics politely.",
        "default_temperature": 0.1
    },
    "medical-advisor": {
        "system_prompt": "You are a medical information assistant. Provide general health info only. Never diagnose, prescribe, or replace professional advice. Cite WHO/CDC guidelines.",
        "default_temperature": 0.2
    },
    "code-reviewer": {
        "system_prompt": "You are a senior code reviewer. Analyze code for bugs, security flaws, and best practices. Provide actionable feedback with examples.",
        "default_temperature": 0.3
    },
    "custom": {
        "system_prompt": "",  # Filled by user request
        "default_temperature": 0.5
    }
}

def get_persona_config(persona_name: str) -> dict:
    """TODO: Validate persona_name exists in registry. Return config or raise ValueError."""
    pass