import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_FRENCH = ("Arial", 40, "italic")
FONT_ENGLISH = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
SECONDS_START = 5

# Read the French Word files
try:
    vocab_table = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    vocab_table = pd.read_csv("french_words.csv")
    vocab_table = vocab_table.to_dict(orient="records")
else:
    vocab_table = vocab_table.to_dict(orient="records")


# ----------------------------------------- count down function -----------------------------------------
def next_card():
    global vocab, timer
    root.after_cancel(timer)
    vocab = random.choice(vocab_table)
    canvas.itemconfig(canvas_img, image=front)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=vocab["French"])
    count_down(SECONDS_START)


# ----------------------------------------- count down function -----------------------------------------
def count_down(seconds):
    if seconds > 0:
        global timer
        root.after(1000, count_down, seconds-1)
    else:
        # flip the flash card
        canvas.itemconfig(card_title, text="")
        canvas.itemconfig(card_word, text="")
        flip()


# ----------------------------------------- flip the card -----------------------------------------
def flip():
    global vocab
    canvas.itemconfig(canvas_img, image=back)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=vocab["English"])


# ----------------------------------------- correct_button -----------------------------------------
def correct_button():
    vocab_table.remove(vocab)
    print(f"{len(vocab_table)} words left")
    next_card()


# ----------------------------------------- wrong_button -----------------------------------------
def wrong_button():
    pd.DataFrame.from_dict(vocab_table).to_csv("words_to_learn.csv")
    next_card()


# Create window
root = tkinter.Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# initialize a random word to display on window
vocab = random.choice(vocab_table)
timer = root.after(5000, func=flip)

# Create canvas widget in the window, show French title and French word
canvas = tkinter.Canvas(root, width=800, height=525)
front = tkinter.PhotoImage(file="images/card_front.png")
back = tkinter.PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 265, image=front)
card_title = canvas.create_text(400, 150, text="French", font=FONT_FRENCH)
card_word = canvas.create_text(400, 263, text=vocab["French"], font=FONT_WORD)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Create button for right
r_img = tkinter.PhotoImage(file="images/right.png")
r_button = tkinter.Button(root, image=r_img, highlightthickness=0, command=correct_button)
r_button.grid(row=1, column=1)

# Create Button for wrong
w_img = tkinter.PhotoImage(file="images/wrong.png")
w_button = tkinter.Button(root, image=w_img, highlightthickness=0, command=wrong_button)
w_button.grid(row=1, column=0)


tkinter.mainloop()
