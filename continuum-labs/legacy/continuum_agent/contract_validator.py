class ContractViolation(Exception):
    pass


def require(condition: bool, message: str):
    if not condition:
        raise ContractViolation(message)

