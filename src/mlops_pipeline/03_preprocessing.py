import subprocess
import sys

result = subprocess.run(
    [sys.executable, "src/preprocess_pipeline.py"],
    check=False
)
if result.returncode != 0:
    sys.exit(result.returncode)

print("[SUCCESS] Stage 03: Preprocessing completed.")
