from divergence.divergence_engine import DivergenceEngine


def test_time_lens_filters_future_assertions():
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

    # As of 2023 → only one assertion exists → no divergence
    result = engine.compute(as_of_time="2023-01-01")

    assert result == []

