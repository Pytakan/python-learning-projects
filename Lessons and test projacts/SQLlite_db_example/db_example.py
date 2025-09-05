import sqlite3
from sqlite3 import Error
from pathlib import Path

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

db_path = Path(__file__).resolve().parent / "pythonsqlite.db"
# print(create_connection(db_path))

# with create_connection(db_path) as conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, name text NOT NULL, age integer);"""
#     conn.execute(sql_request)

# users = [
#     (1, 'Alice', 30),
#     (2, 'Bob', 25),
#     (3, 'Charlie', 35),
#     (4, 'Diana', 28),
#     (5, 'Ethan', 40),
#     (6, 'Fiona', 22)

# ]

# with create_connection(db_path) as conn:
#     sql_request = """INSERT INTO users (id, name, age) VALUES (?, ?, ?);"""
#     conn.executemany(sql_request, users)
#     conn.commit()

with create_connection(db_path) as conn:
    sql_request = """SELECT * FROM users WHERE age > ?;"""
    cursor = conn.execute(sql_request, (23,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)