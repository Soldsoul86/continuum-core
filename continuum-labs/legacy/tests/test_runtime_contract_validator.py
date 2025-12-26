import pytest
from continuum_agent.sample import SampleEngine
from continuum_agent.contract_validator import ContractViolation


def test_runtime_contract_violation_is_raised():
    with pytest.raises(ContractViolation):
        SampleEngine(data=None)

