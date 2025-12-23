# continuum-agent-prov/contradiction_index.py

from collections import defaultdict

def build_contradiction_index(events):
    index = defaultdict(lambda: {"incoming": [], "outgoing": []})

    for e in events:
        if e.get("event_type") != "contradiction_edge":
            continue

        index[e["from_claim"]]["outgoing"].append(e)
        index[e["to_claim"]]["incoming"].append(e)

    return dict(index)
