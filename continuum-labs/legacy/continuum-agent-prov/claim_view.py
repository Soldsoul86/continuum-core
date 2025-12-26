# continuum-agent-prov/claim_view.py

from contradiction_index import build_contradiction_index

def build_claim_views(claims, events):
    index = build_contradiction_index(events)
    views = {}

    for cid, claim in claims.items():
        views[cid] = {
            "claim": claim,
            "contradictions": index.get(
                cid,
                {"incoming": [], "outgoing": []}
            )
        }

    return views
