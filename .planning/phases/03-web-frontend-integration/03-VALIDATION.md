# Phase 3 Validation Strategy

## Core Requirements Validation
| Requirement | Test Method | Success Criteria |
|-------------|-------------|------------------|
| UIUX-01 (Simple UI) | Visual Inspect | UI is clean, minimalistic, and usable on mobile screens |
| UIUX-02 (Upload photo) | Functional Test | User can select a photo from their device and upload it to the backend |
| UIUX-03 (Display result) | Functional Test | Backend response (disease, confidence, remedy) renders clearly in a Results Card |
| UIUX-04 (History view) | Functional Test | Scanning history appears in a list by fetching `/api/history` |
| UIUX-05 (Mobile responsive) | Visual Inspect | Layout stacks correctly on narrow viewports natively |

## Integration Testing
- The frontend correctly sends `Authorization: Bearer <token>` to protected backend routes (`/api/predict`, `/api/history`).
- Form data for image uploads is correctly formatted as `multipart/form-data`.
