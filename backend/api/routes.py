from fastapi import APIRouter, File, UploadFile, HTTPException
from backend.ml.preprocess import process_image
from backend.ml.inference import predict_disease

router = APIRouter()

@router.post("/predict")
async def predict_endpoint(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")
    try:
        file_bytes = await file.read()
        tensor = process_image(file_bytes)
        result = predict_disease(tensor)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
