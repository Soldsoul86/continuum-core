from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass(frozen=True)
class ExecutionContext:
    orchestration_id: str
    execution_id: str
    triggered_at: datetime
    reason: str  # "time_tick" or "event_presence"

    @staticmethod
    def create(reason: str):
        return ExecutionContext(
            orchestration_id=str(uuid.uuid4()),
            execution_id=str(uuid.uuid4()),
            triggered_at=datetime.utcnow(),
            reason=reason,
        )

