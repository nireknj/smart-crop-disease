---
wave: 1
depends_on: []
files_modified: []
autonomous: true
---

# Phase 3: Web Frontend & Integration

## Objective
Build a React application that integrates with the backend API to provide a seamless user experience for farmers uploading crop images for disease detection.

## Requirements Addressed
- UIUX-01
- UIUX-02
- UIUX-03
- UIUX-04
- UIUX-05

## Must Haves
- The frontend MUST run locally via `npm run dev`.
- The application MUST integrate with the FastAPI backend running on port 8000.
- A user MUST be able to register, login, upload an image, and see the results.
- A user MUST be able to view their scan history.

## Tasks

<task>
<description>
Initialize Vite React App and TailwindCSS.
</description>
<read_first>
- .planning/phases/03-web-frontend-integration/03-RESEARCH.md
</read_first>
<action>
1. Run `npx -y create-vite frontend --template react` in the project root to initialize the `frontend` directory.
2. Navigate into `frontend` and run `npm install`.
3. Run `npm install react-router-dom axios lucide-react`.
4. Run `npm install -D tailwindcss postcss autoprefixer`, then `npx tailwindcss init -p`.
5. Configure `frontend/tailwind.config.js` to scan `./src/**/*.{js,jsx,ts,tsx}`.
6. Replace `frontend/src/index.css` content with Tailwind `@tailwind` directives.
</action>
<acceptance_criteria>
- `frontend` directory exists with a Vite project structure.
- `tailwind.config.js` is properly configured.
- `index.css` contains `@tailwind` directives.
</acceptance_criteria>
</task>

<task>
<description>
Implement context, routing, and basic layout.
</description>
<read_first>
- .planning/phases/03-web-frontend-integration/03-UI-SPEC.md
</read_first>
<action>
1. In `frontend/src`, create folder `context` and `AuthContext.jsx` to manage JWT token storage in localStorage and provide login/logout functions.
2. In `frontend/src`, create folder `api` and `client.js` with an Axios instance pre-configured with `baseURL: 'http://localhost:8000'` and a request interceptor that attaches the Bearer token.
3. In `frontend/src`, setup `App.jsx` with React Router setting up routes: `/login`, `/register`, and protected routes for `/` (Dashboard) and `/history`.
4. In `frontend/src/components`, build a `Navbar.jsx` component that shows login/logout status and navigation links. Update styling per UI spec with green themes.
</action>
<acceptance_criteria>
- `AuthContext.jsx` manages `token` state.
- `client.js` attaches JWT reliably.
- `App.jsx` handles core routing.
</acceptance_criteria>
</task>

<task>
<description>
Implement Authentication screens.
</description>
<read_first>
- .planning/phases/03-web-frontend-integration/03-UI-SPEC.md
</read_first>
<action>
1. In `frontend/src/pages`, create `Login.jsx` with an email/password form. Post to `/api/auth/login`. On success, set token via context and redirect to dashboard.
2. In `frontend/src/pages`, create `Register.jsx` with a registration form. Post to `/api/auth/register`. On success, redirect to login page.
</action>
<acceptance_criteria>
- Users can log in and register through the UI. Forms have basic styling and error handling.
</acceptance_criteria>
</task>

<task>
<description>
Implement Dashboard, scanning interface, and history.
</description>
<read_first>
- .planning/phases/03-web-frontend-integration/03-UI-SPEC.md
</read_first>
<action>
1. In `frontend/src/pages`, create `Dashboard.jsx`. Create a large UI component for selecting/uploading a crop leaf photo (using an HTML file input hidden behind a styled button or dropzone).
2. When selected and "Analyze" is clicked, submit it via Axios as `FormData` to `/api/predict`. Show a loading spinner during the payload request.
3. Create a `ResultsCard.jsx` component inside `frontend/src/components` to display the backend results (Disease, Confidence as percentage, Remedy text) cleanly.
4. In `frontend/src/pages`, create `History.jsx`. On mount, fetch data from `/api/history` and display a list/grid of previous scans.
</action>
<acceptance_criteria>
- Users can select and upload images to the prediction endpoint.
- Results are displayed faithfully based on the API response.
- History page lists all previously scanned results visually.
</acceptance_criteria>
</task>
