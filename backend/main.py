from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router as predict_router
from backend.api.auth import router as auth_router
from backend.api.history import router as history_router
from backend.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Crop Disease Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(history_router, prefix="/api/history", tags=["history"])
app.include_router(predict_router, prefix="/api")

@app.get("/health")
def health_check():
    return {"status": "ok"}
