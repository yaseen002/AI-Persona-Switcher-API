from fastapi import FastAPI, HTTPException
from app.models import ChatRequest, ChatResponse, SessionHistory
from app.personas import PERSONA_REGISTRY, get_persona_config
from app.session_manager import create_session, add_message, get_history
from app.llm_client import call_llm
from app.config import DEFAULT_TEMPERATURE

app = FastAPI(title="AI Persona Switcher", version="1.0.0")

@app.get("/personas")
def list_personas():
    """TODO: Return list of available personas + descriptions."""
    pass

@app.post("/chat/{persona_name}", response_model=ChatResponse)
def chat(persona_name: str, req: ChatRequest):
    """TODO:
    1. Validate persona
    2. Get/create session_id
    3. Build messages array (system + history + new user message)
    4. Call LLM
    5. Save response to session
    6. Return ChatResponse
    """
    pass

@app.post("/chat/custom", response_model=ChatResponse)
def chat_custom(req: ChatRequest, system_prompt: str = None):
    """TODO: Same as /chat/{persona} but use provided system_prompt."""
    pass

@app.get("/history/{session_id}", response_model=SessionHistory)
def get_session_history(session_id: str):
    """TODO: Return session history. 404 if not found."""
    pass