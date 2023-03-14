from flask import Flask

app = Flask(__name__)


def emphasize(func):
    def decor():
        return f"<em>{func()}</em>"
    return decor


def underline(func):
    def decor():
        return f"<u>{func()}</u>"
    return decor


def bold(func):
    def decor():
        return f"<b>{func()}</b>"
    return decor


@app.route("/")
@bold
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<number>")
def guess_number(number):
    target = 6
    number = int(number)
    if number < target:
        return "<h1 style='color: red'>Too low, try again</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > target:
        return "<h1 style='color: purple'>Too high, try again</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


# run the code
if __name__ == '__main__':
    app.run(debug=True)


