from collections import defaultdict

class ClaimInterpreter:
    def __init__(self, events):
        self.events = events

    def build_claims(self):
        claims = defaultdict(list)

        for event in self.events:
            claim_id = event.get("claim_id")
            if claim_id:
                claims[claim_id].append(event)

        return dict(claims)

