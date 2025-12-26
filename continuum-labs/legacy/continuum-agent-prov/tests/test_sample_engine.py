from continuum_agent.sample import SampleEngine

def test_sample_engine_accepts_valid_input():
    engine = SampleEngine(data=[])
    result = engine.compute()
    assert isinstance(result, list)
