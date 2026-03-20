# Architecture Research

**Domain:** Crop Disease Detection Web App
**Researched:** 2026-03-20
**Confidence:** HIGH

## System Architecture

### Component Boundaries
1. **Frontend Client (React/SPA):**
   - Handles UI, Camera access, Image compression before upload.
   - Communicates via REST APIs.
2. **Backend API (FastAPI):**
   - Handles Authentication, User Management.
   - Accepts image uploads, validates them.
   - Calls the Inference Engine.
3. **Inference Engine (TF/PyTorch wrapped in FastAPI):**
   - Loads the pre-trained MobileNet model.
   - Processes the image tensor, gets top prediction.
4. **Database (PostgreSQL):**
   - Stores Users, Scan History, and Advisory Content (Remedies mapping).

### Data Flow
1. User captures image -> React compresses it -> POST `/api/predict`.
2. FastAPI receives image -> validates JWT -> passes to Inference Engine.
3. Inference Engine predicts -> FastAPI queries DB for Remedy text.
4. FastAPI returns `{disease, confidence, remedy}` -> React displays.

### Build Order
1. **Phase 1: ML Pipeline.** Train MobileNet on PlantVillage, export lightweight model.
2. **Phase 2: Backend API.** Build FastAPI shell, integrate model, add auth & DB.
3. **Phase 3: Frontend UI.** Build React app, wire up to API.
4. **Phase 4: Deployment.** Deploy to Render/Vercel.
