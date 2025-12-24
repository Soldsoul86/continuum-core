from divergence.divergence_engine import DivergenceEngine


def test_no_ranking_scoring_or_truth_fields():
    claims = [
        {
            "subject": "Policy",
            "predicate": "value",
            "object": "current",
            "assertions": [
                {
                    "authority": "A",
                    "value": "yes",
                    "asserted_at": "2020-01-01T00:00:00Z"
                },
                {
                    "authority": "B",
                    "value": "no",
                    "asserted_at": "2021-01-01T00:00:00Z"
                }
            ]
        }
    ]

    engine = DivergenceEngine(claims)
    result = engine.compute()[0]

    forbidden_keys = {
        "rank",
        "score",
        "confidence",
        "winner",
        "truth",
        "probability"
    }

    assert forbidden_keys.isdisjoint(result.keys())

