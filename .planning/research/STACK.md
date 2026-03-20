# Stack Research

**Domain:** Crop Disease Detection Web App
**Researched:** 2026-03-20
**Confidence:** HIGH

## Recommended Stack

### Core Technologies

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| FastAPI (Python)  | 0.100+ | Backend API & Model Serving | Extremely fast, great for async ML inference, built-in validation. |
| TensorFlow / Keras | 2.15+ | ML Model Training & Inference | Support for MobileNetV2/V3 which are lightweight and perfect for this. |
| React | 18+ | Frontend Web UI | Component-based, easy to build PWA for low-end devices. |
| SQLite (dev) / PostgreSQL (prod) | - | Database | Simple user and inference history storage. |

### Supporting Libraries

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| Pillow (PIL) | 10+ | Image Processing | Preprocessing images before feeding to model. |
| SQLAlchemy | 2.0+ | ORM | Database interactions. |
| python-jose / passlib | latest | Authentication | JWT based auth for secure logins. |
| Tailwind CSS | 3+ | Styling UI | Fast styling for clean minimal interfaces without heavy CSS files. |

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| FastAPI | Flask | If the team only knows Flask, but FastAPI is much better for async ML. |
| TensorFlow | PyTorch | PyTorch is great for research, but TF/TFLite is often easier for production/mobile deployment. |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| Heavy frameworks like Django | Unnecessary overhead for a simple inference API. | FastAPI |
| VGG16 / ResNet50 models | Too heavy, slow inference on free servers. | MobileNetV2/V3 |
