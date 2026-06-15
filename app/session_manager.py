import uuid
from datetime import datetime, timedelta
from typing import Dict, List

# In-memory store (single-process, fine for learning)
SESSIONS: Dict[str, dict] = {}

def create_session(persona_name: str) -> str:
    """TODO: Generate session_id, init empty messages list, store in SESSIONS."""
    pass

def add_message(session_id: str, role: str, content: str) -> None:
    """TODO: Append {role, content} to session's messages. Raise KeyError if invalid."""
    pass

def get_history(session_id: str) -> List[dict]:
    """TODO: Return messages list for session_id. Raise KeyError if not found."""
    pass

def cleanup_old_sessions(max_age_hours: int = 1) -> None:
    """TODO: Remove sessions older than max_age_hours."""
    pass