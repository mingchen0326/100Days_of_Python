from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def check_pass(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_position(self):
        self.penup()
        self.goto(STARTING_POSITION)
