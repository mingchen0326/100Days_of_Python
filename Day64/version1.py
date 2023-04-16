from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from movie_class import Movie
from functions import get_movie
from form_class import EditForm, AddForm

import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie_list_v1.db"
db = SQLAlchemy(app)
Bootstrap(app)


# Create table for database
with app.app_context():
    db.create_all()

# Add data and check if data exist
    try:
        new_movie = Movie(
            id=1,
            title="Phone Booth",
            year=2002,
            description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
            rating=7.3,
            ranking=10,
            review="My favourite character was the caller.",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")
        db.session.add(new_movie)
        db.session.commit()
    except:
        print("data has been created")


# set up home web page
@app.route("/")
def home():
    with app.app_context():
        if not db.session.query(Movie).all():
            first_movie = Movie.query.filter_by(title="Phone Booth").first()
            return render_template("index.html", movie=first_movie, has_movie=True)
    return render_template("index.html", has_movie=False)


# page to add new movies
@app.route("/add")
def add():
    # create form object pass to add.html to add new movie
    form = AddForm()
    if form.validate_on_submit():
        # extract the data from form entry
        added_movie_title = request.form.get('movie_title')
        added_movie = get_movie(added_movie_title)
        print(added_movie["original_title"])
        print(f"the new movie title is {added_movie_title}")
    return render_template("add.html", form=form)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    # create form to edit selected movie
    form = EditForm()
    if form.validate_on_submit():
        # extract the data from form entry
        new_rating = request.form.get('movie_rating')
        new_review = request.form.get('movie_review')

        # update movie rating and review
        movie_to_update = Movie.query.filter_by(title="Phone Booth").first()
        movie_to_update.rating = new_rating
        movie_to_update.review = new_review
        db.session.commit()

        print(new_rating, new_review)
        return redirect(url_for('home'))  # redirect to home page

    return render_template("edit.html", form=form)

@app.route("/delete/<title>", methods=['GET', 'POST'])
def delete(title):
    with app.app_context():
        all_movies = db.session.query(Movie).all()
        print(all_movies)

    print(f"The movie title is {title}")
    with app.app_context():
        movie_to_delete = Movie.query.filter_by(title="Phone Booth").first()
        db.session.delete(movie_to_delete)
        db.session.commit()

    with app.app_context():
        all_movies = db.session.query(Movie).all()
        print(all_movies)
    return redirect(url_for('home'))  # redirect to home page

if __name__ == '__main__':
    app.run(debug=True)
