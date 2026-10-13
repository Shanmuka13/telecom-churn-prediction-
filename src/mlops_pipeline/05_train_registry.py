import subprocess
import sys

result = subprocess.run(
    [sys.executable, "src/train_registry.py"],
    check=False
)
if result.returncode != 0:
    sys.exit(result.returncode)

print("[SUCCESS] Stage 05: Model training and registration script finished.")
