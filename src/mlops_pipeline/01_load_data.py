import json
from pathlib import Path
import pandas as pd

source = Path("data/raw/churn.csv")
if not source.exists():
    raise FileNotFoundError(f"Dataset not found: {source}")

df = pd.read_csv(source)
if df.empty:
    raise ValueError("The dataset is empty.")
if "Churn" not in df.columns:
    raise ValueError("Missing target column: Churn")

Path("artifacts").mkdir(exist_ok=True)
report = {
    "stage": "01 - Load Data",
    "status": "PASSED",
    "source": str(source),
    "rows": int(len(df)),
    "columns": int(len(df.columns)),
    "column_names": df.columns.tolist(),
    "missing_cells": int(df.isna().sum().sum())
}
Path("artifacts/data_load_report.json").write_text(
    json.dumps(report, indent=4), encoding="utf-8"
)
print(f"[SUCCESS] Loaded {len(df)} rows and {len(df.columns)} columns.")
print("[SUCCESS] Report: artifacts/data_load_report.json")
