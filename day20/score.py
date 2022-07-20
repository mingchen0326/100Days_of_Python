from turtle import Turtle
FONT = ('Arial', 10, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', False, align='center', font=FONT)

