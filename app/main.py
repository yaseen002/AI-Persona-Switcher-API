from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os

from app.models import ChatRequest, ChatResponse 
from app.personas import PERSONA_REGISTRY
from app.session_manager import get_history, add_message, get_or_create_session
from app.llm_service import generate_llm_response # <-- NEW IMPORT

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
    
    # 1. Validate Persona Exists
    if persona_id not in PERSONA_REGISTRY:
        raise HTTPException(status_code=404, detail=f"Persona '{persona_id}' not found.")
    
    persona_config = PERSONA_REGISTRY[persona_id]
    
    # 2. Handle Custom Persona Logic
    if persona_id == "custom":
        if not request.custom_prompt:
            raise HTTPException(status_code=400, detail="custom_prompt is required for the 'custom' persona.")
        system_prompt = request.custom_prompt
    else:
        system_prompt = persona_config["system_prompt"]

    # 3. Get or Create Session
    session_id = get_or_create_session(request.session_id, persona_id)
    
    # 4. Build the Messages Payload for the LLM
    # Get existing history
    raw_history = get_history(session_id)
    
    # CRITICAL: Strip out the 'timestamp' key, Mistral only wants 'role' and 'content'
    clean_history = [{"role": msg["role"], "content": msg["content"]} for msg in raw_history]
    
    # Construct final messages list: System Prompt + History + New User Message
    messages_to_send = [
        {"role": "system", "content": system_prompt}
    ] + clean_history + [
        {"role": "user", "content": request.message}
    ]

    # 5. Call the LLM Service
    ai_response_text = await generate_llm_response(
        messages=messages_to_send,
        temperature=persona_config["default_temperature"],
        max_tokens=MAX_TOKENS
    )

    # 6. Save to Session History
    add_message(session_id, role="user", content=request.message)
    add_message(session_id, role="assistant", content=ai_response_text)

    # 7. Return the Final Response
    return ChatResponse(
        response=ai_response_text,
        persona_used=persona_id,
        session_id=session_id
    )