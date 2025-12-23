import os
from datetime import datetime
from continuum_core.event_store import read_events, append_event
from event_writer import emit_event

# Ensure all reads/writes happen relative to project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
os.chdir(PROJECT_ROOT)

ACTOR = "agent:prov-001"


def evaluate_outcomes():
    events = read_events()

    # Collect all proposal events
    proposals = [
        e for e in events
        if e.get("event_type") == "proposal"
    ]

    # Collect proposal IDs that already have outcomes
    evaluated_proposals = {
        e["payload"].get("proposal_event_id")
        for e in events
        if e.get("event_type") == "outcome"
    }

    for proposal in proposals:
        proposal_id = proposal["event_id"]

        # Idempotency: never evaluate the same proposal twice
        if proposal_id in evaluated_proposals:
            continue

        # Deterministic v0.2 rule:
        # Any proposal without an outcome is marked successful
        outcome_event = emit_event(
            actor=ACTOR,
            event_type="outcome",
            payload={
                "proposal_event_id": proposal_id,
                "status": "success",
                "reason": "deterministic v0.2 outcome rule",
                "observed_at": datetime.utcnow().isoformat() + "Z"
            }
        )

        append_event(outcome_event)


if __name__ == "__main__":
    evaluate_outcomes()
    print("Outcome evaluation complete.")

