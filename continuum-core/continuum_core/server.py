# continuum_core/server.py
# CONTINUUM CORE SERVER — v0.4
# READ-ONLY, PASSIVE, APPEND-ONLY

from flask import Flask, jsonify
from continuum_core.event_store import read_events
from collections import defaultdict

app = Flask(__name__)


def build_claims(events):
    claims = {}
    for e in events:
        if e.get("event_type") == "claim":
            claims[e["claim_id"]] = e
    return claims


def build_topology(events):
    incoming = defaultdict(list)
    outgoing = defaultdict(list)

    for e in events:
        if e.get("event_type") != "contradiction_edge":
            continue

        outgoing[e["from_claim"]].append(e)
        incoming[e["to_claim"]].append(e)

    return incoming, outgoing


@app.route("/claims", methods=["GET"])
def get_claims():
    events = read_events()
    claims = build_claims(events)
    return jsonify(list(claims.values()))


@app.route("/claim/<claim_id>/topology", methods=["GET"])
def get_claim_topology(claim_id):
    events = read_events()
    incoming, outgoing = build_topology(events)

    return jsonify({
        "claim_id": claim_id,
        "incoming_contradictions": incoming.get(claim_id, []),
        "outgoing_contradictions": outgoing.get(claim_id, []),
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
