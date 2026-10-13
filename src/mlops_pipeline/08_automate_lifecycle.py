import subprocess
import sys

print("[INFO] Stage 08: Automated Model Lifecycle")

result = subprocess.run(
    [sys.executable, "src/automate_lifecycle.py"],
    check=False
)

if result.returncode != 0:
    print("[ERROR] Model lifecycle automation failed.")
    sys.exit(result.returncode)

print("[SUCCESS] Stage 08 completed.")
