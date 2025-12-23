# continuum_core/event_store.py

import json
from pathlib import Path
from datetime import datetime

EVENTS_FILE = Path("events.json")

ALLOWED_EVENT_TYPES = {
    "claim",
    "outcome",
    "contradiction_edge",
}

def append_event(event: dict):
    if event.get("event_type") not in ALLOWED_EVENT_TYPES:
        raise ValueError("Unknown event_type")

    event["stored_at"] = datetime.utcnow().isoformat()

    if EVENTS_FILE.exists():
        events = json.loads(EVENTS_FILE.read_text())
    else:
        events = []

    events.append(event)
    EVENTS_FILE.write_text(json.dumps(events, indent=2))


def read_events():
    if not EVENTS_FILE.exists():
        return []
    return json.loads(EVENTS_FILE.read_text())
