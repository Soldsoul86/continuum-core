import json
import time
from pathlib import Path

EVENTS_FILE = Path("events.json")
EVALUATOR_ACTOR = "system:outcome-engine"


def load_events():
    if not EVENTS_FILE.exists():
        return []
    with open(EVENTS_FILE, "r") as f:
        return json.load(f)


def append_event(event):
    events = load_events()
    events.append(event)
    with open(EVENTS_FILE, "w") as f:
        json.dump(events, f, indent=2)


def evaluate_outcomes():
    """
    v0.3-compatible outcome evaluator.
    Operates on claim_id, not payload / proposal IDs.
    """

    events = load_events()

    assertions_by_claim = {}
    outcomes_by_claim = set()

    for e in events:
        claim_id = e.get("claim_id")
        role = e.get("role")

        if not claim_id:
            continue

        if role == "assertion":
            assertions_by_claim[claim_id] = e

        elif role == "outcome":
            outcomes_by_claim.add(claim_id)

    # Emit outcome only for claims that do not yet have one
    for claim_id, assertion in assertions_by_claim.items():
        if claim_id in outcomes_by_claim:
            continue

        outcome_event = {
            "event_type": "outcome",
            "actor": EVALUATOR_ACTOR,
            "claim_id": claim_id,
            "role": "outcome",
            "content": "Outcome evaluation pending",
            "timestamp": time.time()
        }

        append_event(outcome_event)

    print("Outcome evaluation complete.")


if __name__ == "__main__":
    evaluate_outcomes()

