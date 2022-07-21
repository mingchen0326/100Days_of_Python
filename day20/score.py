from turtle import Turtle
FONT = ('Arial', 10, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, align='center', font=FONT)

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)
