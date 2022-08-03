import tkinter
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_FRENCH = ("Arial", 40, "italic")
FONT_ENGLISH = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
SECONDS_START = 5
french_label = ""
french_word = ""
english_label = ""
english_word = ""
vocab = {}
# Read the French Word files
vocab_table = pd.read_csv("french_words.csv")


# ----------------------------------------- count down function -----------------------------------------
def fresh_word():
    global vocab
    vocab = {pair.French: pair.English for (index, pair) in vocab_table.sample().iterrows()}
    canvas.create_image(400, 265, image=front)
    global french_label, french_word
    french_label = canvas.create_text(400, 150, text="French", font=FONT_FRENCH)
    french_word = list(vocab.keys())[0]
    print(f"french word is {french_word}")
    french_word = canvas.create_text(400, 263, text=french_word, font=FONT_WORD)
    count_down(SECONDS_START)


# ----------------------------------------- count down function -----------------------------------------
def count_down(seconds):
    print(f"{seconds} seconds remaining")
    if seconds > 0:
        root.after(1000, count_down, seconds-1)
    else:
        # flip the flash card
        canvas.delete(french_label)
        canvas.delete(french_word)
        flip()


# ----------------------------------------- flip the card -----------------------------------------
def flip():
    global vocab, english_word
    english_word = list(vocab.values())[0]
    back = tkinter.PhotoImage(file="images/card_back.png")
    canvas.create_image(400, 265, image=back)
    canvas.create_text(400, 150, text="English", font=FONT_ENGLISH)
    canvas.create_text(400, 263, text=english_word, font=FONT_WORD)


# Create window
root = tkinter.Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create canvas widget in the window, show French title and French word
canvas = tkinter.Canvas(root, width=800, height=525)
front = tkinter.PhotoImage(file="images/card_front.png")
img = canvas.create_image(400, 265, image=front)
text1 = canvas.create_text(400, 150, text="French", font=FONT_FRENCH)
text2 = canvas.create_text(400, 263, text="French Word", font=FONT_WORD)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Create button for right
r_img = tkinter.PhotoImage(file="images/right.png")
r_button = tkinter.Button(root, image=r_img, highlightthickness=0, command=fresh_word)
r_button.grid(row=1, column=1)

# Create Button for wrong
w_img = tkinter.PhotoImage(file="images/wrong.png")
w_button = tkinter.Button(root, image=w_img, highlightthickness=0)
w_button.grid(row=1, column=0)


tkinter.mainloop()
