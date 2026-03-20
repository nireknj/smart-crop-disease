# Phase 1: ML Pipeline & Core API - Research

## Technical Approach
- **API Framework:** FastAPI with Uvicorn for asynchronous model serving.
- **ML Engine:** TensorFlow (CPU-only version to save memory/storage on free tiers) using MobileNetV2 for lightweight inference.
- **Image Processing:** Use `Pillow` and `python-multipart` to accept `multipart/form-data` image uploads. Images must be resized to 224x224 and normalized.
- **Model Storage:** The model should be saved in `saved_model` or `.tflite` format. For Phase 1, a dummy model or a pre-trained base model will be loaded to establish the API contract before full domain training is completed.

## API Contract
- **Endpoint:** `POST /api/predict`
- **Request:** `multipart/form-data` containing `file` (image/jpeg, image/png).
- **Response (200 OK):**
  ```json
  {
    "disease": "Tomato_Blight",
    "confidence": 0.92,
    "remedy": "Remove infected leaves. Apply copper-based fungicide."
  }
  ```

## Validation Architecture
- **API Tests:** Use `fastapi.testclient` to ensure endpoints return 200 OK for valid images and 400 Bad Request for non-image inputs.
- **Mock Inference:** Ensure the model prediction logic is cleanly decoupled from the API route so it can be mocked during basic CI tests.
