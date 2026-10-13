import sys
sys.path.insert(0, "src")
import pandas as pd
from validate_data import validate_schema

df = pd.read_csv("data/raw/churn.csv")
if not validate_schema(df, output_report_name="baseline_validation.csv"):
    sys.exit(1)

print("[SUCCESS] Stage 02: Data validation passed.")
