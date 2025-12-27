from abc import ABC, abstractmethod
from app.rules.context import UserContext
from app.rules.system import SystemContext
from app.rules.history import EventHistory
from app.rules.decision import EventDecision


class Rule(ABC):

    @abstractmethod
    def evaluate(
        self,
        user: UserContext,
        system: SystemContext,
        history: EventHistory
    ) -> EventDecision:
        pass
