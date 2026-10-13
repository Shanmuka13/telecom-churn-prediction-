import os
import sys

import joblib
import mlflow
import numpy as np
import pandas as pd
from mlflow.tracking import MlflowClient

MODEL_NAME = "Telco_Churn_Production_Model"
INPUT_PATH = "data/raw/new_churn.csv"
PREPROCESSOR_PATH = "models/preprocessor.pkl"
OUTPUT_PATH = "outputs/lab7_inference_predictions.csv"

def main():
    print("[INFO] Stage 09: Production Inference")

    for path in (INPUT_PATH, PREPROCESSOR_PATH):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Required file not found: {path}")

    client = MlflowClient()
    versions = client.search_model_versions(f"name='{MODEL_NAME}'")
    production = [
        version for version in versions
        if version.current_stage == "Production"
    ]

    if not production:
        raise RuntimeError(f"No Production version found for {MODEL_NAME}")

    selected = max(production, key=lambda version: int(version.version))
    model_uri = f"models:/{MODEL_NAME}/{selected.version}"
    print(f"[INFO] Loading {model_uri}")

    model = mlflow.sklearn.load_model(model_uri)
    preprocessor = joblib.load(PREPROCESSOR_PATH)

    raw = pd.read_csv(INPUT_PATH)
    customer_ids = (
        raw["customerID"].astype(str)
        if "customerID" in raw.columns
        else pd.Series(
            [f"row_{i}" for i in range(len(raw))],
            name="customerID"
        )
    )

    features = raw.drop(columns=["customerID"], errors="ignore")
    features["TotalCharges"] = pd.to_numeric(
        features["TotalCharges"], errors="coerce"
    )

    transformed = preprocessor.transform(features)

    if transformed.shape[1] != model.n_features_in_:
        raise ValueError(
            f"Feature mismatch: transformed data has {transformed.shape[1]} "
            f"features but model expects {model.n_features_in_}."
        )

    predictions = model.predict(transformed)
    probabilities = model.predict_proba(transformed)[:, 1]

    output = pd.DataFrame({
        "customerID": customer_ids,
        "predicted_churn": predictions.astype(int),
        "churn_probability": probabilities,
    })

    os.makedirs("outputs", exist_ok=True)
    output.to_csv(OUTPUT_PATH, index=False)

    print(f"[SUCCESS] Predictions saved to {OUTPUT_PATH}")
    print(f"[INFO] Rows predicted: {len(output)}")
    print(output.head().to_string(index=False))

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[ERROR] Inference failed: {exc}")
        sys.exit(1)
