# Phase 4: Production Deployment - Context

**Gathered:** 2026-03-20
**Status:** Ready for planning
**Source:** Claude's Discretion (user delegated all decisions)

<domain>
## Phase Boundary

Deploy the complete Smart Crop Disease Detection system — FastAPI backend + React/Vite frontend + PostgreSQL database — to free-tier cloud providers so the app is publicly accessible via static URLs.

This phase does NOT expand features. It converts the local-only dev setup into a production-ready deployment.

</domain>

<decisions>
## Implementation Decisions

### 1. Database Hosting
- **Provider: Neon** (neon.tech) — managed serverless PostgreSQL, free tier (0.5 GB, unlimited branches)
- Migrate from local SQLite (`sql_app.db`) to PostgreSQL for production
- SQLite stays in place for local development — `DATABASE_URL` env var switches between them
- Neon connection string injected via Render's environment variables

### 2. Backend Hosting
- **Provider: Render** (render.com) — free tier web service for Python
- Deploy `uvicorn backend.main:app` as a web service
- Auto-deploy from GitHub `main` branch on push
- Set environment variables via Render dashboard (never commit secrets)
- CORS `allow_origins` in `main.py` must be updated to the production Vercel URL

### 3. Frontend Hosting
- **Provider: Vercel** (vercel.com) — zero-config Vite/React deployment
- Auto-deploy from GitHub `main` branch on push
- `frontend/.env.production` must define `VITE_API_URL=https://<render-service>.onrender.com`
- Vercel CDN provides low-latency delivery for Indian users

### 4. Environment & Secrets Management
- **Backend (Render):** All secrets set in Render dashboard environment variables:
  - `DATABASE_URL` — Neon PostgreSQL connection string
  - `SECRET_KEY` — cryptographically random string (generate once, never rotate unless needed)
  - `ALGORITHM` — `HS256`
- **Frontend (Vercel):** `VITE_API_URL` set as Vercel project environment variable for Production environment
- **Local dev:** `.env` file (already gitignored) with SQLite URL and local secret key
- **NEVER commit** `.env`, secrets, or connection strings to git

### 5. ML Model Handling
- Since ML inference is currently mocked (TensorFlow removed due to Python 3.14 compat), the mock stays in production for now — real model integration deferred to v2
- No GPU or special compute resources needed for Render free tier

### 6. Database Migration
- Alembic (already in `requirements.txt`) used to run migrations against Neon PostgreSQL
- `alembic upgrade head` run as part of the Render build command before starting the server

### Claude's Discretion
- Build/start command on Render: `pip install -r requirements.txt && alembic upgrade head`; start: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
- Root redirect (`/`) should return health JSON so Render health checks pass
- Vercel `vercel.json` with `rewrites` to handle React Router's client-side routing

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project Stack & Constraints
- `.planning/PROJECT.md` — Vision, target users, cost constraints
- `.planning/REQUIREMENTS.md` — PLAT-03 (free-tier deployment requirement)
- `.planning/ROADMAP.md` — Phase 4 success criteria

### Current Backend Code
- `backend/main.py` — FastAPI app entry point, CORS config (must update allow_origins for prod URL)
- `backend/database.py` — SQLAlchemy setup (must switch to PostgreSQL via DATABASE_URL env var)
- `backend/requirements.txt` — Dependencies to install on Render

### Current Frontend Code
- `frontend/src/api/client.js` — Axios baseURL (must use `import.meta.env.VITE_API_URL` for prod)
- `frontend/package.json` — Build scripts (`npm run build` for Vercel)

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `backend/database.py` — Already uses `DATABASE_URL` env variable with SQLite fallback; just needs the env var set to Neon's PostgreSQL string on Render
- `backend/requirements.txt` — `alembic` already included; used for DB migrations
- `frontend/src/api/client.js` — Axios client; baseURL must be updated to read from `VITE_API_URL`

### Established Patterns
- Backend uses SQLAlchemy ORM — compatible with both SQLite (local) and PostgreSQL (prod) without model changes
- Frontend is Vite-based — `npm run build` outputs to `dist/` folder; Vercel detects this automatically

### Integration Points
- `backend/main.py` → `allow_origins` list must include the Vercel production URL
- `backend/main.py` → `uvicorn` start command on Render must bind to `0.0.0.0:$PORT`
- `frontend/src/api/client.js` → Change hardcoded `http://127.0.0.1:8000` to `import.meta.env.VITE_API_URL`

</code_context>

<specifics>
## Specific Ideas

- Use `DATABASE_URL` env var to keep the same codebase for local (SQLite) and prod (PostgreSQL) — no code branch needed
- Render free tier spins down after 15 min inactivity; first request after spin-down takes ~30s. Acceptable for MVP
- For Vercel, React Router requires a `vercel.json` with: `"rewrites": [{ "source": "/(.*)", "destination": "/" }]`

</specifics>

<deferred>
## Deferred Ideas

- Real ML model deployment (TensorFlow/PyTorch on GPU, HuggingFace Inference API) — v2 scope
- Custom domain (e.g., smartcrop.in) — v2 scope
- CI/CD pipeline with tests before deploy — v2 scope
- Render paid tier to avoid spin-down cold starts — v2 scope
- Hindi/Marathi UI localization — v2 scope

</deferred>

---

*Phase: 04-production-deployment*
*Context gathered: 2026-03-20 via Claude's Discretion (all defaults)*
