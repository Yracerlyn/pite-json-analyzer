from __future__ import annotations
from typing import Any, NamedTuple

# Type alias for a single record
Record = dict[str, Any]

# Define the structure for the analysis result
class AnalysisResult(NamedTuple):
    count: int
    sum_value: float
    average: float


def _clean_and_get_value(record: Record) -> float | None:
    """
    Attempts to extract and convert the 'value' field to a float.
    Returns None if conversion fails.
    """
    raw_value = record.get("value", None)
    if raw_value is None:
        return 0.0

    # Ensure it's a string or numeric type
    if isinstance(raw_value, (int, float)):
        return float(raw_value)
    elif isinstance(raw_value, str):
        try:
            return float(raw_value)
        except ValueError:
            # Failed to convert string to float
            return None
    # Unhandled type
    return None


def _get_status(record: Record) -> str:
    """Extracts a normalized (lowercase) status from a record."""
    # Prioritize lowercase 'status', then uppercase 'STATUS', default to '??'
    status = record.get("status", record.get("STATUS", "??")).lower()
    return status


def filter_records(records: list[Record], threshold: int, include_all: bool) -> list[Record]:
    """
    Filters and cleans records based on status and value threshold.

    Filters are:
    1. Status is "ok", unless 'include_all' is True.
    2. Value is successfully converted to float.
    3. Value is greater than or equal to the 'threshold'.
    """
    filtered_records = []
    
    for record in records:
        value = _clean_and_get_value(record)
        status = _get_status(record)

        # 2. Check for successful value conversion
        if value is None:
            continue
        
        # 1. Check status (if not including all)
        is_ok = (status == "ok")
        if not (is_ok or include_all):
            continue

        # 3. Check threshold
        if value >= threshold:
            # We standardize the output record structure
            filtered_records.append({"status": status, "value": value})
            
    return filtered_records


def analyze_records(records: list[Record]) -> AnalysisResult:
    """
    Computes count, sum, and average of 'value' from a list of records.
    """
    # Use a list comprehension to safely extract and sum the float values
    values = [r["value"] for r in records if isinstance(r.get("value"), (int, float))]
    
    count = len(records)
    total_sum = sum(values)
    
    average = (total_sum / count) if count > 0 else 0.0
    
    return AnalysisResult(count=count, sum_value=total_sum, average=average)