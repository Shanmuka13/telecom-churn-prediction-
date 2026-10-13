import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PYTHON = sys.executable

STAGES = [
    ("01_load_data.py", "Load Data"),
    ("02_validate_data.py", "Validate Data"),
    ("03_preprocessing.py", "Preprocessing"),
    ("04_validate_outputs.py", "Validate Preprocessing Outputs"),
    ("06_model_evaluation.py", "Model Evaluation"),
    ("07_quality_gate.py", "Quality Gate"),
    ("09_inference.py", "Production Inference"),
    ("10_failure_injection.py", "Failure Injection Test"),
]

def main():
    print("=" * 60)
    print("CHURN PREDICTION - MLOPS PIPELINE")
    print("=" * 60)

    for script, name in STAGES:
        path = ROOT / "src" / "mlops_pipeline" / script

        print(f"\n[INFO] Running: {name}")
        result = subprocess.run(
            [PYTHON, str(path)],
            cwd=ROOT
        )

        if result.returncode != 0:
            print(f"[FAILED] Pipeline stopped at: {name}")
            sys.exit(result.returncode)

        print(f"[SUCCESS] Completed: {name}")

    print("\n" + "=" * 60)
    print("[SUCCESS] All pipeline stages completed.")
    print("Predictions: outputs/lab7_inference_predictions.csv")
    print("Quality report: reports/quality_gate_report.json")
    print("Failure report: artifacts/failure_simulation_report.json")
    print("=" * 60)

if __name__ == "__main__":
    main()
