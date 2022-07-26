from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I Am a Label", font=("Arial,", 24))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# button
def button_clicked():
    print("I got clicked")
    new_text = Input.get()
    my_label.config(text=new_text)


# Entry
Input = Entry(width=10)
Input.pack()


button = Button(text="Click Me", command=button_clicked)
button.pack()





window.mainloop()