from pydantic import BaseModel, Field
from typing import Optional
import uuid

class ChatRequest(BaseModel):
    message: str = Field(
        ..., 
        description="The user message to the AI persona", 
        min_length=1  
    )

    session_id: Optional[str] = Field(
        default_factory=lambda: str(uuid.uuid4()),  
        description="Unique identifier for the conversation session"
    ) 

    custom_prompt: Optional[str] = Field(  
        default=None,
        description="A custom system prompt if the user wants to define their own persona"
    )

class ChatResponse(BaseModel):
    response: str = Field(..., description="The AI's generated Response")
    persona_used: str = Field(..., description="The name of the persona that answered (e.g., 'legal-assistant')") 
    session_id: str = Field(..., description="The active session ID for tracking history") 