from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os

# Ensure these import paths match your actual folder structure
from app.models import ChatRequest, ChatResponse 
from app.personas import PERSONA_REGISTRY
from app.session_manager import get_history

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_API_BASE_URL")
MODEL_NAME = os.getenv("LLM_MODEL")
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", 0.3))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 512))

app = FastAPI(title="AI Persona Switcher API")

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/health-check')
def health_check():
    return {"Status": "healthy"}

@app.get('/personas')
def get_personas():
    """
    Returns a list of available personas.
    SECURITY: Notice we do NOT return the 'system_prompt'. 
    We only expose safe, public-facing metadata.
    """
    personas_list = []
    for persona_id, persona_data in PERSONA_REGISTRY.items():
        personas_list.append({
            "id": persona_id,
            "name": persona_data["display_name"],
            "temperature": persona_data["default_temperature"]
        })
    
    return {"personas": personas_list}

@app.get('/history/{session_id}')
def get_session_history(session_id: str):
    """
    Retrieves the conversation history for a given session ID.
    Reference: https://fastapi.tiangolo.com/tutorial/handling-errors/#use-httpexception
    """
    try:
        history = get_history(session_id)
        return {"session_id": session_id, "history": history}
    except KeyError:        
        raise HTTPException(status_code=404, detail="Session not found")

@app.post("/chat/{persona_id}", response_model=ChatResponse)
async def chat_with_persona(persona_id: str, request: ChatRequest):
    """
    Dummy endpoint to verify that FastAPI correctly validates 
    the incoming ChatRequest and formats the outgoing ChatResponse.
    """

    return ChatResponse(
        response=f"This is a dummy response for persona: {persona_id}. Your message was: '{request.message}'",
        persona_used=persona_id,
        session_id=request.session_id
    )