from collections import defaultdict
from typing import List, Dict, Any, Optional


class DivergenceEngine:
    """
    Derived-only detector of structural disagreement.
    No truth, no ranking, no scoring.
    """

    def __init__(self, claims: List[Dict[str, Any]]):
        self.claims = claims

    def compute(self, as_of_time: Optional[str] = None) -> List[Dict[str, Any]]:
        grouped = defaultdict(list)

        for claim in self.claims:
            s = claim["subject"]
            p = claim["predicate"]
            o = claim["object"]

            for a in claim["assertions"]:
                if as_of_time and a["asserted_at"] > as_of_time:
                    continue

                grouped[(s, p, o)].append({
                    "authority": a["asserted_by"],
                    "value": a["value"],
                    "asserted_at": a["asserted_at"]
                })

        divergences = []

        for (s, p, o), assertions in grouped.items():
            values = set(x["value"] for x in assertions)

            if len(values) > 1:
                divergences.append({
                    "subject": s,
                    "predicate": p,
                    "object": o,
                    "divergent": True,
                    "assertions": assertions
                })

        return divergences

