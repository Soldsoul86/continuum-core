class OutcomeLinker:
    def __init__(self, claims):
        self.claims = claims

    def link_outcomes(self):
        linked = {}

        for claim_id, events in self.claims.items():
            assertions = []
            outcomes = []

            for e in events:
                role = e.get("role")
                if role == "assertion":
                    assertions.append(e)
                elif role == "outcome":
                    outcomes.append(e)

            linked[claim_id] = {
                "assertions": assertions,
                "outcomes": outcomes
            }

        return linked

