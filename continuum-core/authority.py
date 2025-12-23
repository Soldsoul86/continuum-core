from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Authority:
    """
    Pure data object.
    Represents a declared source of legitimacy.
    No validation. No ranking. No logic.
    """
    authority_id: str          # stable identifier
    authority_type: str        # law | institution | llm | human | agent | unknown
    label: str                 # human-readable name
    parent: Optional[str] = None  # optional hierarchy

