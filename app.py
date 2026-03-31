from flask import Flask, render_template, request, redirect
import sqlite3

def create_db():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            description TEXT,
            year INTEGER,
            image_url TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_db()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/author')
def author():
    return render_template('author.html')

@app.route('/library')
def library():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    conn.close()

    return render_template('library.html', books=books)

@app.route('/book/<int:book_id>')
def book(book_id):
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = c.fetchone()
    conn.close()

    return render_template('book_details.html', book=book)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    description = request.form['description']
    year = request.form['year']
    image_url = request.form['image_url']
    
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute(
        '''INSERT INTO books 
        (title, author, description, year, image_url, created_at) 
        VALUES (?, ?, ?, ?, ?, datetime("now"))''',
        (title, author, description, year, image_url)
    )
    conn.commit()
    conn.close()

    return redirect("/library")  

@app.route('/delete_book/<int:id>')
def delete_book(id):
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return redirect("/library")

if __name__ == "__main__":
    app.run(debug=True)