import tkinter
from ui import THEME_COLOR


class QuizBrain:

    def __init__(self, q_list):
        super().__init__()
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

        # create window for GUI
        self.root = tkinter.Tk()
        self.root.title("Quiz")
        self.root.config(padx=50, pady=50, bg=THEME_COLOR)

        # create canvas in windows
        self.canvas = tkinter.Canvas(self.root, width=500, height=500)
        self.canvas_text = self.canvas.create_text(200, 150, text="")
        self.canvas.grid(row=0, column=0, columnspan=2)

        # create true button
        self.true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_answer = "True"
        self.true_button = tkinter.Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(row=1, column=0)

        # create false button
        self.false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_answer = "False"
        self.false_button = tkinter.Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(row=1, column=1)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        q = f"Q.{self.question_number}: {self.current_question.text}"
        print(q)
        # self.check_answer(user_answer)
        self.canvas.itemconfig(self.canvas_text, text=q)

    def get_click(self):
        self.true_button.config(command=lambda: self.check_answer(self.true_answer))
        self.false_button.config(command=lambda: self.check_answer(self.false_answer))

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
