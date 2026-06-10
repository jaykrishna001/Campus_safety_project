import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS complaints (
id INTEGER PRIMARY KEY AUTOINCREMENT,
type TEXT,
description TEXT,
location TEXT,
date TEXT,
time TEXT,
photo TEXT,
is_sos INTEGER,
severity TEXT DEFAULT 'medium',
is_priority INTEGER DEFAULT 0,
status TEXT DEFAULT 'Pending'
)
''')

# Ensure severity column exists for old databases
cur = conn.cursor()
cur.execute("PRAGMA table_info(complaints)")
columns = [row[1] for row in cur.fetchall()]
if 'severity' not in columns:
    cur.execute("ALTER TABLE complaints ADD COLUMN severity TEXT DEFAULT 'medium'")

conn.commit()
conn.close()