from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto((0, 0))
        self.moving_distanceX = 10
        self.moving_distanceY = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.moving_distanceX
        new_y = self.ycor() + self.moving_distanceY
        self.goto(new_x, new_y)

    def vertical_bounce(self):
        self.moving_distanceY *= -1

    def paddle_bounce(self):
        self.moving_distanceX *= -1

    def reset(self):
        self.goto((0, 0))
        self.paddle_bounce()


