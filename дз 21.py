import sqlite3

conn = sqlite3.connect("books.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)")
cur.execute("INSERT INTO books VALUES (1, 'Harry Potter', 'Rowling')")
cur.execute("INSERT INTO books VALUES (2, '1984', 'Orwell')")
cur.execute("INSERT INTO books VALUES (3, 'Hobbit', 'Tolkien')")

conn.commit()

for x in cur.execute("SELECT * FROM books"):
    print(x)
cur.execute("DELETE FROM books WHERE id = 2")
conn.commit()

for x in cur.execute("SELECT * FROM books"):
    print(x)
conn.close()