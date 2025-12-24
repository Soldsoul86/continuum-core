from abc import ABC, abstractmethod
from typing import List
from orchestrator.history.event import HistoryEvent


class HistoryReader(ABC):
    """
    Read-only interface to history.

    Guarantees:
    - no mutation
    - ordered replay
    """

    @abstractmethod
    def read_all(self) -> List[HistoryEvent]:
        """
        Return full ordered history.
        """
        raise NotImplementedError

    @abstractmethod
    def read_since(self, *, since_event_id: str) -> List[HistoryEvent]:
        """
        Return history after a given event.
        """
        raise NotImplementedError

