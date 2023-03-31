from flask import Flask, render_template, request
import requests

# get API url
url = "https://api.npoint.io/09e4554be7d7c58be99d"
content = requests.get(url).json()
print(content)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=content)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact_page():
    if request.method == "POST":
        data = request.form
        non_empty = bool(data)
        print(non_empty)
        feedback_msg = "Successfully sent your message"
        return render_template('contact.html', received=non_empty, feedback=feedback_msg)
    return render_template("contact.html")


@app.route("/blog/<blog_id>")
def get_blog(blog_id):
    index = int(blog_id) - 1
    blog_post = content[index]
    return render_template("post.html", post=blog_post)


if __name__ == '__main__':
    app.run(debug=True)
