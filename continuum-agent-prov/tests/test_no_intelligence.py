import inspect
import prov_agent


def test_agent_has_no_truth_resolution():
    source = inspect.getsource(prov_agent)

    forbidden = [
        "resolve",
        "truth",
        "winner",
        "correct",
        "choose",
        "rank",
    ]

    for word in forbidden:
        assert word not in source.lower()

