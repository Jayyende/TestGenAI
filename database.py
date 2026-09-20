import sqlite3


def init_db():

    conn = sqlite3.connect("testgenai.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        functions_count INTEGER,

        quality_score INTEGER,

        risk_level TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()
    conn.close()


def save_analysis(
        filename,
        functions_count,
        quality_score,
        risk_level):

    conn = sqlite3.connect("testgenai.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO analysis_history
    (
        filename,
        functions_count,
        quality_score,
        risk_level
    )
    VALUES (?,?,?,?)
    """,
    (
        filename,
        functions_count,
        quality_score,
        risk_level
    ))

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect("testgenai.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM analysis_history
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data