from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from validate_data import validate_schema

def main():
    source = ROOT / "data" / "raw" / "churn.csv"
    report_dir = ROOT / "artifacts"
    report_dir.mkdir(exist_ok=True)

    if not source.exists():
        raise FileNotFoundError(f"Dataset not found: {source}")

    df = pd.read_csv(source)
    corrupted = df.copy()
    corrupted.loc[corrupted.index[0], "gender"] = "INVALID_GENDER"

    print("[INFO] Validating intentionally corrupted data...")
    valid = validate_schema(
        corrupted,
        output_report_name="corrupted_simulation_errors.csv"
    )

    result = {
        "test": "controlled_data_corruption",
        "corruption": "gender=INVALID_GENDER",
        "failure_detected": not valid,
        "original_dataset_modified": False
    }

    import json
    output = report_dir / "failure_simulation_report.json"
    output.write_text(json.dumps(result, indent=4), encoding="utf-8")

    if valid:
        print("[FAIL] Corrupted data was not detected.")
        sys.exit(1)

    print("[SUCCESS] Corrupted data detected.")
    print(f"[INFO] Report: {output}")

if __name__ == "__main__":
    main()
