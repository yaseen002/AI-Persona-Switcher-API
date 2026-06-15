from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User message")
    temperature: Optional[float] = Field(
        default=None, 
        ge=0.0, le=2.0, 
        description="Override persona default temperature"
    )

class ChatResponse(BaseModel):
    session_id: str
    answer: str
    persona: str
    tokens_used: Optional[int] = None
    response_time_ms: Optional[float] = None

class SessionHistory(BaseModel):
    session_id: str
    persona: str
    messages: List[dict]
    created_at: datetime