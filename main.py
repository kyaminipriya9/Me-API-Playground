from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import sqlite3
import logging
from database import init_db, get_conn
from models import Profile, Skill, Project, Work, Link

# -------------------- Init --------------------
init_db()
app = FastAPI(title="Me-API Playground")

# -------------------- Logging --------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -------------------- CORS --------------------
origins = ["*"]  # allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- Root --------------------
@app.get("/")
def root():
    return {"message": "Welcome to Me-API Playground"}

# -------------------- Health --------------------
@app.get("/health")
def health():
    return {"status": "OK"}

# -------------------- Profile --------------------
@app.get("/profile", response_model=Profile)
def get_profile():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM profile WHERE id=1")
    row = cur.fetchone()
    conn.close()
    if row:
        logger.info("Fetched profile")
        return Profile(id=row[0], name=row[1], email=row[2], education=row[3], mobile=row[4], address=row[5])
    raise HTTPException(status_code=404, detail="Profile not found")

# -------------------- Skills --------------------
@app.get("/skills", response_model=List[Skill])
def get_skills():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, skill FROM skills WHERE profile_id=1")
    rows = cur.fetchall()
    conn.close()
    logger.info(f"Fetched {len(rows)} skills")
    return [Skill(id=r[0], skill=r[1]) for r in rows]

@app.get("/skills/top", response_model=List[Skill])
def top_skills(limit: int = 5):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, skill FROM skills WHERE profile_id=1 LIMIT ?", (limit,))
    rows = cur.fetchall()
    conn.close()
    logger.info(f"Fetched top {len(rows)} skills")
    return [Skill(id=r[0], skill=r[1]) for r in rows]

# -------------------- Projects --------------------
@app.get("/projects", response_model=List[Project])
def get_projects(skill: str = Query(None)):
    conn = get_conn()
    cur = conn.cursor()
    if skill:
        logger.info(f"Filtering projects by skill: {skill}")
        cur.execute(
            "SELECT id, title, description, link FROM projects WHERE profile_id=1 AND (title LIKE ? OR description LIKE ?)",
            (f"%{skill}%", f"%{skill}%")
        )
    else:
        logger.info("Fetching all projects")
        cur.execute("SELECT id, title, description, link FROM projects WHERE profile_id=1")
    rows = cur.fetchall()
    conn.close()
    return [Project(id=r[0], title=r[1], description=r[2], link=r[3]) for r in rows]

# -------------------- Work --------------------
@app.get("/work", response_model=List[Work])
def get_work():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM work WHERE profile_id=1")
    rows = cur.fetchall()
    conn.close()
    logger.info(f"Fetched {len(rows)} work entries")
    return [Work(id=r[0], company=r[2], role=r[3], start_date=r[4], end_date=r[5], description=r[6]) for r in rows]

# -------------------- Links --------------------
@app.get("/links", response_model=List[Link])
def get_links():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM links WHERE profile_id=1")
    rows = cur.fetchall()
    conn.close()
    logger.info(f"Fetched {len(rows)} links")
    return [Link(id=r[0], type=r[2], url=r[3]) for r in rows]

# -------------------- Search --------------------
@app.get("/search")
def search(q: str, limit: int = 10):
    conn = get_conn()
    cur = conn.cursor()
    logger.info(f"Searching for query: {q}")
    # Search in projects (title + description)
    cur.execute(
        "SELECT title, description FROM projects WHERE title LIKE ? OR description LIKE ? LIMIT ?",
        (f"%{q}%", f"%{q}%", limit)
    )
    projects = [{"title": r[0], "description": r[1]} for r in cur.fetchall()]
    # Search in skills
    cur.execute("SELECT skill FROM skills WHERE skill LIKE ? LIMIT ?", (f"%{q}%", limit))
    skills = [r[0] for r in cur.fetchall()]
    conn.close()
    return {"projects": projects, "skills": skills}
