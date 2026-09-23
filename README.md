# Churn Prediction — MLOps Project

This repo follows the Lab 1–5 structure from the MLOps Telco Churn project guide.

## Structure

```
churn-prediction/
├── data/
│   ├── raw/churn.csv                      # Lab 1 — raw dataset
│   └── processed/                         # Lab 1 / Lab 5 outputs (generated)
├── notebooks/project_implementation.ipynb # Lab 1
├── src/
│   ├── preprocess.py                      # Lab 1
│   ├── train.py                           # Lab 2
│   ├── evaluate.py                        # Lab 2
│   ├── train_mlflow.py                    # Lab 4
│   ├── validate_reproducibility.py        # Lab 4
│   ├── validate_data.py                   # Lab 5
│   ├── preprocess_pipeline.py             # Lab 5
│   └── validate_outputs.py                # Lab 5
├── pipelines/
│   ├── run_lab3_baseline.py
│   ├── run_lab4_tracking.py
│   └── run_lab5_pipeline.py               # Lab 5
├── models/      # generated: scaler.pkl, ohe.pkl, *.pkl model files
├── outputs/     # generated: false_negatives.csv, false_positives.csv
├── artifacts/   # generated: confusion_matrix.png, roc_curve.png, reports
├── logs/
├── mlruns/      # Lab 4 — MLflow tracking store
├── requirements.txt
└── .gitignore
```

## Note on generated files

`data/processed/*.npy`, `models/*.pkl`, `outputs/*.csv`, and `artifacts/*` are
produced by running the Lab 1, 2, 4, and 5 scripts — they aren't included here
since they didn't exist in the uploaded files. Run the pipeline scripts below
to generate them.

## Getting started

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Lab 1: preprocessing
python src/preprocess.py

# Lab 2/3: baseline training + evaluation
python pipelines/run_lab3_baseline.py
## Lab 3 Git Workflow

This project uses Git for version control, branching, merging, and reproducibility.

# Lab 4: MLflow tracking + reproducibility check
python pipelines/run_lab4_tracking.py

# Lab 5: full pipeline (validation → preprocessing → training → output checks)
python pipelines/run_lab5_pipeline.py
```

See `MLOps_Telco_Churn_Lab1-4_Project_Guide.docx` for the full lab write-up.
