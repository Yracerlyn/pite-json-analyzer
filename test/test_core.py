"""
Tests simples pour core.py
"""
from src.core import filter_records, analyze_records


def test_filter_records_basic(simple_records):
    """Test que filter_records filtre correctement les enregistrements 'ok'."""
    result = filter_records(simple_records, threshold=0, include_all=False)
    assert len(result) == 2
    assert all(record["status"] == "ok" for record in result)


def test_filter_records_with_threshold(simple_records):
    """Test que filter_records respecte le seuil de valeur."""
    result = filter_records(simple_records, threshold=15, include_all=False)
    assert len(result) == 1 
    assert result[0]["value"] >= 15


def test_analyze_records_basic():
    """Test qu'analyze_records calcule correctement count, sum et average."""
    records = [
        {"status": "ok", "value": 10},
        {"status": "ok", "value": 20}
    ]
    
    result = analyze_records(records)
    
    assert result.count == 2
    assert result.sum_value == 30
    assert result.average == 15.0


def test_analyze_records_empty():
    """Test qu'analyze_records gère les listes vides."""
    result = analyze_records([])
    
    assert result.count == 0
    assert result.sum_value == 0
    assert result.average == 0.0