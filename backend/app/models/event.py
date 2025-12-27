from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional, Dict, Any


class TimelineEventType(str, Enum):
    MORNING_GREETING = "morning_greeting"
    MIDDAY_CHECKIN = "midday_checkin"
    EVENING_WRAPUP = "evening_wrapup"
    INACTIVITY_NUDGE = "inactivity_nudge"
    SYSTEM_NOTE = "system_note"


class TimelineEvent(BaseModel):
    id: UUID = Field(default_factory=uuid4)

    user_id: UUID

    type: TimelineEventType

    content: str
    """
    AI-generated text shown to the user.
    """

    created_at: datetime = Field(default_factory=datetime.utcnow)
    scheduled_for: Optional[datetime] = None
    """
    When the event *should* have appeared.
    Useful for ordering and future push delivery.
    """

    read: bool = False

    trigger_reason: str
    """
    Human-readable explanation of why this event exists.
    Example: "morning window reached and no greeting sent today"
    """

    metadata: Dict[str, Any] = Field(default_factory=dict)
    """
    Optional structured context:
    - detected habits
    - energy level
    - summary references
    """





