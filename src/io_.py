from __future__ import annotations
from pathlib import Path
import json
from typing import Any

# Type alias for a single record (a dictionary)
Record = dict[str, Any]

# Backup data used if file loading fails
BACKUP_DATA: list[Record] = [
    {"status": "ok", "value": "3"},
    {"status": "bad", "value": "x"},
    {"status": "ok", "value": 7}
]


def load_records(path: str | Path, encoding: str = "utf-8") -> list[Record]:
    """
    Load a list of JSON records from *path*.

    Handles file I/O and validation of the top-level type.
    Returns BACKUP_DATA and prints a warning on failure.
    """
    try:
        data = json.loads(Path(path).read_text(encoding=encoding))
        if not isinstance(data, list):
            raise ValueError("Expected a JSON list of records (top-level type must be a list)")
        print(f"Successfully loaded data from {path}")
        return data
    except Exception as e:
        # A controlled way to handle I/O failure
        print(f"Could not read file at '{path}'. Error: {e}. Using backup data.")
        return BACKUP_DATA