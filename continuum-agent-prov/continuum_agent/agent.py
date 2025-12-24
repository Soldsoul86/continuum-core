class Agent:
    """
    Continuum provenance agent.

    This agent:
    - records inputs and outputs
    - has no authority
    - performs no evaluation
    - performs no comparison
    """

    def __init__(self):
        pass

    def emit(self, event):
        return event

