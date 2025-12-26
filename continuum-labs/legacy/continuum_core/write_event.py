# continuum_core/write_event.py

from event_store import append_event
import sys
import time

event = {
    "timestamp": time.time(),
    "agent": "cli_writer",
    "payload": sys.argv[1:] or ["hello"]
}

append_event(event)
print("event written")


