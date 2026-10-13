# Lab 8: Continuous Integration Report

## Objective
Use GitHub Actions to install dependencies and run automated project tests on pushes and pull requests.

## Workflow
The workflow is defined in `.github/workflows/lab8_ci.yml`.

It checks out the repository, sets up Python, installs dependencies, and runs pytest.

## Expected result
The workflow should complete successfully when dependencies install correctly and all tests pass.

## Evidence
After pushing the repository, open GitHub Actions and save the successful workflow run as evidence.

Note: a local test pass does not prove that the GitHub Actions run has passed.
