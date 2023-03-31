from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['POST'])
def receive_data():
    username = request.form['username']
    password = request.form['password']
    print(username)
    print(password)
    return render_template("data.html", USERNAME=username, PASSWORD=password)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

