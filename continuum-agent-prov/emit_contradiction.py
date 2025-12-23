# continuum-agent-prov/emit_contradiction.py

from datetime import datetime
import uuid

def emit_contradiction(
    from_claim,
    to_claim,
    relation_type,
    dimension,
    scope,
    agent_id="agent-prov",
):
    return {
        "event_type": "contradiction_edge",
        "edge_id": f"contr-{uuid.uuid4().hex[:8]}",
        "from_claim": from_claim,
        "to_claim": to_claim,
        "relation_type": relation_type,
        "dimension": dimension,
        "scope": scope,
        "introduced_by": agent_id,
        "timestamp": datetime.utcnow().isoformat(),
    }
