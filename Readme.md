# PITE Project - JSON Data Analyzer

## 📋 Description

This project analyzes JSON files containing a list of records. It filters data based on status and a threshold value, then calculates statistics (count, sum, average).

## 🗂️ Project Structure

```
pite/
├── src/
│   ├── cli.py       # Command-line interface
│   ├── core.py      # Filtering and analysis logic
│   ├── io_.py       # JSON file reading/writing
│   └── config.py    # Default configuration
├── data/
│   └── sample.json  # Sample data file
├── test/
│   ├── conftest.py  # Test configuration
│   ├── test_core.py # Tests for core.py
│   └── test_cli.py  # Tests for cli.py
└── README.md
```

## ⚡ Installation and Usage

### 1. Install dependencies
```bash
pip install pytest
```

### 2. Run the application
```bash
# With default file
python src/cli.py

# With specific file
python src/cli.py --file data/sample2.json

# Include all statuses (not just "ok")
python src/cli.py --file data/sample.json --all

# With minimum value threshold
python src/cli.py --file data/sample.json --thres 20

# Combine options
python src/cli.py --file data/sample.json --all --thres 10
```

### 3. Run tests
```bash
# All tests
python -m pytest test/ -v

# Specific tests
python -m pytest test/test_core.py -v
python -m pytest test/test_cli.py -v
```

## 📝 JSON File Format

The file must be a **list** of objects at the root level:

```json
[
  {
    "status": "ok", 
    "value": 15
  },
  {
    "status": "bad", 
    "value": 20
  },
  {
    "status": "ok", 
    "value": "25.5"
  }
]
```

## 🔧 Command Line Options

- `--file FILE` : Specify the JSON file to analyze
- `--all` : Include all statuses (not just "ok")  
- `--thres NUMBER` : Set the minimum value threshold
- `--help` : Show help message

## 📊 Example Output

```
✅ Successfully loaded data from data/sample.json
Total raw records: 5
Records after filtering (threshold=0, mode='OK'): 3

--- Analysis Summary ---
[2025/10/16-15:30:45] ok_count=3 total_value=65.50 avg=21.83
```

## 🧪 Tests

The project includes 8 tests that verify:
- Record filtering functionality
- Statistics calculation  
- CLI configuration
- Application execution

All tests pass ✅