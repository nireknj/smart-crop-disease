# Pitfalls Research

**Domain:** Crop Disease Detection Web App
**Researched:** 2026-03-20
**Confidence:** HIGH

## Common Mistakes

### 1. Uncompressed Image Uploads
- **Warning Sign:** API times out, users complain about data usage.
- **Prevention:** Compress images on the client side (Canvas API) before sending.
- **Phase to Address:** Frontend / API definitions.

### 2. Over-confident False Positives
- **Warning Sign:** Model predicts "Healthy" on a picture of a dog or a foot.
- **Prevention:** Add a "Not a Leaf" confidence threshold or a preliminary binary classifier (Leaf vs Non-Leaf). Alternatively, threshold the confidence strictly (e.g., if < 60%, return "Unsure").
- **Phase to Address:** ML Pipeline / Backend Logic.

### 3. Heavy Server-Side Models
- **Warning Sign:** Server runs out of memory on Render free tier (usually 512MB RAM).
- **Prevention:** Use MobileNet. Export as TFLite or ONNX to reduce memory footprint. Load model once at startup, not per request.
- **Phase to Address:** ML Pipeline.

### 4. Zero Offline Capability
- **Warning Sign:** Farmers can't use it in the middle of a field.
- **Prevention:** Implement basic Service Workers (PWA) so the UI loads. (Inference still requires network unless run via TF.js on client, but for now network inference is expected).
- **Phase to Address:** Frontend UI.
