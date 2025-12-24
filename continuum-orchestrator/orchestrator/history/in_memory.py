from typing import List
from orchestrator.history.reader import HistoryReader
from orchestrator.history.writer import HistoryWriter
from orchestrator.history.event import HistoryEvent


class InMemoryHistory(HistoryReader, HistoryWriter):
    """
    Deterministic in-memory history.
    """

    def __init__(self):
        self._events: List[HistoryEvent] = []

    def append(self, event: HistoryEvent) -> None:
        self._events.append(event)

    def read_all(self) -> List[HistoryEvent]:
        return list(self._events)

    def read_since(self, *, since_event_id: str) -> List[HistoryEvent]:
        found = False
        result = []

        for e in self._events:
            if found:
                result.append(e)
            if e.event_id == since_event_id:
                found = True

        return result

