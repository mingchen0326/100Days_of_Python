from flask import Flask, render_template, request
import sqlite3

# create server
app = Flask(__name__)

# create empty bookshelf
all_books = []

# ------------------------------------------ Create Table -------------------------------------#
# create database and cursor
conn = sqlite3.connect("./instance/book_shelf.db", check_same_thread=False)
c = conn.cursor()

# Check if table has been created
try:
    c.execute("""CREATE TABLE books(
        book_title text,
        book_author text,
        book_rating text
        )""")
except sqlite3.OperationalError:
    pass


@app.route('/')
def home():
    # ------------------------------------------ Read Data ----------------------------------
    all_books = c.execute("SELECT * FROM books")

    # Commit our command
    conn.commit()
    return render_template('index.html', bookshelf=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.form:
        book = {'book_name': request.form['book_name'],
                'book_author': request.form['book_author'],
                'book_rating': request.form['book_rating']}

        # ------------------------------ Add single data and add many data ----------------------
        c.execute(f"INSERT INTO books VALUES ('{book['book_name']}', '{book['book_author']}', '{book['book_rating']}')")

        # ------------------------------------------ Read Data ----------------------------------
        all_books = c.execute("SELECT * FROM books")

        # Commit our command
        conn.commit()
        return render_template('index.html', bookshelf=all_books)
    return render_template('add.html')

# # Close our connection
# conn.close()


if __name__ == "__main__":
    app.run(debug=True)

