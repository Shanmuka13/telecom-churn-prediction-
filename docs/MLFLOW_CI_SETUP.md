# MLflow and CI Setup

## Local MLflow
The project uses MLflow for experiment tracking and model registry operations. The registered model used for inference is `Telco_Churn_Production_Model`.

## Local requirements
- Python virtual environment
- Project dependencies from `requirements.txt`
- Raw churn dataset under `data/raw/`
- A locally available MLflow tracking store and registered Production model for inference

## Continuous Integration
GitHub Actions runs automated tests independently of the local Production model registry. Registry-dependent inference may require a separately configured tracking store and registered model.

## Security
Do not commit passwords, API keys, access tokens, or private database connection strings. Use GitHub Actions secrets for any credentials needed by a workflow.
