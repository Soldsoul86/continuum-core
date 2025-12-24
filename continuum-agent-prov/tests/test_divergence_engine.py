from divergence.divergence_engine import DivergenceEngine


def test_divergence_detected_when_values_differ():
    claims = [
        {
            "subject": "Tax rate",
            "predicate": "value",
            "object": "current",
            "assertions": [
                {
                    "authority": "Govt-2022",
                    "value": "18%",
                    "asserted_at": "2022-01-01T00:00:00Z"
                },
                {
                    "authority": "Govt-2024",
                    "value": "20%",
                    "asserted_at": "2024-01-01T00:00:00Z"
                }
            ]
        }
    ]

    engine = DivergenceEngine(claims)
    result = engine.compute()

    assert len(result) == 1
    assert result[0]["divergent"] is True
    assert len(result[0]["assertions"]) == 2

