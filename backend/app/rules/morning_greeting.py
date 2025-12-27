from datetime import time
import pytz

from app.rules.base import Rule
from app.rules.decision import EventDecision
from app.rules.context import UserContext
from app.rules.system import SystemContext
from app.rules.history import EventHistory
from app.models.event import TimelineEventType


class MorningGreetingRule(Rule):

    def evaluate(
        self,
        user: UserContext,
        system: SystemContext,
        history: EventHistory
    ) -> EventDecision:

        # 1. Wake window must exist
        if not user.wake_window_start or not user.wake_window_end:
            return EventDecision(should_create=False)

        # 2. Convert current time to user's timezone
        tz = pytz.timezone(user.timezone)
        now_local = system.now_utc.astimezone(tz)

        current_time = now_local.time()

        wake_start = time.fromisoformat(user.wake_window_start)
        wake_end = time.fromisoformat(user.wake_window_end)

        # 3. Check if current time is inside wake window
        if not (wake_start <= current_time <= wake_end):
            return EventDecision(should_create=False)

        # 4. Prevent duplicate greetings
        if TimelineEventType.MORNING_GREETING in history.events_sent_today:
            return EventDecision(should_create=False)

        # 5. All conditions met → request event creation
        return EventDecision(
            should_create=True,
            event_type=TimelineEventType.MORNING_GREETING,
            trigger_reason="Current time is within wake window and no morning greeting was sent today",
            metadata={
                "local_time": current_time.isoformat(),
                "wake_window": f"{user.wake_window_start}-{user.wake_window_end}"
            }
        )
