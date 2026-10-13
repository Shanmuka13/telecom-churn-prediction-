import json
import os
import sys

def main():
    registry_path = "artifacts/production_model_report.json"
    output_path = "artifacts/deployment_readiness_report.json"

    print("[INFO] Starting Lab 8: Deployment Readiness Validation")

    if not os.path.exists(registry_path):
        print(f"[ERROR] Missing registry report: {registry_path}")
        return False

    with open(registry_path, "r", encoding="utf-8-sig") as f:
        registry = json.load(f)

    metrics = registry.get("performance_metrics", {})
    checks = {
        "registry_ready": registry.get("registry_status") == "READY_FOR_DEPLOYMENT",
        "model_in_production": registry.get("model_lineage", {}).get("current_stage") == "Production",
        "recall_at_least_0.70": metrics.get("recall", 0) >= 0.70,
        "f1_at_least_0.60": metrics.get("f1_score", 0) >= 0.60,
        "roc_auc_at_least_0.80": metrics.get("roc_auc", 0) >= 0.80,
    }

    for name, passed in checks.items():
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")

    ready = all(checks.values())
    report = {
        "stage": "Lab 8 - Deployment Readiness Validation",
        "model_name": registry.get("model_lineage", {}).get("registered_name"),
        "model_version": registry.get("model_lineage", {}).get("version"),
        "checks": checks,
        "performance_metrics": metrics,
        "deployment_ready": ready,
    }

    os.makedirs("artifacts", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    print(f"[INFO] Report saved to {output_path}")
    print("[SUCCESS] Model is ready for deployment." if ready
          else "[WARNING] Model did not pass all readiness checks.")

    return ready

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
