from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Create Table
connect = sqlite3.connect("./instance/movie_list.db", check_same_thread=False).cursor()


new_movie = {'title': "Phone Booth",
             'year': 2002,
             'description': "Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
             'rating': 7.3,
             'ranking': 10,
             'review': "My favourite character was the caller.",
             'img_url': "https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"}


# Create form class for edit movie
class EditForm(FlaskForm):
    movie_rating = StringField(label='movie_rating', validators=[DataRequired()], render_kw={"style": "width: 200px;"})
    movie_review = StringField(label='movie_review', validators=[DataRequired()], render_kw={"style": "width: 200px;"})
    edit_submit = SubmitField(label='Done')


class AddForm(FlaskForm):
    movie_title = StringField(label='movie_rating', validators=[DataRequired()], render_kw={"style": "width: 200px;"})
    add_submit = SubmitField(label='Add Movie')


# Check if table has been created
try:
    connect.execute("""CREATE TABLE movie(
        title text,
        year text,
        description text,
        rating text,
        ranking integer,
        review text,
        img_url text,
        )""")

except sqlite3.OperationalError:
    print("the table is already exist")


@app.route("/")
def home():
    # add movie to the database
    # connect.execute(
    #     """INSERT INTO movie (id, title, year, description, rating, ranking, review, img_url)
    # VALUES(:id, :title, :year, :description, :rating, :ranking, :review, :img_url);""", new_movie)
    connect.execute("INSERT INTO movie VALUES (?, ?, ?, ?, ?, ?, ? )", (new_movie['title'], new_movie['year'], new_movie['description'], new_movie['rating'], new_movie['ranking'], new_movie['review'], new_movie['img_url']))
    print(connect.fetchone())
    return render_template("index.html", movie=new_movie)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditForm()
    if form.validate_on_submit():
        # extract the data from form entry
        new_rating = request.form.get('movie_rating')
        new_review = request.form.get('movie_review')
        # connect.execute(f""" UPDATE movie SET rating = {new_rating}, review = {new_review} WHERE title = 'Phone Booth' """)
        # connect.execute(f""" UPDATE movie SET rating = {new_rating}, review = (?) WHERE title = 'Phone Booth' """, (new_review))
        connect.execute(f""" UPDATE movie SET rating = {new_rating} WHERE racking = 10 """)
        print(new_rating, new_review)
        return redirect(url_for('home'))  # redirect to home page

    return render_template("edit.html", form=form)





if __name__ == '__main__':
    app.run(debug=True)
