# Phase 2 Validation Strategy

## Core Requirements Validation
| Requirement | Test Method | Success Criteria |
|-------------|-------------|------------------|
| AUTH-01 (Secure Auth) | API Test | `POST /api/auth/register` creates user, `POST /api/auth/login` succeeds with valid credentials and fails with invalid |
| AUTH-02 (JWT tokens) | API Test | `GET /api/users/me` requires `Authorization: Bearer <token>` |
| PLAT-01 (Database) | Process Test | Alembic migrations run successfully against local Postgres/Sqlite |

## Integration Testing
- The `/api/predict` endpoint correctly stores a record in the `ScanHistory` table if the user provides a valid JWT token.
- Unauthenticated users can still predict (guest scans), or are blocked based on the endpoint's configuration. We will allow guest scans but only save for authenticated users.
