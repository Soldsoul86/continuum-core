from abc import ABC, abstractmethod
from orchestrator.history.event import HistoryEvent


class HistoryWriter(ABC):
    """
    Append-only history writer.

    Guarantees:
    - no overwrite
    - no deletion
    """

    @abstractmethod
    def append(self, event: HistoryEvent) -> None:
        """
        Append event to history.
        """
        raise NotImplementedError

