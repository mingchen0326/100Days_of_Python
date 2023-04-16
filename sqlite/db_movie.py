from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

# with app.app_context():
#     try:
#         new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#         db.session.add(new_book)
#         db.session.commit()
#     except:
#         print("data has been created")

# Read Data
with app.app_context():
    all_books = db.session.query(Book).all()
    print(all_books)

    book = Book.query.filter_by(id=1).first()
    print(book)

# #Read A Particular Record By Query
#     book = Book.query.filter_by(title="Harry Potter").first()

# # Update Data Record By Query
# with app.app_context():
#     book_to_update = Book.query.filter_by(title="Harry Potter").first()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()

# Delete A Particular Record By PRIMARY KEY
# with app.app_context():
#     book_id = 1
#     book_to_delete = Book.query.get(book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()
