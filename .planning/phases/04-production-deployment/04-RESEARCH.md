# Phase 4: Production Deployment — Research

**Phase:** 4 — Production Deployment
**Written:** 2026-03-20

---

## 1. Neon PostgreSQL Setup

**Project Creation:**
- Sign up at neon.tech → create project → copy the connection string from the dashboard
- Default format: `postgresql://[USER]:[PASSWORD]@[HOSTNAME]/[DBNAME]?sslmode=require`
- Some providers emit `postgres://` — SQLAlchemy 2.0+ requires `postgresql://` prefix; fix programmatically if needed

**SQLAlchemy Driver:**
- Use `psycopg2-binary` for synchronous SQLAlchemy (already compatible with existing sync FastAPI code)
- Add `psycopg2-binary` to `requirements.txt` — Neon requires it; SQLite used `pysqlite` (built-in)
- Connection URL for Neon: `postgresql+psycopg2://USER:PASS@HOST/DBNAME?sslmode=require`

**backend/database.py Migration:**
- Currently reads `DATABASE_URL` from env with SQLite fallback — no logic change needed
- Just ensure `DATABASE_URL` is set on Render to the Neon connection string
- SQLite uses `connect_args={"check_same_thread": False}` — this must be removed/guarded for PostgreSQL

**Alembic on Render:**
- `alembic.ini` → set `sqlalchemy.url` dynamically via `env.py` (read from `os.environ["DATABASE_URL"]`)
- Build Command on Render: `pip install -r requirements.txt && alembic upgrade head`
- This ensures DB schema is migrated before the new server starts serving traffic

---

## 2. Render Backend Deployment

**Service Config:**
- Service Type: Web Service
- Runtime: Python 3 (Render auto-detects)
- Root Directory: Leave blank (repo root), OR set to `backend/` if using a sub-directory layout
- Build Command: `pip install -r requirements.txt && alembic upgrade head`
- Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`

**Environment Variables (set in Render dashboard):**
```
DATABASE_URL   = postgresql+psycopg2://USER:PASS@HOST/DBNAME?sslmode=require
SECRET_KEY     = <random 32+ char string>
ALGORITHM      = HS256
```

**CORS Update in backend/main.py:**
```python
allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://<your-app>.vercel.app",   # ← add Vercel prod URL
]
```

**Cold Start Warning:**
- Render free tier: spins down after 15 min inactivity
- First request after spin-down takes ~30–60 seconds
- Acceptable for MVP; note this in the README

---

## 3. Vercel Frontend Deployment

**Project Setup:**
- Connect GitHub repo → Vercel detects it as a Vite project
- Root Directory: `frontend`
- Framework Preset: Vite
- Build Command: `npm run build`
- Output Directory: `dist`

**Environment Variable:**
- Set `VITE_API_URL = https://<your-backend>.onrender.com` in Vercel project settings → Production environment

**frontend/src/api/client.js Change:**
```js
// Before:
baseURL: 'http://127.0.0.1:8000'

// After:
baseURL: import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000'
```
The `|| 'http://127.0.0.1:8000'` fallback keeps local dev working without `.env.local`.

**React Router / vercel.json:**
Without this, direct URL access (e.g., `yourapp.vercel.app/dashboard`) returns 404:
```json
// frontend/vercel.json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/" }
  ]
}
```

---

## 4. Database Migration Plan

**Current state:** SQLite file (`sql_app.db`) in project root — local dev only, not deployed to Render.

**Migration Steps:**

1. Ensure `psycopg2-binary` is in `requirements.txt`
2. Update `alembic/env.py` to read `DATABASE_URL` from env:
   ```python
   import os
   config.set_main_option("sqlalchemy.url", os.environ.get("DATABASE_URL", "sqlite:///./sql_app.db"))
   ```
3. Generate initial migration (run locally against Neon URL):
   ```bash
   DATABASE_URL=<neon_url> alembic revision --autogenerate -m "initial_schema"
   ```
4. Review the generated migration file, then apply:
   ```bash
   DATABASE_URL=<neon_url> alembic upgrade head
   ```
5. On Render, the Build Command runs `alembic upgrade head` automatically on each deploy

**Key SQLite → PostgreSQL differences:**
- PostgreSQL uses `SERIAL`/`SEQUENCE` for autoincrement — SQLAlchemy handles this transparently with `Integer, primary_key=True`
- SQLite `check_same_thread` arg must be removed for PostgreSQL connections
- Boolean columns: PostgreSQL uses native `BOOLEAN`; SQLite uses `INTEGER` — no code change needed with SQLAlchemy ORM

---

## 5. Validation Architecture

### Dimension 1: Environment Config
- Render env vars (DATABASE_URL, SECRET_KEY, ALGORITHM) accessible at runtime
- VITE_API_URL accessible in built frontend bundle (prefixed with VITE_)
- **Check:** `GET https://<render-url>/health` returns `{"status": "ok"}`

### Dimension 2: Backend Health
- `GET /health` → returns `{"status": "ok"}` at Render URL
- `POST /api/auth/register` with valid JSON → returns 201/200 (no 500 errors)
- **Check:** `curl -X POST https://<render>/api/auth/register -H "Content-Type: application/json" -d '{"email":"t@t.com","password":"abc"}'`

### Dimension 3: Frontend Accessibility
- Vercel URL loads the app (no blank screen, no JS errors in console)
- `/login` route renders correctly
- `/register` route renders correctly
- Direct URL access (e.g., `yourapp.vercel.app/history`) doesn't 404
- **Check:** Navigate to Vercel URL in browser; open DevTools → Console: no errors

### Dimension 4: Database Connectivity
- Successful registration stores user in Neon PostgreSQL (verify via Neon console query)
- Login after registration succeeds, returns JWT token
- Scan history persists across browser refreshes
- **Check:** `SELECT * FROM users` in Neon console after registering

### Dimension 5: CORS
- Frontend at Vercel URL can `POST /api/auth/register` to Render URL without CORS errors
- No `Access-Control-Allow-Origin` header errors in browser DevTools → Network tab
- **Check:** Register user from frontend, observe Network tab → register request has 200 response

---

## 6. Risks & Gotchas

| Risk | Mitigation |
|------|-----------|
| `passlib`/`bcrypt` Python 3.14 incompatibility | Already mocked in `backend/core/security.py` — keep the mock for MVP; note in README |
| Render free tier: 512MB RAM limit | ML inference is already mocked (no TF loaded); should be well within limit |
| Render cold starts (15 min spin-down) | Acceptable for MVP; warn users in README |
| Neon free tier: max 10 concurrent connections | Set `pool_size=5, max_overflow=0` in SQLAlchemy `create_engine()` |
| `sslmode=require` missing from DATABASE_URL | Always append `?sslmode=require` to Neon URL |
| SQLite `check_same_thread` arg crashes PostgreSQL | Guard with: `connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}` |
| Vite env vars not prefixed with `VITE_` | All frontend env vars must be `VITE_*` — `VITE_API_URL` ✓ |
| Render `$PORT` not used in start command | Must use `--port $PORT` in start command — not hardcoded 8000 |
| Images uploaded to backend are ephemeral on Render | For MVP, base64 data in DB or accept loss; v2 → Cloudinary / S3 |
| alembic.ini still points to SQLite URL | Must update `env.py` to read from `DATABASE_URL` env var dynamically |
