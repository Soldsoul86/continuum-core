class Outcome:
    """
    An outcome records what happened later,
    according to a specific authority.

    It does NOT decide truth.
    It only records observation.
    """

    def __init__(
        self,
        outcome_id: str,
        claim_id: str,
        authority_id: str,
        result: str,        # observed | contradicted | unchanged
        observed_at: str,
        notes: str = ""
    ):
        self.outcome_id = outcome_id
        self.claim_id = claim_id
        self.authority_id = authority_id
        self.result = result
        self.observed_at = observed_at
        self.notes = notes

