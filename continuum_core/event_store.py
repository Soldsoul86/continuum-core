import json
import os

EVENTS_FILE = "events.json"

def read_events():
    if not os.path.exists(EVENTS_FILE):
        return []

    with open(EVENTS_FILE, "r") as f:
        return json.load(f)

def append_event(event):
    events = read_events()
    events.append(event)

    with open(EVENTS_FILE, "w") as f:
        json.dump(events, f, indent=2)

