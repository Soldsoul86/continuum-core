from collections import defaultdict
from typing import Dict, Any


class AuthorityIndex:
    """
    Agent-side derived index.

    Computes credibility signals from historical
    claims and outcomes.

    IMPORTANT:
    - Not truth
    - Not written to core
    - Fully rebuildable
    """

    def __init__(self):
        self.stats: Dict[str, Dict[str, int]] = defaultdict(
            lambda: {
                "assertions": 0,
                "observed": 0,
                "contradicted": 0,
            }
        )

    def ingest_claim(self, claim: Any):
        for assertion in getattr(claim, "assertions", []):
            authority_id = assertion.get("asserted_by")
            if authority_id:
                self.stats[authority_id]["assertions"] += 1

    def ingest_outcome(self, outcome: Any):
        authority_id = outcome.authority_id
        result = outcome.result

        if result == "observed":
            self.stats[authority_id]["observed"] += 1
        elif result == "contradicted":
            self.stats[authority_id]["contradicted"] += 1

    def credibility_view(self) -> Dict[str, Dict[str, float]]:
        view = {}

        for authority_id, s in self.stats.items():
            total = s["observed"] + s["contradicted"]

            score = (
                s["observed"] / total
                if total > 0
                else None
            )

            view[authority_id] = {
                "assertions": s["assertions"],
                "observed": s["observed"],
                "contradicted": s["contradicted"],
                "credibility_score": score,
            }

        return view

