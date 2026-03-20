# Phase 3: Web Frontend & Integration - Research

## Technical Approach
- **Framework:** React + Vite (Standard JS for simplicity unless TypeScript is preferred).
- **Styling:** TailwindCSS for utility-first responsive design mapping closely to the UI-SPEC constraints.
- **Routing:** React Router v6 for navigation (Auth, Dashboard, Scan, History).
- **State/Auth Management:** React Context API for localized state mapping. We will store the JWT in `localStorage`.
- **API Client:** Axios or native `fetch` to interact with the FastAPI backend created in Phases 1 & 2.

## Key Dependencies to Install
- `react`, `react-dom`
- `react-router-dom`
- `axios`
- `tailwindcss`, `postcss`, `autoprefixer`
- `lucide-react` (for icons)
