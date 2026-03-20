# Smart Crop Disease Detection and Advisory System

## What This Is

An AI-powered web platform for small and medium-scale farmers in India that allows them to upload photos of crop leaves to identify diseases and receive actionable treatment advice. It focuses on a clean, simple, and mobile-friendly experience to reduce crop loss and improve yields.

## Core Value

Accurately diagnose crop diseases from images and provide clear, practical treatment recommendations for farmers on low-end devices.

## Requirements

### Validated

- [x] API backend using FastAPI to serve the ML model *(Validated in Phase 1: ML Pipeline & Core API)*
- [x] CNN-based ML model (MobileNet or similar) logic initialized for disease classification *(Validated in Phase 1)*

### Active

- [ ] Image upload functionality for crop leaves (UI)
- [ ] Support for Tomato and Potato crops initially
- [ ] Display disease name and confidence score (UI)
- [ ] Advisory system providing pesticide/organic treatment suggestions and preventive measures
- [ ] Simple, clean, minimal, mobile-friendly UI (HTML/CSS/JS or React)
- [ ] Secure user authentication
- [ ] Database-driven backend to store user history/data
- [ ] Deployable on free tiers (Render, Vercel, HuggingFace)

### Out of Scope

- Heavy, complex UI frameworks — needs to remain fast on slow internet
- Support for all crops immediately — scaling incrementally after Tomato/Potato

## Context

- Target users are farmers in India with basic smartphone access and potentially slow internet connections.
- The system must prioritize real-world usability and low-latency inference over complex engineering.
- Expected to be a portfolio/resume-worthy project demonstrating full-stack and applied ML skills.
- Potential future additions: Hindi/Marathi localization, weather risk suggestions, chatbot, real-time camera detection.

## Constraints

- **Performance**: Must remain lightweight and load quickly on low-end mobile devices and slow internet.
- **Cost**: Infrastructure must utilize free hosting platforms (Render, Vercel, HF Spaces).
- **Tech Stack**: Python (FastAPI, TF/PyTorch) and web frontend (React/Vanilla).

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Start with Tomato & Potato | Narrow initial scope allows for higher model accuracy and faster feedback loop | — Pending |
| Use MobileNet / lightweight CNN | Better inference speed and lower memory footprint on free tiers | — Pending |

---
*Last updated: 2026-03-20 after Phase 1 completion*
