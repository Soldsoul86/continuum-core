from divergence.divergence_engine import DivergenceEngine


def test_divergence_detected_without_resolution():
    # Claim-view structure EXACTLY as expected by DivergenceEngine
    claim_view = [
        {
            "subject": "Tax rate",
            "predicate": "value",
            "object": "current",
            "assertions": [
                {
                    "authority": "Govt-2022",
                    "value": "18%",
                    "asserted_at": "2022-01-01T00:00:00Z",
                },
                {
                    "authority": "Govt-2024",
                    "value": "20%",
                    "asserted_at": "2024-01-01T00:00:00Z",
                },
            ],
        }
    ]

    engine = DivergenceEngine(claim_view)
    divergences = engine.compute()

    # Exactly one divergence must be detected
    assert len(divergences) == 1

    d = divergences[0]

    # Divergence must be explicit
    assert d["divergent"] is True

    # Both authorities must be preserved
    authorities = {a["authority"] for a in d["assertions"]}
    assert authorities == {"Govt-2022", "Govt-2024"}

    # No resolution, ranking, or truth allowed
    forbidden_keys = {"winner", "resolved", "truth", "preferred"}
    assert forbidden_keys.isdisjoint(d.keys())

