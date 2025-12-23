from typing import List, Dict, Any, Optional

class Claim:
    """
    A claim is a semantic statement.
    It may receive multiple assertions from different authorities over time.
    Continuum does not evaluate or reconcile them.
    """

    def __init__(
        self,
        claim_id: str,
        subject: str,
        predicate: str,
        object: str,
        assertions: Optional[List[Dict[str, Any]]] = None,
    ):
        self.claim_id = claim_id
        self.subject = subject
        self.predicate = predicate
        self.object = object

        # Passive, append-only metadata
        self.assertions = assertions or []

    def add_assertion(self, assertion: Dict[str, Any]):
        """
        Append-only.
        No validation, no authority checks, no truth evaluation.
        """
        self.assertions.append(assertion)

