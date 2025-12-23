import json
from pathlib import Path

class EventReader:
    def __init__(self, event_file: Path):
        self.event_file = event_file

    def read_events(self):
        with open(self.event_file, "r") as f:
            return json.load(f)

