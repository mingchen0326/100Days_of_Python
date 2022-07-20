from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title='Racing Bet', prompt='Please enter the color of turtle you bet on')
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y = [-70, -40, -10, 20, 50, 80]
x = [0, 0, 0, 0, 0, 0]
all_turtles = []
winner = ''

line = Turtle(shape='triangle')
line.penup()
line.goto(200, 200)
line.pendown()
line.setheading(270)
line.forward(400)

for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y[i])
    all_turtles.append(new_turtle)

run = True

while run:
    for i in range(0, 6):
        all_turtles[i].forward(random.randint(0, 10))
        x[i] = all_turtles[i].xcor()

    if max(x) > 200:
        winner = color[x.index(max(x))]
        run = False


if winner == bet:
    print('Congratulations!!! You win!!!')
else:
    print(f'You lose, the winner is {winner}')
