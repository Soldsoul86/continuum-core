from dataclasses import dataclass
from typing import Optional, List

@dataclass(frozen=True)
class Authority:
    """
    Declared source of legitimacy.

    Structure only.
    No ranking.
    No validation.
    """
    authority_id: str
    authority_type: str
    label: str

    parent: Optional[str] = None
    valid_from: Optional[str] = None
    valid_to: Optional[str] = None

