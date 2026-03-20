# Roadmap: Smart Crop Disease Detection

**Created:** 2026-03-20
**Granularity:** Coarse
**Total Phases:** 4

## Phase 1: ML Pipeline & Core API

**Goal:** Establish the foundational ML model and serve it via a stateless FastAPI endpoint.

**Requirements Mapped:**
- INFR-01
- INFR-02
- INFR-03
- INFR-04
- INFR-05
- PLAT-02

**Success Criteria:**
1. Developer can run the FastAPI server locally and submit a leaf image via cURL/Postman.
2. API returns a JSON response with disease name, confidence (>0.0), and treatment advice.
3. System processes images in under 1 second locally using the MobileNet model.

## Phase 2: User Accounts & Data Persistence

**Goal:** Integrate PostgreSQL database and JWT authentication to store user profiles and scan history.

**Requirements Mapped:**
- AUTH-01
- AUTH-02
- PLAT-01

**Success Criteria:**
1. User can register an account and receive a JWT token.
2. User can authenticate API requests using the JWT token.
3. Scan results are automatically saved to the database linked to the authenticated user.

## Phase 3: Web Frontend & Integration

**Goal:** Build the React/web client for farmers to easily upload images and view history.

**Requirements Mapped:**
- UIUX-01
- UIUX-02
- UIUX-03
- UIUX-04
- UIUX-05

**Success Criteria:**
1. User can access a mobile-friendly landing page and log in.
2. User can upload a photo (which is compressed client-side) and receive a visual diagnosis and remedy.
3. User can navigate to their dashboard and see previously uploaded scans and results.

## Phase 4: Production Deployment

**Goal:** Deploy the full stack application to free-tier cloud providers.

**Requirements Mapped:**
- PLAT-03

**Success Criteria:**
1. Frontend is accessible via a public URL (e.g., Vercel).
2. Backend API and ML model are hosted securely (e.g., Render) and respond to frontend requests.
3. Database is hosted and connected.
