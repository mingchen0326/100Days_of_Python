from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
# from movie_class import Movie
from functions import search_movie, get_movie
from form_class import EditForm, AddForm
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie_list_v1.db"
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, primary_key=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# Create table for database
with app.app_context():
    db.create_all()


# set up home web page
@app.route("/")
def home():
    with app.app_context():
        all_movies = db.session.query(Movie).all()
        db.session.commit()
        if len(all_movies) > 0:
            ordered_movie = Movie.query.order_by(desc(Movie.rating))
            rank = 1
            for item in ordered_movie:
                item.ranking = rank
                rank += 1
            return render_template("index.html", movies=ordered_movie, has_movie=True)
    return render_template("index.html", has_movie=False)


@app.route("/update/<add_id>")
def update(add_id):
    if add_id:
        movie_to_add = get_movie(add_id)
        print(movie_to_add)
        with app.app_context():
            try:
                db.session.add(movie_to_add)
                db.session.commit()
            except:
                print("the movie is already in the database")
        return home()


# page to add new movies
@app.route("/add", methods=['GET', 'POST'])
def add():
    # create form object pass to add.html to add new movie
    form = AddForm()
    if form.validate_on_submit():
        # extract the data from form entry
        added_movie_title = request.form.get('movie_title')
        search_result = search_movie(added_movie_title)
        print(f"the new movie title is {added_movie_title}")
        return render_template("add.html", search=search_result)
    return render_template("add.html", form=form)


title_list = []
@app.route("/edit", methods=['GET', 'POST'])
def edit():
    # title will be None once user submit new review, so index 0 is to keep the movie title
    title_list.append(request.args.get("title"))
    title = title_list[0]

    with app.app_context():
        # create form to edit selected movie
        form = EditForm()
        if form.validate_on_submit():
            # get the data from form entry
            new_rating = request.form.get('movie_rating')
            new_review = request.form.get('movie_review')

            # update movie rating and review
            movie_to_update = Movie.query.filter_by(title=title).first()
            movie_to_update.rating = new_rating
            movie_to_update.review = new_review
            db.session.commit()

            return home()  # redirect to home page

    return render_template("edit.html", form=form, movie_title=title)


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
