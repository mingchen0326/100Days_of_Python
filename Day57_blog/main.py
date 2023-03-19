from flask import Flask, render_template
from post import Post

app = Flask(__name__)
url = "https://api.npoint.io/1ded3246fe4b7e2d847b"
post = Post(url).get_posts()
@app.route('/')
def home():
    return render_template("index.html", posts=post)


@app.route("/blog/<blog_id>")
def get_blog(blog_id):
    index = int(blog_id) - 1
    blog_post = post[index]
    blog_title = blog_post['title']
    blog_body = blog_post['body']
    return render_template("post.html", title=blog_title, body=blog_body)


if __name__ == "__main__":
    app.run(debug=True)
