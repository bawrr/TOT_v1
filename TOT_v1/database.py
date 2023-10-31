import sqlite3
import csv

DATABASE_NAME = 'trick_or_treaters.db'

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trick_or_treaters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT DEFAULT 'Anonymous',  -- Default to 'Anonymous' if name is not provided
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_trick_or_treater(name=None):  # Allow name to be None
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO trick_or_treaters (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

def export_data_to_csv():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM trick_or_treaters')
    rows = cursor.fetchall()
    conn.close()
    with open('trick_or_treaters.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Name', 'Timestamp'])
        writer.writerows(rows)

def reset_data():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM trick_or_treaters')
    conn.commit()
    conn.close()

def get_trick_or_treater_count():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM trick_or_treaters')
    count = cursor.fetchone()[0]
    conn.close()
    return count