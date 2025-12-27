from pydantic import BaseModel
from app.models.event import TimelineEventType
from typing import Dict, Any


class EventDecision(BaseModel):
    should_create: bool

    event_type: TimelineEventType | None = None

    trigger_reason: str | None = None

    metadata: Dict[str, Any] = {}
