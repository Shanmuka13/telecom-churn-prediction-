from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from validate_data import validate_schema

DATA_FILE = ROOT / "data" / "raw" / "churn.csv"


def test_churn_dataset_exists_and_has_expected_columns():
    assert DATA_FILE.exists(), "Raw churn dataset is missing"

    df = pd.read_csv(DATA_FILE)

    assert not df.empty
    assert "customerID" in df.columns
    assert "gender" in df.columns
    assert "Churn" in df.columns


def test_clean_dataset_passes_schema_validation():
    df = pd.read_csv(DATA_FILE)

    assert validate_schema(
        df,
        output_report_name="pytest_clean_validation.csv"
    ) is True


def test_invalid_gender_fails_schema_validation():
    df = pd.read_csv(DATA_FILE)
    df.loc[df.index[0], "gender"] = "INVALID_GENDER"

    (ROOT / "artifacts").mkdir(exist_ok=True)

    assert validate_schema(
        df,
        output_report_name="pytest_corrupted_validation.csv"
    ) is False
