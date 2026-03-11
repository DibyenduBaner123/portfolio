import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            completion_percent REAL,
            budget_variance REAL,
            risk_score REAL,
            risk_level TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_record(data, risk_result):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO project_history 
        (completion_percent, budget_variance, risk_score, risk_level)
        VALUES (?, ?, ?, ?)
    """, (
        data["completion_percent"],
        data["budget_variance"],
        risk_result["risk_score"],
        risk_result["risk_level"]
    ))
    conn.commit()
    conn.close()
    
def fetch_all_records():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM project_history ORDER BY id DESC")
    records = cursor.fetchall()

    conn.close()
    return records