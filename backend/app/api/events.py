from fastapi import APIRouter
from typing import List
from app.models.event import TimelineEvent

router = APIRouter(prefix="/events", tags=["events"])

@router.get("/", response_model=List[TimelineEvent])
def list_events():
    """
    TEMPORARY: returns mock events.
    Will be backed by DB next.
    """
    return []
