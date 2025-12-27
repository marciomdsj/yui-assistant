from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Dict, Any, Optional, List


class UserContext(BaseModel):
    user_id: UUID
    timezone: str

    wake_window_start: Optional[str] = None  # "07:00"
    wake_window_end: Optional[str] = None    # "09:00"

    quiet_hours_start: Optional[str] = None
    quiet_hours_end: Optional[str] = None

    preferences: Dict[str, Any] = {}
