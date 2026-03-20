# Phase 2: User Accounts & Data Persistence - Research

## Technical Approach
- **Database:** PostgreSQL. We will use `SQLAlchemy` as the ORM and `asyncpg` for asynchronous database connections or standard `psycopg2-binary`. For local development before Postgres is spun up, we can use `sqlite` (with generic async support if possible, or build the schema in a way that is easily portable). Given FastAPI's async nature, `SQLAlchemy` is best practice.
- **Migrations:** `Alembic` to manage database schema migrations.
- **Authentication:** `passlib[bcrypt]` for password hashing and `python-jose[cryptography]` for JWT creation and validation.
- **Models:**
  - `User`: id, email (unique), hashed_password, created_at.
  - `ScanHistory`: id, user_id (foreign key), image_path/url (optional for now), disease_name, confidence, remedy, created_at.

## API Additions
- `POST /api/auth/register`: Create a new user.
- `POST /api/auth/login`: Return a JWT access token.
- `GET /api/users/me`: Return current user profile.
- `GET /api/history`: Return history of scans for the authenticated user.
- Modifications to `POST /api/predict`: Link the prediction to a user if authenticated, and save to database.

## Dependencies added
- `sqlalchemy`, `alembic`, `passlib[bcrypt]`, `python-jose[cryptography]`, `pydantic[email]`.
