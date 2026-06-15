import time
import requests
from app.config import LLM_API_KEY, LLM_API_BASE_URL, LLM_MODEL

def call_llm(system_prompt: str, messages: list, temperature: float) -> dict:
    """
    TODO: 
    1. Build payload (OpenAI/Mistral compatible format)
    2. Add Authorization + Content-Type headers
    3. POST to LLM_API_BASE_URL
    4. Handle timeouts, 429s, 401s with retries/logging
    5. Parse response -> return {"answer": str, "tokens_used": int}
    """
    pass