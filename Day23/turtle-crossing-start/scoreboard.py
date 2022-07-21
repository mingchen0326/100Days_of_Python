from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-200, 250)
        self.refresh()

    def refresh(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', False, align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', False, align='center', font=FONT)
