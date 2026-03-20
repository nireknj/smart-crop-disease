# Phase 1 Validation Strategy
**Phase:** 01-ml-pipeline-core-api
**Date:** 2026-03-20

## Core Requirements Validation

| Requirement | Test Method | Success Criteria |
|-------------|-------------|------------------|
| INFR-01 (Image uploads) | API Test | POST to `/api/predict` with dummy image succeeds without 500 error |
| INFR-02 (Resize images) | Unit Test | Processing function output tensor is shape (1, 224, 224, 3) |
| INFR-04 (Return disease/conf) | API Test | Response JSON contains `disease` (string) and `confidence` (float) |
| PLAT-02 (FastAPI backend) | Process Test | Web server starts successfully via `uvicorn main:app` |

## Integration Testing
- Standup the FastAPI app and hit the `/api/predict` endpoint using `curl` or Postman with a test leaf image. Verify the ML prediction is mapped to the internal disease database/dictionary.

## Acceptance
- The backend API runs without errors.
- Image uploads are properly parsed into tensors.
- The dummy/initial model runs inference and returns the expected JSON structure.
