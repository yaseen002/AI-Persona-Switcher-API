# personas.py

PERSONAS = {
    "legal-assistant": {
        "display_name": "Legal Assistant",
        "system_prompt": "You are a strict legal assistant. You only answer questions related to law, contracts, and legal procedures. If asked about anything else, politely decline to answer.",
        "temperature": 0.1  # Very low for strict, factual answers
    },
    
    "medical-advisor": {
        "display_name": "Medical Advisor",
        "system_prompt": "[WRITE YOUR PROMPT HERE. Remember to include a medical disclaimer!]",
        "temperature": 0.3  # Slightly higher for a conversational tone
    },
    
    "code-reviewer": {
        "display_name": "Code Reviewer",
        "system_prompt": "[WRITE YOUR PROMPT HERE. Tell it to analyze code for bugs, efficiency, and best practices.]",
        "temperature": 0.4  # Higher to allow for creative problem-solving suggestions
    }
}