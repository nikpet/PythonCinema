import sqlite3
import sys
from local_settings import DB_NAME, SQL_FILE

conn = sqlite3.connect(DB_NAME)

def create_table():
    with open(SQL_FILE, "r") as f:
        conn.executescript(f.read())
        conn.commit()

def main():
    create_table()

if __name__ == '__main__':
    main()
