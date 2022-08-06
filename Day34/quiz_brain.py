import tkinter
from ui import THEME_COLOR
from tkinter import messagebox
import html

FONT = ("Ariel", 20, "italic")


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
        self.canvas = tkinter.Canvas(self.root, width=350, height=350)
        self.canvas_text = self.canvas.create_text(180, 180, text="", font=FONT, width=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # create true button
        self.true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_answer = "True"
        self.true_button = tkinter.Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        # create false button
        self.false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_answer = "False"
        self.false_button = tkinter.Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        # score label
        self.score_label = tkinter.Label(self.root, text="Score: 0", bg=THEME_COLOR, fg="white",
                                         font=("Ariel", 15, "italic"))
        self.score_label.grid(row=0, column=1)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if not self.still_has_questions():
            messagebox.showinfo(title="Quiz Finished", message=f"You've completed the quiz.\nYour score was {self.score}")
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.canvas.itemconfig(self.canvas_text, text=html.unescape(self.current_question.text))
        self.canvas.configure(bg="white")


    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.canvas.configure(bg="green")
            self.score += 1
            print("You got it right!")
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.configure(bg="red")
            # time.sleep(1)
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def true_func(self):
        self.root.after(3000, self.next_question)
        self.check_answer("True")

    def false_func(self):
        self.root.after(3000, self.next_question)
        self.check_answer("False")

    def start(self):
        # self.true_button.config(command=lambda: self.check_answer(self.true_answer))
        # self.false_button.config(command=lambda: self.check_answer(self.false_answer))
        self.next_question()
        self.true_button.config(command=self.true_func)
        self.false_button.config(command=self.false_func)
