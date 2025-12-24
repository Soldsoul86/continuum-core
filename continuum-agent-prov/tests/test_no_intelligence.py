import inspect
from continuum_agent import Agent


def test_agent_has_no_truth_resolution():
    src = inspect.getsource(Agent).lower()

    forbidden = [
        "truth",
        "resolve",
        "rank",
        "optimize",
        "best",
        "correct",
    ]

    for word in forbidden:
        assert word not in src, (
            f"Agent must not contain intelligence or truth resolution logic (found: {word})"
        )

