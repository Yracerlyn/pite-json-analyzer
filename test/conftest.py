"""
Configuration simple pour les tests pytest.
"""
import pytest


@pytest.fixture
def simple_records():
    """Quelques enregistrements simples pour tester."""
    return [
        {"status": "ok", "value": 10},
        {"status": "bad", "value": 20},
        {"status": "ok", "value": "30"}
    ]