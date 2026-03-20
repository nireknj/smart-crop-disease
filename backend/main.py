import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router as predict_router
from backend.api.auth import router as auth_router
from backend.api.history import router as history_router
from backend.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Crop Disease Detection API")

# CORS: allow local dev + production Vercel frontend
FRONTEND_URL = os.environ.get("FRONTEND_URL", "")
allow_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
if FRONTEND_URL:
    allow_origins.append(FRONTEND_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(history_router, prefix="/api/history", tags=["history"])
app.include_router(predict_router, prefix="/api")

import traceback
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def debug_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc), "traceback": traceback.format_exc()}
    )

@app.get("/health")
def health_check():
    return {"status": "ok"}
