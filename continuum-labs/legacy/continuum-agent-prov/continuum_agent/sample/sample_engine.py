class SampleEngine:
    """
    Continuum engine.

    Derived-only.
    No authority.
    No resolution.
    """

    def __init__(self, data):
        if data is None:
            raise ValueError("data must not be None")
        self.data = data

    def compute(self):
        return []
