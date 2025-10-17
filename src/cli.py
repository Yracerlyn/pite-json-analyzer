from __future__ import annotations
import sys
import argparse
import datetime as dt
import random
import os
from config import DEFAULT_CONFIG
from core import filter_records, analyze_records
from io_ import load_records

# --- Configuration & Defaults ---
# The config is now an explicit dictionary managed here, not a global that mutates widely.

def setup_config(argv: list[str] | None = None) -> dict:
    """
    Sets up the application configuration using default values and command-line arguments.
    """
    # Use argparse for robust and documented CLI
    parser = argparse.ArgumentParser(description="Analyze a list of JSON records.")
    parser.add_argument(
        "--file", 
        type=str, 
        default=DEFAULT_CONFIG["path"], 
        help=f"Path to the JSON file to analyze (default: {DEFAULT_CONFIG['path']})"
    )
    parser.add_argument(
        "--all", 
        action="store_true", 
        default=False, 
        help="Include records regardless of their 'status' (except unparseable ones)."
    )
    parser.add_argument(
        "--thres", 
        type=int, 
        default=DEFAULT_CONFIG["threshold"], 
        help=f"Minimum 'value' threshold for a record to be included (default: {DEFAULT_CONFIG['threshold']})"
    )

    args = parser.parse_args(argv)

    # Convert args to our unified config dictionary
    config = {
        "path": args.file,
        "encoding": DEFAULT_CONFIG["encoding"],
        "threshold": args.thres,
        "mode": "ALL" if args.all else "OK",
    }
        
    return config


def main(argv: list[str] | None = None) -> None:
    """
    Main application logic: config -> load -> filter -> analyze -> report.
    """
    # 1. Setup Configuration
    config = setup_config(argv)
    
    # 2. Load Data
    records_raw = load_records(config["path"], config["encoding"])
    
    # 3. Filter Records
    include_all = config["mode"] == "ALL"
    records_filtered = filter_records(
        records_raw, 
        threshold=config["threshold"], 
        include_all=include_all
    )
    print(f"Total raw records: {len(records_raw)}")
    print(f"Records after filtering (threshold={config['threshold']}, mode='{config['mode']}'): {len(records_filtered)}")

    # 4. Analyze
    # The random filter path logic is removed in favor of using the single, clean filter_records.
    # The "do_everything_and_nothing" function's side effects are entirely removed.
    # The sleep and mutable default arguments from "compute" are gone.
    analysis_result = analyze_records(records_filtered)
    
    # 5. Report Summary
    stamp = dt.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
    print("\n--- Analysis Summary ---")
    print(
        f"[{stamp}] "
        f"ok_count={analysis_result.count} "
        f"total_value={analysis_result.sum_value:.2f} "
        f"avg={analysis_result.average:.2f}"
    )


if __name__ == "__main__":
    # Ensure all initialization logic is contained within main()
    try:
        main(sys.argv[1:])
    except Exception as e:
        # A clean exit on unexpected errors
        print(f"\n An unrecoverable error occurred: {e}", file=sys.stderr)
        sys.exit(1)