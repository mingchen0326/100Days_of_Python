from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)

all_books = []

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

with app.app_context():
    db.create_all()
    books = db.session.execute(db.select(Book)).scalars()

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.form:
        book = {'book_name': request.form['book_name'],
                'book_author': request.form['book_author'],
                'book_rating': request.form['book_rating']}
        new_book = Book(title=book['book_name'], author=book['book_author'], rating=book['book_rating'])
        db.session.add(new_book)
        db.session.commit()

        # message = f"{book['book_name']} - {book['book_author']} - {book['book_rating']}/10"
        # all_books = Book.query.all()
        # print(all_books)
        # all_books.append(book)
        # return render_template('index.html', bookshelf=all_books)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

