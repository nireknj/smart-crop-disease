# Phase 3 UI Spec

## Concept & Layout
The frontend will be a React application created with Vite + TailwindCSS.
The application will have a minimalist, mobile-first design, given the target audience consists of farmers who likely access this via smartphones.
Regional language support (Hindi/Marathi) is planned but currently we will structure the app to easily support i18n in the future.

### Key Screens

1. **Landing/Auth Page:**
   - Hero section explaining the app.
   - Login and Registration forms.
   
2. **Dashboard (Main App Area):**
   - Header with Logo, Navigation (Scan, History, Profile).
   - "New Scan" Floating Action Button or prominent central area.
   
3. **Scan Interface:**
   - Image upload zone (tap to select camera or file).
   - Once selected, show a preview.
   - "Analyze" button.
   - **Results Card:**
     - Disease Name & Confidence Score.
     - Remedy suggestions clearly laid out.

4. **History Loop:**
   - List of previous scans with small thumbnails, dates, and disease names.

## Styles & Interactions
- **Color Palette:** Green hues (indicative of agriculture/plants), off-white backgrounds, dark grey text for readability.
- **Typography:** Inter or system default sans-serif, large tap targets.
- **Animations:** Subtle fade-ins when switching tabs or showing results.
- **Upload Interaction:** Show a spinner while awaiting the backend API response.
