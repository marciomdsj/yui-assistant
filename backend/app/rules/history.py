from typing import Set
from app.models.event import TimelineEventType
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Dict, Any, Optional, List


class EventHistory(BaseModel):
    """
    Minimal event knowledge needed by rules.
    """
    events_sent_today: Set[TimelineEventType] = set()
    last_event_at: Optional[datetime] = None
