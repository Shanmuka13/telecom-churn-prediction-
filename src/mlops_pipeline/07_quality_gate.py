import json
import os
import sys

REPORT_PATH = "reports/evaluation_report.json"
OUTPUT_PATH = "reports/quality_gate_report.json"

THRESHOLDS = {
    "accuracy": 0.75,
    "precision": 0.50,
    "recall": 0.70,
    "f1_score": 0.60,
    "roc_auc": 0.80,
}

def main():
    print("[INFO] Starting Stage 07: Quality Gate")

    if not os.path.exists(REPORT_PATH):
        print(f"[ERROR] Evaluation report not found: {REPORT_PATH}")
        return False

    with open(REPORT_PATH, "r", encoding="utf-8-sig") as f:
        report = json.load(f)

    metrics = report.get("metrics", {})
    checks = {
        name: {
            "threshold": threshold,
            "actual": metrics.get(name),
            "passed": (
                metrics.get(name) is not None
                and metrics[name] >= threshold
            ),
        }
        for name, threshold in THRESHOLDS.items()
    }

    passed = all(check["passed"] for check in checks.values())

    result = {
        "stage": "07 - Quality Gate",
        "status": "PASSED" if passed else "FAILED",
        "checks": checks,
    }

    os.makedirs("reports", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    for name, check in checks.items():
        state = "PASS" if check["passed"] else "FAIL"
        actual = check["actual"]
        print(f"[{state}] {name}: {actual} (minimum {check['threshold']})")

    print(f"[INFO] Report saved to {OUTPUT_PATH}")
    print(f"[{'SUCCESS' if passed else 'ERROR'}] Quality gate {result['status']}")

    return passed

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
