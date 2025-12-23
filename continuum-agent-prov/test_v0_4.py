from continuum_core.event_store import append_event, read_events
from emit_contradiction import emit_contradiction
from claim_view import build_claim_views

# Clean start
open("events.json", "w").write("[]")

append_event({
    "event_type": "claim",
    "claim_id": "claim-A",
    "content": "Tax rate is 18%",
    "authority": "Govt-2022",
    "timestamp": "2022-01-01T00:00:00Z"
})

append_event({
    "event_type": "claim",
    "claim_id": "claim-B",
    "content": "Tax rate is 20%",
    "authority": "Govt-2024",
    "timestamp": "2024-01-01T00:00:00Z"
})

edge = emit_contradiction(
    from_claim="claim-A",
    to_claim="claim-B",
    relation_type="supersedes",
    dimension="authority",
    scope={"jurisdiction": "India", "domain": "tax"}
)

append_event(edge)

events = read_events()

claims = {
    "claim-A": {"id": "claim-A"},
    "claim-B": {"id": "claim-B"},
}

views = build_claim_views(claims, events)

for cid, v in views.items():
    print(cid)
    print("incoming:", len(v["contradictions"]["incoming"]))
    print("outgoing:", len(v["contradictions"]["outgoing"]))
    print()
