import json
import time
import uuid
from pathlib import Path

EVENTS_FILE = Path("events.json")
ACTOR_ID = "agent:prov-001"


def new_claim_id(prefix="claim"):
    """
    Generate a forward-only, agent-owned claim ID.
    Not authoritative. Not global. Not retroactive.
    """
    return f"{prefix}-{uuid.uuid4().hex[:12]}"


def emit_event(event: dict):
    """
    Append an event to the immutable events log.
    """
    if EVENTS_FILE.exists():
        with open(EVENTS_FILE, "r") as f:
            events = json.load(f)
    else:
        events = []

    events.append(event)

    with open(EVENTS_FILE, "w") as f:
        json.dump(events, f, indent=2)


def run_agent():
    """
    Single execution of the agent producing one claim.
    """

    # --- agent produces some output ---
    response_text = "This is a test assertion produced by prov agent."

    # --- claim emission ---
    claim_id = new_claim_id("claim-prov")

    assertion_event = {
        "event_type": "assertion",
        "actor": ACTOR_ID,
        "claim_id": claim_id,
        "role": "assertion",
        "content": response_text,
        "timestamp": time.time()
    }

    emit_event(assertion_event)

    # --- optional outcome (example) ---
    outcome_event = {
        "event_type": "outcome",
        "actor": "system:evaluator",
        "claim_id": claim_id,
        "role": "outcome",
        "content": "No outcome observed yet",
        "timestamp": time.time()
    }

    emit_event(outcome_event)


if __name__ == "__main__":
    run_agent()

