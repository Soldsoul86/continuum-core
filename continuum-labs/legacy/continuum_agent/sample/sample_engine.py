from continuum_agent.contract_validator import require


class SampleEngine:
    """
    Continuum engine.

    Derived-only.
    No authority.
    No resolution.
    """

    def __init__(self, data):
        require(data is not None, "data must not be None")
        require(isinstance(data, list), "data must be a list")
        self.data = data

    def compute(self):
        return []

