import turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

r_score = Score((30, 220))
l_score = Score((-30, 220))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.vertical_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.distance(r_paddle) > 50 and ball.xcor() > 350:
        r_score.refresh()
        ball.reset()
    elif ball.distance(l_paddle) > 50 and ball.xcor() < -350:
        l_score.refresh()
        ball.reset()

screen.exitonclick()




