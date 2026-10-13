import json
import os
import sys

import mlflow
import numpy as np
from mlflow.tracking import MlflowClient

MODEL_NAME = "Telco_Churn_Production_Model"

def main():
    print("[INFO] Starting Lab 9: Production Model Smoke Test")

    report_path = "artifacts/deployment_readiness_report.json"
    if not os.path.exists(report_path):
        print("[ERROR] Lab 8 report is missing.")
        return False

    with open(report_path, "r", encoding="utf-8-sig") as f:
        report = json.load(f)

    if not report.get("deployment_ready", False):
        print("[ERROR] Model did not pass deployment-readiness checks.")
        return False

    client = MlflowClient()
    version = str(report["model_version"])

    model_info = client.get_model_version(MODEL_NAME, version)
    if model_info.current_stage != "Production":
        print(f"[ERROR] Model version {version} is not in Production.")
        return False

    model_uri = f"models:/{MODEL_NAME}/{version}"
    print(f"[INFO] Loading registered model: {model_uri}")

    model = mlflow.sklearn.load_model(model_uri)

    X_test = np.load("data/processed/X_test_final.npy")
    if X_test.ndim != 2 or len(X_test) == 0:
        print("[ERROR] Test dataset is empty or has an invalid shape.")
        return False

    # Use one row to verify prediction capability.
    sample = X_test[:1]
    prediction = model.predict(sample)

    if len(prediction) != 1:
        print("[ERROR] Unexpected prediction output.")
        return False

    print(f"[PASS] Model loaded successfully.")
    print(f"[PASS] Input shape: {sample.shape}")
    print(f"[PASS] Prediction returned: {prediction[0]}")
    print("[SUCCESS] Production model smoke test completed.")
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as exc:
        print(f"[ERROR] Smoke test failed: {exc}")
        sys.exit(1)
