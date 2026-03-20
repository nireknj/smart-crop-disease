from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from backend.api.deps import get_db, get_current_user
from backend.models import User, ScanHistory
from backend.schemas import ScanHistoryResponse

router = APIRouter()

@router.get("/", response_model=List[ScanHistoryResponse])
def get_user_history(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    scans = db.query(ScanHistory).filter(ScanHistory.user_id == current_user.id).all()
    return scans
