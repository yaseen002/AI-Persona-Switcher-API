from fastapi import FastAPI
from dotenv import load_dotenv
import os

from app.models import ChatRequest, ChatResponse 
from app.personas import PERSONAS

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_API_BASE_URL")
MODEL_NAME = os.getenv("LLM_MODEL")             # Fixed: was 'MODEl_NAME'
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", 0.3)) # Fixed: was 'TEMPERATURE', added float() and default
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 512))  # Fixed: was 'MAX_TOKENTS', added int() and default

app = FastAPI(title="AI Persona Switcher API")

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/health-check')
def health_check():
    return {"Status": "healthy"}

@app.get('/personas')
def personas_list():
    return {"Total Personas": len(PERSONAS)}

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