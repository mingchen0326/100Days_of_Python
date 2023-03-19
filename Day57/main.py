from flask import Flask, render_template
import datetime
import requests


# create server and home page
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess/<name>")
def age_gender(name):
    # Connect Agify.io and Genderize.io API, get age and gender
    age = requests.get(f"https://api.agify.io?name={name}").json()['age']
    gender = requests.get(f"https://api.genderize.io?name={name}").json()['gender']
    current_year = datetime.date.today().year
    return render_template("guess.html", year=current_year, person=name, age=age, gender=gender)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    return render_template("Blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)