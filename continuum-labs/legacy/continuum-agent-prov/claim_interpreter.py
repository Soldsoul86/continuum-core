from typing import List, Dict, Any
from collections import defaultdict


class ClaimInterpreter:
    """
    Canonical claim interpreter.

    Converts raw claim events into structured claims.
    This is the ONLY place where claim structure is defined.
    """

    def __init__(self, events: List[Dict[str, Any]]):
        self.events = events

    def build_claims(self) -> List[Dict[str, Any]]:
        claims = defaultdict(lambda: {
            "subject": None,
            "predicate": "value",
            "object": "current",
            "assertions": []
        })

        for e in self.events:
            if e.get("event_type") != "claim":
                continue

            content = e.get("content", "")
            if " is " not in content:
                continue

            subject, value = content.split(" is ", 1)
            key = subject.strip()

            claim = claims[key]
            claim["subject"] = key

            claim["assertions"].append({
                "authority": e.get("authority"),
                "value": value.strip(),
                "asserted_at": e.get("timestamp")
            })

        return list(claims.values())

