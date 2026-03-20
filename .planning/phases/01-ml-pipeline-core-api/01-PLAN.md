---
wave: 1
depends_on: []
files_modified: ["backend/main.py", "backend/ml/inference.py", "backend/ml/preprocess.py", "backend/api/routes.py", "backend/requirements.txt"]
autonomous: true
---

# Phase 1: ML Pipeline & Core API

## Objective
Establish the FastAPI backend and image processing pipeline. Set up a functional `/api/predict` endpoint that takes an image, processes it, runs it through MobileNetV2 (pretrained), and returns the prediction with a mapped remedy.

## Requirements Addressed
- INFR-01
- INFR-02
- INFR-03
- INFR-04
- INFR-05
- PLAT-02

## Must Haves
- The backend MUST start via Uvicorn on port 8000 without crashing.
- `POST /api/predict` MUST accept `multipart/form-data` and return JSON with `disease`, `confidence`, and `remedy`.
- The image MUST be resized to 224x224 before inference.

## Tasks

<task>
<description>
Initialize the FastAPI backend application structure and core configuration.
</description>
<read_first>
- .planning/phases/01-ml-pipeline-core-api/01-RESEARCH.md
</read_first>
<action>
1. Create `backend/` directory.
2. Create `backend/requirements.txt` with: `fastapi`, `uvicorn`, `python-multipart`, `tensorflow-cpu`, `Pillow`.
3. Create `backend/main.py` that initializes FastAPI, sets up CORS middleware to allow `*`, and includes a health check `GET /health` returning `{"status": "ok"}`.
</action>
<acceptance_criteria>
- `backend/requirements.txt` contains `fastapi` and `tensorflow-cpu`
- `backend/main.py` contains `app = FastAPI()` and `app.add_middleware(CORSMiddleware`
- `backend/main.py` contains `@app.get("/health")`
</acceptance_criteria>
</task>

<task>
<description>
Implement the image preprocessing utility.
</description>
<read_first>
- backend/requirements.txt
</read_first>
<action>
1. Create `backend/ml/preprocess.py`.
2. Write a function `process_image(file_bytes: bytes)` that:
   - Uses `PIL.Image.open(io.BytesIO(file_bytes))` to read the image.
   - Resizes it to `(224, 224)`.
   - Converts it to a numpy array.
   - Applies MobileNetV2 specific preprocessing (`tensorflow.keras.applications.mobilenet_v2.preprocess_input`).
   - Returns the standardized tensor with shape `(1, 224, 224, 3)`.
</action>
<acceptance_criteria>
- `backend/ml/preprocess.py` contains `def process_image`
- Code uses `preprocess_input`
</acceptance_criteria>
</task>

<task>
<description>
Implement the ML inference module and remedy mapping.
</description>
<read_first>
- backend/ml/preprocess.py
</read_first>
<action>
1. Create `backend/ml/inference.py`.
2. Load a pre-trained Keras model globally at the top of the file: `model = tensorflow.keras.applications.MobileNetV2(weights='imagenet')`. (Note: We use the base ImageNet model for Phase 1 to prove out the pipeline).
3. Create a dictionary `REMEDY_MAP` that maps disease names to remedy strings. Provide a dummy default output for phase 1.
4. Write a function `predict_disease(tensor)` that:
   - Passes tensor to `model.predict(tensor)`.
   - Uses `decode_predictions` to get the top prediction name and confidence score.
   - Looks up the name in `REMEDY_MAP` or uses the fallback.
   - Returns `{"disease": name, "confidence": float(score), "remedy": remedy}`.
</action>
<acceptance_criteria>
- `backend/ml/inference.py` contains `model = tensorflow.keras.applications.MobileNetV2`
- Function returns a dict with keys exactly matching: `disease`, `confidence`, `remedy`
</acceptance_criteria>
</task>

<task>
<description>
Wire up the `/api/predict` endpoint.
</description>
<read_first>
- backend/main.py
- backend/ml/inference.py
- backend/ml/preprocess.py
</read_first>
<action>
1. Create `backend/api/routes.py`.
2. Define an `APIRouter` and a `@router.post("/predict")` endpoint.
3. The endpoint should accept `file: UploadFile = File(...)`.
4. Read the bytes from the file, call `process_image()`, then call `predict_disease()`.
5. Implement basic error handling (try/except) returning 400 or 500 HTTP exceptions on failure.
6. Register the router in `backend/main.py` under the prefix `/api`.
</action>
<acceptance_criteria>
- `backend/api/routes.py` contains `@router.post("/predict")`
- `backend/main.py` contains `app.include_router`
</acceptance_criteria>
</task>
