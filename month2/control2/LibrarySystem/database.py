import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    genre TEXT,
    year INTEGER,
    pages INTEGER,
    available INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    phone TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS borrow_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    book_id INTEGER,
    borrow_date TEXT,
    return_date TEXT
)
""")

conn.commit()

def add_book(title, author, genre, year, pages):
    cursor.execute(
        "INSERT INTO books(title, author, genre, year, pages, available) VALUES(?, ?, ? ,?, ?, 1)",
        (title, author, genre, year, pages)
    )
    conn.commit()


def show_books():
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()


def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()


def add_user(name, age, phone):
    cursor.execute(
        "INSERT INTO users(name, age, phone) VALUES(?, ?, ?)",
        (name, age, phone)
    )
    conn.commit()


def show_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()