from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any


@dataclass(frozen=True)
class HistoryEvent:
    """
    Immutable history event.

    Payload is opaque.
    Semantics are external.
    """
    event_id: str
    agent_id: str
    event_type: str
    occurred_at: datetime
    payload: Dict[str, Any]

