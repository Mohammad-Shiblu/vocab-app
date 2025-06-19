import sqlite3

DB_NAME = 'vocab.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    with get_connection() as conn:
        conn.execute("Create Table if Not Exists words (word Text, meaning Text)")

def save_word(word, meaning):
    with get_connection() as conn:
        try:
            conn.execute('INSERT INTO words (word, meaning) VALUES (?, ?)', (word, meaning))
            conn.commit()
        except sqlite3.IntegrityError:
            print(f"Word '{word}' already exists in the database.")

def get_all_words():
    with get_connection() as conn:
        cursor = conn.execute('SELECT * FROM words')
        return cursor.fetchall()

create_table()