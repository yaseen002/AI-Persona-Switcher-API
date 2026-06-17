import uuid
from datetime import datetime, timedelta
from typing import Dict, List

SESSIONS: Dict[str, dict] = {}

def create_session(persona_name: str) -> str:
    session_id = str(uuid.uuid4())
    SESSIONS[session_id] = {
        "persona_name": persona_name,
        "messages": [],
        "created_at": datetime.now()
    }
    return session_id

def add_message(session_id: str, role: str, content: str) -> None:
    if session_id not in SESSIONS:
        raise KeyError(f"Session {session_id} not found")
    
    SESSIONS[session_id]["messages"].append({
        "role": role,
        "content": content,
        "timestamp": datetime.now().isoformat()
    })


def get_history(session_id: str) -> List[dict]:
    """Return messages list for session_id. Raise KeyError if not found."""
    
    if session_id not in SESSIONS:
        raise KeyError(f"Session {session_id} not found")
    
    # Simply return the list of messages stored under this session_id
    return SESSIONS[session_id]["messages"]

def cleanup_old_sessions(max_age_hours: int = 1) -> None:
    """Remove sessions older than max_age_hours."""
    now = datetime.now()
    
    for session_id in list(SESSIONS.keys()):
        session_data = SESSIONS[session_id]
        age = now - session_data["created_at"]
        
        if age > timedelta(hours=max_age_hours):
            del SESSIONS[session_id] # Remove the expired session