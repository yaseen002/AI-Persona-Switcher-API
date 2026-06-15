import os
from dotenv import load_dotenv

load_dotenv()

# TODO: Add validation/fallbacks for missing keys
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_BASE_URL = os.getenv("LLM_API_BASE_URL", "https://api.mistral.ai/v1/chat/completions")
LLM_MODEL = os.getenv("LLM_MODEL", "mistral-small-latest")
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.3"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "512"))