from typing import List, Dict, Any
from datetime import datetime


class DivergenceEngine:
    """
    Derived-only divergence detection.

    - No ranking
    - No resolution
    - No write-back
    - No authority privilege
    """

    def __init__(self, claims: List[Dict[str, Any]]):
        self.claims = claims

    def compute(self, as_of_time: str = None) -> List[Dict[str, Any]]:
        cutoff = None
        if as_of_time:
            cutoff = datetime.fromisoformat(as_of_time)

        results = []

        for claim in self.claims:
            active_assertions = []

            for a in claim.get("assertions", []):
                ts = datetime.fromisoformat(
                    a["asserted_at"].replace("Z", "")
                )

                if cutoff and ts > cutoff:
                    continue

                active_assertions.append({
                    "authority": a["authority"],
                    "value": a["value"],
                    "asserted_at": a["asserted_at"]
                })

            values = set(a["value"] for a in active_assertions)

            if len(values) > 1:
                results.append({
                    "subject": claim["subject"],
                    "predicate": claim["predicate"],
                    "object": claim["object"],
                    "divergent": True,
                    "assertions": active_assertions
                })

        return results

