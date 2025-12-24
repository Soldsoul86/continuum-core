from claim_interpreter import ClaimInterpreter


def test_claim_interpreter_schema_is_stable():
    events = [
        {
            "event_type": "claim",
            "authority": "Authority-A",
            "timestamp": "2022-01-01T00:00:00Z",
            "content": "Tax rate is 18%"
        }
    ]

    claims = ClaimInterpreter(events).build_claims()

    assert len(claims) == 1

    claim = claims[0]

    assert claim["subject"] == "Tax rate"
    assert claim["predicate"] == "value"
    assert claim["object"] == "current"
    assert isinstance(claim["assertions"], list)

    assertion = claim["assertions"][0]

    # Canonical v0.7 assertion schema
    assert set(assertion.keys()) == {
        "authority",
        "value",
        "asserted_at"
    }

