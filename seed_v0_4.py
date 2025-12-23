from continuum_core.event_store import append_event

# Claim A
append_event({
    "event_type": "claim",
    "claim_id": "claim-A",
    "content": "Tax rate is 18%",
    "authority": "Govt-2022",
    "timestamp": "2022-01-01T00:00:00Z"
})

# Claim B
append_event({
    "event_type": "claim",
    "claim_id": "claim-B",
    "content": "Tax rate is 20%",
    "authority": "Govt-2024",
    "timestamp": "2024-01-01T00:00:00Z"
})

# Contradiction (supersession)
append_event({
    "event_type": "contradiction_edge",
    "edge_id": "contr-001",
    "from_claim": "claim-A",
    "to_claim": "claim-B",
    "relation_type": "supersedes",
    "dimension": "authority",
    "scope": {"jurisdiction": "India", "domain": "tax"},
    "introduced_by": "seed",
    "timestamp": "2024-01-01T00:00:00Z"
})

print("Seeded v0.4 data")
