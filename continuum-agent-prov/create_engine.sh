#!/usr/bin/env bash
set -e

ENGINE_NAME="$1"

if [ -z "$ENGINE_NAME" ]; then
  echo "Usage: ./create_engine.sh <engine_name>"
  exit 1
fi

ENGINE_DIR="continuum_agent/$ENGINE_NAME"
TEST_DIR="tests"

ENGINE_CLASS="$(tr '[:lower:]' '[:upper:]' <<< ${ENGINE_NAME:0:1})${ENGINE_NAME:1}Engine"

if [ -d "$ENGINE_DIR" ]; then
  echo "Engine already exists: $ENGINE_DIR"
  exit 1
fi

echo "Creating engine: $ENGINE_NAME"

mkdir -p "$ENGINE_DIR"

# __init__.py
cat > "$ENGINE_DIR/__init__.py" <<EOF
from .${ENGINE_NAME}_engine import $ENGINE_CLASS
EOF

# engine file
cat > "$ENGINE_DIR/${ENGINE_NAME}_engine.py" <<EOF
class $ENGINE_CLASS:
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
EOF

# CONTRACT.md
cat > "$ENGINE_DIR/CONTRACT.md" <<EOF
# ${ENGINE_CLASS} — Contract

## Input
Explicit, documented structure only.

## Forbidden
- Raw events
- Implicit guessing
- Partial structures

## Behavior
- Read-only
- Derived-only
- No resolution
- No ranking

Contract change requires version bump.
EOF

# Positive test
cat > "$TEST_DIR/test_${ENGINE_NAME}_engine.py" <<EOF
from continuum_agent.${ENGINE_NAME} import $ENGINE_CLASS

def test_${ENGINE_NAME}_engine_accepts_valid_input():
    engine = $ENGINE_CLASS(data=[])
    result = engine.compute()
    assert isinstance(result, list)
EOF

# Negative test
cat > "$TEST_DIR/test_${ENGINE_NAME}_contract.py" <<EOF
import pytest
from continuum_agent.${ENGINE_NAME} import $ENGINE_CLASS

def test_${ENGINE_NAME}_engine_rejects_invalid_input():
    with pytest.raises(ValueError):
        $ENGINE_CLASS(data=None)
EOF

echo "Engine ${ENGINE_NAME} created successfully."

