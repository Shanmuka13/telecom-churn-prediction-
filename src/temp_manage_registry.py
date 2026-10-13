from mlflow import MlflowClient

def main():
    client = MlflowClient()
    model_name = "Telco_Churn_Production_Model"

    print(f"[INFO] Registered versions for {model_name}")

    try:
        versions = client.search_model_versions(
            f"name='{model_name}'"
        )

        if not versions:
            print("[INFO] No registered versions found.")
            return

        for version in versions:
            print(
                f"Version={version.version}, "
                f"Stage={version.current_stage}, "
                f"Status={version.status}"
            )

    except Exception as exc:
        print(f"[ERROR] Could not read model registry: {exc}")
        raise

if __name__ == "__main__":
    main()
