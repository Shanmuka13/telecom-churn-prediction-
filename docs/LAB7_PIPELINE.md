# Lab 7: MLOps Pipeline

## Objective
Build a repeatable churn-prediction workflow with data validation, preprocessing, model evaluation, quality gates, inference, and failure testing.

## Pipeline stages
1. Load the raw dataset.
2. Validate the input schema.
3. Preprocess the data.
4. Validate preprocessing outputs.
5. Train and register a model when required.
6. Evaluate model performance.
7. Apply quality thresholds.
8. Automate model lifecycle management.
9. Generate predictions using the Production model.
10. Inject invalid data and verify that validation detects it.

## Execution
Run from the project root:

    python .\src\mlops_pipeline\churn_prediction_pipeline.py

## Outputs
- artifacts/data_load_report.json
- artifacts/preprocessing_summary_report.json
- reports/evaluation_report.json
- reports/quality_gate_report.json
- outputs/lab7_inference_predictions.csv
- artifacts/failure_simulation_report.json

The orchestrator currently runs stages 01–04, 06–07, 09, and 10.
