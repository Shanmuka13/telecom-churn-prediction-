import json
import os
import sys

import pandas as pd

from pathlib import Path

sys.path.insert(0, "src")
from validate_data import validate_schema

def main():
    print("[INFO] Stage 10: Controlled Failure Injection")

    source = Path("data/raw/churn.csv")
    if not source.exists():
        raise FileNotFoundError(f"Dataset not found: {source}")

    clean = pd.read_csv(source)
    corrupted = clean.copy()
    corrupted.loc[0, "gender"] = "INVALID_GENDER"

    os.makedirs("artifacts", exist_ok=True)
    errors_path = "artifacts/corrupted_simulation_errors.csv"

    detected = not validate_schema(
        corrupted,
        output_report_name="corrupted_simulation_errors.csv"
    )

    result = {
        "stage": "10 - Failure Injection",
        "injected_fault": "Invalid gender value",
        "fault_detected": detected,
        "original_dataset_modified": False,
        "status": "PASSED" if detected else "FAILED",
    }

    with open(
        "artifacts/failure_simulation_report.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(result, f, indent=4)

    print(f"[INFO] Error details: {errors_path}")
    print("[SUCCESS] Invalid data was detected." if detected
          else "[ERROR] Invalid data was not detected.")

    return detected

if __name__ == "__main__":
    try:
        sys.exit(0 if main() else 1)
    except Exception as exc:
        print(f"[ERROR] Failure injection failed: {exc}")
        sys.exit(1)
