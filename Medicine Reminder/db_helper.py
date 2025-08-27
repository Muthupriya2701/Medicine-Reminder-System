import sqlite3

def connect_db():
    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        time TEXT,
        dose TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_reminder(name, time, dose):
    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reminders (name, time, dose) VALUES (?, ?, ?)", (name, time, dose))
    conn.commit()
    conn.close()

def fetch_reminders():
    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reminders")
    data = cursor.fetchall()
    conn.close()
    return data
