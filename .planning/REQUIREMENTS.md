# Requirements: Smart Crop Disease Detection

**Defined:** 2026-03-20
**Core Value:** Accurately diagnose crop diseases from images and provide clear, practical treatment recommendations for farmers on low-end devices.

## v1 Requirements

### Authentication

- [ ] **AUTH-01**: User can sign up with email and password
- [ ] **AUTH-02**: User can log in and securely maintain session via JWT

### Core Inference (ML)

- [ ] **INFR-01**: System accepts image uploads of crop leaves
- [ ] **INFR-02**: System resizes/normalizes images for MobileNet inference
- [ ] **INFR-03**: CNN model successfully classifies disease for Tomato/Potato classes
- [ ] **INFR-04**: System returns predicted disease name and confidence percentage
- [ ] **INFR-05**: System maps predicted disease to a predefined remedy/advisory text

### Frontend UX

- [ ] **UIUX-01**: Clean, mobile-friendly landing page
- [ ] **UIUX-02**: Simple image upload interface (camera integration or file picker)
- [ ] **UIUX-03**: Client-side image compression before upload (to save bandwidth)
- [ ] **UIUX-04**: Results page clearly displaying disease, confidence, and treatment
- [ ] **UIUX-05**: User dashboard showing past scan history

### Platform & Database

- [ ] **PLAT-01**: PostgreSQL database stores user profiles and scan history
- [ ] **PLAT-02**: FastAPI backend serves endpoints and ML model efficiently
- [ ] **PLAT-03**: Application is deployable to free-tier hosting (e.g., Render)

## v2 Requirements

### Multilingual & Extended Support

- **LANG-01**: UI supports Hindi and Marathi localization
- **CROP-01**: Model expanded to support additional cash crops
- **WEAT-01**: Weather API integration to warn about blight risks
- **CHAT-01**: AI chatbot for general farming queries

## Out of Scope

| Feature | Reason |
|---------|--------|
| Complex Social Feeds | Distracts from core diagnostic value |
| Heavy 3D Graphics | Drains battery and stalls low-end devices |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| AUTH-01 | TBD | Pending |
| AUTH-02 | TBD | Pending |
| INFR-01 | TBD | Pending |
| INFR-02 | TBD | Pending |
| INFR-03 | TBD | Pending |
| INFR-04 | TBD | Pending |
| INFR-05 | TBD | Pending |
| UIUX-01 | TBD | Pending |
| UIUX-02 | TBD | Pending |
| UIUX-03 | TBD | Pending |
| UIUX-04 | TBD | Pending |
| UIUX-05 | TBD | Pending |
| PLAT-01 | TBD | Pending |
| PLAT-02 | TBD | Pending |
| PLAT-03 | TBD | Pending |

**Coverage:**
- v1 requirements: 15 total
- Mapped to phases: 0
- Unmapped: 15 ⚠️

---
*Requirements defined: 2026-03-20*
*Last updated: 2026-03-20 after initial definition*
