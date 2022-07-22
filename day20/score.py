from turtle import Turtle
FONT = ('Arial', 10, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        with open("data.txt") as data:
            self.high_score = int(data.read())
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
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)
