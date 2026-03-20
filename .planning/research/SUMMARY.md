# Research Summary

**Domain:** Crop Disease Detection Web App
**Researched:** 2026-03-20

## Key Findings

**Stack:** 
FastAPI is the standard for serving Python ML models efficiently. React is recommended for the frontend to ensure a responsive, maintainable mobile-first experience. MobileNet is the go-to architecture for the model to ensure it fits within free-tier RAM limits (512MB).

**Table Stakes:** 
Image capture/upload, fast CNN-based disease classification, confidence scores, and immediately actionable treatment advice. The UI must be dead simple and mobile-friendly.

**Watch Out For:** 
- **Memory Limits:** Free tier servers will crash if you use large models like ResNet. Stick to MobileNet or TFLite.
- **Data Usage:** Farmers have slow internet; compress images on the client *before* uploading.
- **False Positives:** The model might predict diseases on non-leaf images. Implement confidence thresholds.

**Recommended Build Order:**
1. ML Pipeline (Training & Model Export)
2. Backend Infrastructure & API (FastAPI + Auth)
3. Frontend Client (React)
4. Deployment & Optimization
