import json
from pathlib import Path
from flask import Flask, jsonify, request
from divergence.divergence_engine import DivergenceEngine

app = Flask(__name__)

AGENT_DIR = Path(__file__).resolve().parent
EVENTS_PATH = AGENT_DIR / "events.json"


def load_claims_adapter():
    """
    TEMPORARY v0.6 ADAPTER
    Converts flat claim events into structured claims.
    """

    if not EVENTS_PATH.exists():
        raise RuntimeError(f"events.json not found at {EVENTS_PATH}")

    try:
        raw_events = json.loads(EVENTS_PATH.read_text())
    except Exception as e:
        raise RuntimeError(f"Invalid JSON in events.json: {e}")

    claims_by_key = {}

    for e in raw_events:
        if e.get("event_type") != "claim":
            continue

        if "content" not in e or " is " not in e["content"]:
            raise RuntimeError(f"Invalid claim content format: {e}")

        subject, value = e["content"].split(" is ", 1)

        key = (subject.strip(), "value", "current")

        if key not in claims_by_key:
            claims_by_key[key] = {
                "subject": subject.strip(),
                "predicate": "value",
                "object": "current",
                "assertions": []
            }

        claims_by_key[key]["assertions"].append({
            "asserted_by": e.get("authority"),
            "value": value.strip(),
            "asserted_at": e.get("timestamp")
        })

    return list(claims_by_key.values())


@app.route("/divergences")
def divergences():
    try:
        as_of = request.args.get("as_of")
        claims = load_claims_adapter()

        engine = DivergenceEngine(claims)
        result = engine.compute(as_of_time=as_of)

        return jsonify(result)

    except Exception as e:
        # PRINT FULL ERROR TO TERMINAL
        print("🔥 INTERNAL ERROR:", repr(e))
        raise


if __name__ == "__main__":
    app.run(port=8000, debug=True)

