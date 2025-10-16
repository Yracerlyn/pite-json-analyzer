"""
Test configuration.
"""
import pytest


@pytest.fixture
def simple_records():
    """Sample records for testing."""
    return [
        {"status": "ok", "value": 10},
        {"status": "bad", "value": 20},
        {"status": "ok", "value": "30"}
    ]