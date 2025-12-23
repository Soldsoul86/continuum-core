from event_writer import emit_event

# Import core append function WITHOUT modifying core
from continuum_core.event_store import append_event

event = emit_event(
    actor="agent:prov-001",
    event_type="proposal",
    payload={
        "explanation": "Dry run proposal to test schema v2.0 ingestion",
        "note": "No intelligence involved"
    }
)

append_event(event)

print("Dry-run event ingested via continuum_core.")

