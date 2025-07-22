import sqlite3

def get_db_connection():
    try:
        conn = sqlite3.connect('users.db', check_same_thread=False)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"[DB ERROR] {e}")
        return None, None

conn, cursor = get_db_connection()
