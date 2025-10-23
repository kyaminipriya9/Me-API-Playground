# Me-API Playground

A simple full-stack project to showcase personal profile, skills, projects, links, and work experience using a FastAPI backend and a static frontend.

## Live Demo

| Component  | URL |
|-----------|-----|
| **Frontend (GitHub Pages)** | https://kyaminipriya9.github.io/Me-API-Playground/ |
| **Backend (Render)**        | https://me-api-playground-as54.onrender.com |

## Features

- View personal profile information
- Display links (GitHub, LinkedIn, Portfolio.)
- Interactive skills filter
- List of projects with links
- Work experience section
- Lightweight frontend using HTML, CSS, JavaScript
- REST API built with FastAPI + SQLite

## Tech Stack

| Part     | Technology |
|----------|------------|
| Backend  | FastAPI, Python, SQLite |
| Frontend | HTML, CSS, JavaScript |
| Hosting  | Render (Backend), GitHub Pages (Frontend) |

## Project Structure
Me-API-Playground/
├── backend/
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ └── requirements.txt
│── index.html
│── style.css
│── script.js
└── README.md

## Installation (Local Setup)

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Frontend
Just open index.html in your browser or serve with VS Code Live Server.


