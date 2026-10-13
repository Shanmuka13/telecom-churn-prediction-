# Git Workflow

## Check the current changes

    git status

## Create a feature branch

    git switch -c feature/mlops-labs

## Stage and commit changes

    git add .
    git commit -m "Complete MLOps lab pipeline and CI documentation"

## Push the branch

    git push -u origin feature/mlops-labs

## Review
Open a pull request on GitHub and check the Actions results before merging.

Do not commit virtual environments, credentials, local MLflow databases, or large generated artifacts unless the project specifically requires them.
