"""
Concerned with storing and retrieving books from a list.
"""
from .database_connection import Database_Connection


def create_book_table():
    with Database_Connection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

def book_adder(book_name, author):
    with Database_Connection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?,0)', (book_name, author))


def book_displayer():
    with Database_Connection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': 'No' if row[2] == 0 else 'Yes'} for row in cursor.fetchall()]


    if books[0]['read'] == "No":
        return (f"{books[0]['name']} by {books[0]['author']}. You haven't read this book.")
    else:
        return (f"{books[0]['name']} by {books[0]['author']}. You have read this book.")

def book_marker(name):
    with Database_Connection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))



def book_deleter(delete_this_book):
    with Database_Connection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?',(delete_this_book,))








