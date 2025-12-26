import uuid
import datetime

SCHEMA_VERSION = "2.0"

def emit_event(actor: str, event_type: str, payload: dict) -> dict:
    return {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "actor": actor,
        "event_type": event_type,
        "payload": payload,
        "schema_version": SCHEMA_VERSION
    }

