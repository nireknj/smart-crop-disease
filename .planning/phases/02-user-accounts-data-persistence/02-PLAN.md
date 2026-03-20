---
wave: 1
depends_on: []
files_modified: ["backend/requirements.txt", "backend/database.py", "backend/models.py", "backend/schemas.py", "backend/api/auth.py", "backend/api/history.py", "backend/api/deps.py", "backend/api/routes.py", "backend/core/security.py", "backend/main.py"]
autonomous: true
---

# Phase 2: User Accounts & Data Persistence

## Objective
Integrate PostgreSQL (via SQLAlchemy/Alembic) and JWT-based authentication. Implement user registration, login, and scan history tracking.

## Requirements Addressed
- AUTH-01
- AUTH-02
- PLAT-01

## Must Haves
- The backend MUST be able to run Alembic migrations.
- `POST /api/auth/register` and `POST /api/auth/login` MUST be functional.
- The `ScanHistory` MUST be saved when a logged-in user uses `POST /api/predict`.

## Tasks

<task>
<description>
Setup Database and ORM models.
</description>
<read_first>
- .planning/phases/02-user-accounts-data-persistence/02-RESEARCH.md
- backend/requirements.txt
</read_first>
<action>
1. Add `sqlalchemy`, `alembic`, `passlib[bcrypt]`, `python-jose[cryptography]`, `pydantic[email]` to `backend/requirements.txt`.
2. Create `backend/database.py` to configure SQLAlchemy `create_engine` and `SessionLocal` (using sqlite for local dev fallback `sqlite:///./sql_app.db` or reading `DATABASE_URL` env var).
3. Create `backend/models.py` defining `User` (id, email, hashed_password) and `ScanHistory` (id, user_id, disease, confidence, remedy, timestamp).
4. Do not run alembic init yet, just define the models. A later developer task will initialize alembic explicitly if needed.
</action>
<acceptance_criteria>
- `backend/requirements.txt` contains `sqlalchemy` and `alembic`
- `backend/models.py` contains `class User(Base):` and `class ScanHistory(Base):`
</acceptance_criteria>
</task>

<task>
<description>
Setup JWT Authentication logic and schemas.
</description>
<read_first>
- backend/models.py
</read_first>
<action>
1. Create `backend/schemas.py` for Pydantic models: `UserCreate`, `UserResponse`, `Token`, `ScanHistoryResponse`.
2. Create `backend/core/security.py` implementing `create_access_token` and password hashing (`get_password_hash`, `verify_password`).
3. Create `backend/api/deps.py` for dependency injection: `get_db` and `get_current_user` (which decodes JWT and fetches User from DB). Allow `get_current_user_optional` as well.
</action>
<acceptance_criteria>
- `backend/schemas.py` contains `class UserCreate`
- `backend/core/security.py` contains `def create_access_token`
- `backend/api/deps.py` contains `def get_current_user`
</acceptance_criteria>
</task>

<task>
<description>
Implement API endpoints for Auth and History.
</description>
<read_first>
- backend/schemas.py
- backend/api/routes.py
</read_first>
<action>
1. Create `backend/api/auth.py` with `@router.post("/register")` and `@router.post("/login")`.
2. Modify `backend/api/routes.py`:
   - Inject `db: Session = Depends(get_db)` and `current_user: User = Depends(get_current_user_optional)`.
   - If `current_user` is present, insert a `ScanHistory` record after prediction.
3. Create `backend/api/history.py` with `@router.get("/")` to return scans for `current_user`.
4. Register the new routers (`auth`, `history`) in `backend/main.py`.
</action>
<acceptance_criteria>
- `backend/api/auth.py` contains `@router.post("/register")`
- `backend/main.py` contains `app.include_router(auth.router)`
- `backend/api/routes.py` imports `Depends` and `get_db`
</acceptance_criteria>
</task>
