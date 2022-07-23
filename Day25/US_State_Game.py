import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
FONT = ('Arial', 10, 'bold')
data = pd.read_csv("50_states.csv")


guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another states name?").title()

    if answer_state in data["state"].values:
        guessed_states.append(answer_state)
        row = data[data["state"] == answer_state]
        coor = row[["x", "y"]].values[0]
        display = turtle.Turtle()
        display.hideturtle()
        display.penup()
        display.goto(coor[0], coor[1])
        display.write(answer_state, align="center", font=FONT)
        data.drop(data[data["state"] == answer_state].index, inplace=True)
        print("there are {} states left".format(len(data)))
    elif answer_state == "Quit":
        data["state"].to_csv("missing_states.csv")
        break


turtle.mainloop()

# ------------------------- the following code shows how to get coordinate from the click--------------------------
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
