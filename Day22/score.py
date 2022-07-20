from turtle import Turtle
Font = ("Arial", 30, "bold")


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(position)
        self.refresh()

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f'{self.score}', False, align='center', font=Font)
