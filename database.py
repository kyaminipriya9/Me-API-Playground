import sqlite3

DB_NAME = "me_api.db"

def get_conn():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    
    # Create tables
    cur.execute("""
    CREATE TABLE IF NOT EXISTS profile (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        education TEXT,
        mobile TEXT,
        address TEXT
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY,
        profile_id INTEGER,
        skill TEXT,
        FOREIGN KEY(profile_id) REFERENCES profile(id)
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY,
        profile_id INTEGER,
        title TEXT,
        description TEXT,
        link TEXT,
        FOREIGN KEY(profile_id) REFERENCES profile(id)
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS work (
        id INTEGER PRIMARY KEY,
        profile_id INTEGER,
        company TEXT,
        role TEXT,
        start_date TEXT,
        end_date TEXT,
        description TEXT,
        FOREIGN KEY(profile_id) REFERENCES profile(id)
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS links (
        id INTEGER PRIMARY KEY,
        profile_id INTEGER,
        type TEXT,
        url TEXT,
        FOREIGN KEY(profile_id) REFERENCES profile(id)
    )""")
    
    # Seed profile data
    cur.execute("SELECT COUNT(*) FROM profile")
    if cur.fetchone()[0] == 0:
        cur.execute("""
        INSERT INTO profile (id, name, email, education, mobile, address)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (1, "K. Yamini Priya", "k.priya.22033@iitgoa.ac.in",
              "BTech, Mathematics and Computing, IIT Goa, CGPA 7.75/10", 
              "+91 7893016228", "4-195, Balaji Nagar Colony, Greamspet, Chittoor, AP"))
        
        # Skills
        skills = ["C", "C++", "Python", "Javascript", "HTML", "CSS", "MySQL", 
                  "Git", "GitHub", "Linux", "LaTeX", "MS Office", 
                  "Pandas", "NumPy", "Matplotlib", "scikit-learn", 
                  "DSA", "Algorithm Design", "ML", "Optimization Theory", 
                  "Probability & Statistics", "Linear Algebra"]
        cur.executemany("INSERT INTO skills (profile_id, skill) VALUES (?,?)", [(1,s) for s in skills])
        
        # Projects
        projects = [
            ("IMDB Movie Dataset Analysis", 
             "Explored and visualized IMDB movie data to identify trends in ratings and genres. TechStack: Python, Pandas, Matplotlib",
             "https://github.com/kyaminipriya9/kyaminipriya9.github.io/blob/main/Project_EDIGLOBE.ipynb"),
            ("Predicting Heart Disease Risk", 
             "Predicted 10-year coronary heart disease risk using Framingham dataset. TechStack: Python, scikit-learn, Pandas",
             "https://github.com/kyaminipriya9/kyaminipriya9.github.io/blob/main/ML-MAJOR-FEBRUARY.ipynb"),
            ("Application of Linear Algebra in PCA",
             "Applied PCA using eigen decomposition on Iris dataset. TechStack: Python, NumPy, Matplotlib",
             "https://drive.google.com/file/d/1kDPHfgzt9OmaLYM2nlGbf2l7vzOHuLli/view?usp=sharing")
        ]
        cur.executemany("INSERT INTO projects (profile_id, title, description, link) VALUES (?,?,?,?)", [(1,*p) for p in projects])
        
        # Work experience
        work = [
            ("Ediglobe (Online)", "Intern", "2024-02-01", "2024-03-31", 
             "Completed a 2-month ML course and internship, worked on projects applying ML techniques.")
        ]
        cur.executemany("INSERT INTO work (profile_id, company, role, start_date, end_date, description) VALUES (?,?,?,?,?,?)", [(1,*w) for w in work])
        
        # Links
        links = [
            ("Github", "https://github.com/kyaminipriya9"),
            ("Linkedin", "https://www.linkedin.com/in/yamini-priya-k-404b76259/"),
            ("Portfolio", "https://kyaminipriya9.github.io/My_Portfolio/")
        ]
        cur.executemany("INSERT INTO links (profile_id, type, url) VALUES (?,?,?)", [(1,*l) for l in links])
    
    conn.commit()
    conn.close()
