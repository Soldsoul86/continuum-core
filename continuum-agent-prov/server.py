import json
from pathlib import Path
from flask import Flask, jsonify, request
from claim_interpreter import ClaimInterpreter
from divergence.divergence_engine import DivergenceEngine

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
EVENTS_PATH = BASE_DIR / "events.json"


@app.after_request
def cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@app.route("/divergences", methods=["GET"])
def divergences():
    as_of = request.args.get("as_of")

    raw_events = json.loads(EVENTS_PATH.read_text())

    claims = ClaimInterpreter(raw_events).build_claims()

    engine = DivergenceEngine(claims)
    return jsonify(engine.compute(as_of_time=as_of))


@app.route("/", methods=["GET"])
def health():
    return "Continuum agent running", 200


if __name__ == "__main__":
    app.run(port=8000)

