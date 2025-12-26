import pytest
from continuum_agent.sample import SampleEngine

def test_sample_engine_rejects_invalid_input():
    with pytest.raises(ValueError):
        SampleEngine(data=None)
