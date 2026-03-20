---
phase: 4
slug: production-deployment
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-03-20
---

# Phase 4 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Manual curl + browser verification (no automated test suite) |
| **Config file** | none |
| **Quick run command** | `curl https://<render-url>/health` |
| **Full suite command** | Manual browser walkthrough via acceptance checklist |
| **Estimated runtime** | ~5 minutes manual |

---

## Sampling Rate

- **After every task commit:** Check the specific deployment service is healthy
- **After every plan wave:** Run the full manual acceptance checklist
- **Before `/gsd-verify-work`:** All 5 validation dimensions must be green
- **Max feedback latency:** ~5 minutes

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | Status |
|---------|------|------|-------------|-----------|-------------------|--------|
| 4-01-01 | 01 | 1 | PLAT-03 | manual | `curl https://<render>/health` | ⬜ pending |
| 4-01-02 | 01 | 1 | PLAT-03 | manual | Confirm DB tables in Neon console | ⬜ pending |
| 4-02-01 | 02 | 2 | PLAT-03 | manual | `curl -X POST https://<render>/api/auth/register` | ⬜ pending |
| 4-03-01 | 03 | 3 | PLAT-03 | manual | Open Vercel URL in browser, check no console errors | ⬜ pending |
| 4-03-02 | 03 | 3 | PLAT-03 | manual | Register → Login → Dashboard → History flow | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

None — this phase has no automated tests. All verification is manual via curl and browser.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Backend serves /health at Render URL | PLAT-03 | External cloud service | `curl https://<render-url>/health` → `{"status":"ok"}` |
| DB tables created in Neon | PLAT-03 | Cloud DB requires console check | Run `SELECT * FROM users LIMIT 1` in Neon SQL console |
| Frontend loads at Vercel URL | PLAT-03 | Browser render check | Navigate to Vercel URL; confirm no blank screen |
| Full E2E: Register + Login + Analyze | PLAT-03 | Cross-origin user journey | Register with new email, login, upload leaf image, check result |
| CORS: no errors from Vercel → Render | PLAT-03 | Browser DevTools check | Open DevTools → Network tab: register request returns 200 (not CORS error) |

---

## Validation Sign-Off

- [ ] Backend `/health` returns 200 at Render URL
- [ ] `POST /api/auth/register` returns 200 in Neon-backed environment
- [ ] Frontend loads at Vercel URL with no blank screen
- [ ] React Router deep links don't 404 (e.g., `/history` direct access)
- [ ] CORS: frontend can call backend without network errors
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
