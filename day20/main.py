import turtle
import time
from snake import Snake
from food import Food
from score import Score

"""This python file is designing the snake game, written by Ming Chen"""

screen = turtle.Screen()
screen.setup(width=600, height=600)    # the origin coordinate is in the middle, so the range of x and y are [-300, 300]
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.update()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_high_score()
        snake.reset_snake()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset_high_score()
            snake.reset_snake()







screen.exitonclick()
