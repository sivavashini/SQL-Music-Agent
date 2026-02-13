import sqlite3

def get_connection():
    conn = sqlite3.connect("dataset/Chinook_Sqlite.sqlite")
    return conn
