# Lab 9: Failure Handling Report

## Objective
Verify that the data validation system detects invalid input instead of accepting corrupted data.

## Test procedure
1. Read the original churn dataset.
2. Create a separate in-memory copy.
3. Replace a valid gender value with `INVALID_GENDER`.
4. Validate the corrupted copy.
5. Record the validation error and test result.

## Observed result
The validator detected the invalid gender value at row index 0.

## Output files
- artifacts/corrupted_simulation_errors.csv
- artifacts/failure_simulation_report.json

The original raw dataset should remain unchanged. The test demonstrates schema-error detection; it does not represent a production service outage test.
