import sys
sys.path.insert(0, "src")
from validate_outputs import validate_preprocessing_outputs

if not validate_preprocessing_outputs():
    sys.exit(1)

print("[SUCCESS] Stage 04: Output validation passed.")
