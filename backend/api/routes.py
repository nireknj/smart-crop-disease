from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.ml.preprocess import process_image
from backend.ml.inference import predict_disease
from backend.api.deps import get_db, get_current_user_optional
from backend.models import User, ScanHistory

router = APIRouter()

@router.post("/predict")
async def predict_endpoint(file: UploadFile = File(...), current_user: User = Depends(get_current_user_optional), db: Session = Depends(get_db)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")
    try:
        file_bytes = await file.read()
        tensor = process_image(file_bytes)
        result = predict_disease(tensor)
        
        if current_user:
            scan = ScanHistory(
                user_id=current_user.id,
                disease=result["disease"],
                confidence=result["confidence"],
                remedy=result["remedy"]
            )
            db.add(scan)
            db.commit()
            
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
