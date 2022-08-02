"""This .py file contains extra code using different methods to achieve same feature."""

import string
import tkinter
import random
from tkinter import messagebox

"""Build a password manager"""


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    symbol = list("~!@#$%^&*?")
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    number = list("0123456789")
    selection = [symbol, uppercase, lowercase, number]
    has_all_type = [False, False, False, False]
    password_len = 12
    code = []

    for i in range(password_len):
        if (password_len - i) <= 4 and not all(has_all_type):
            index = has_all_type.index(False)
            unused_list = selection[index]
            random_character = random.choice(unused_list)
            code.append(random_character)
            i = i + 1
            continue
        random_index = random.randint(0, 3)
        has_all_type[random_index] = True
        character = random.choice(selection[random_index])
        code.append(character)

    p = "".join(code)

    window.clipboard_clear()
    window.clipboard_append(p)
    window.update()

    return p


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    # get the text content from website and username entry box
    website = entry_website.get()
    username = entry_username.get()

    # check empty input
    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Blank Input", message="Entry cannot be empty")
        # -------------------------------the following code is to create the message box using canvas-------------------
        # blank_top = tkinter.Toplevel(window)
        # blank_top.geometry("300x300")
        # blank_top.title("Empty Blank")
        #
        # blank_message = tkinter.Label(blank_top, text="Entry cannot be empty")
        # blank_message.grid(row=1, column=1)
        #
        # def exit_blank_top():
        #     blank_top.destroy()
        #     blank_top.update()
        #
        # # OK button to exit the pop-up window
        # ok_button = tkinter.Button(blank_top, text="OK", command=exit_blank_top)
        # ok_button.grid(row=2, column=2)

    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"Website: {website}\n"
        #                                                       f"Email: {username}\n"
        #                                                       f"Password: {password}\n"
        #                                                       f"Is this ok?")
        file = open("data.txt", 'a+')
        file.write(f"{website}  ||  {username} || {password}\n")
        entry_website.delete(0, "end")
        entry_username.delete(0, "end")
        entry_password.delete(0, "end")
        file.close()
        # -------------------------------the following code is to create the pop-up box using canvas------------------
        # top = tkinter.Toplevel(window)
        # top.geometry("400x400")
        # top.title("Confirmation")
        #
        # # create image in canvas
        # canvas2 = tkinter.Canvas(top, width=100, height=100)
        # computer_img = tkinter.PhotoImage(file="logo.png")
        # canvas2.create_image(40, 40, image=computer_img)
        # canvas2.grid(row=2, column=0)
        # img_label = tkinter.Label(top, image=computer_img)
        # img_label.grid(row=2, column=0)
        #
        # confirm_label = tkinter.Label(top, text=f"Website: {website}\n"
        #                                         f"Email: {username}\n"
        #                                         f"Password: {password}\n"
        #                                         f"Is this ok?")
        # confirm_label.grid(row=1, column=1, columnspan=2)
        #
        # def exit_top():
        #     top.destroy()
        #     top.update()
        #

        #
        # # No button to exit the confirmation window
        # no_button = tkinter.Button(top, text="No", command=exit_top)
        # no_button.grid(row=2, column=2)
        # # Yes button to continue recording password
        # yes_button = tkinter.Button(top, text="Yes", command=record_password)
        # yes_button.grid(row=2, column=3)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(window, width=200, height=200)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(140, 100, image=lock_img)
canvas.grid(row=0, column=1)

# crate website label
label_website = tkinter.Label(text="Website")
label_website.grid(row=1, column=0)
# create entry box for website
entry_website = tkinter.Entry(window, width=50)
entry_website.grid(row=1, column=1, columnspan=2)

# crate username label
label_username = tkinter.Label(text="Email/Username")
label_username.grid(row=2, column=0)
# create entry box for username
entry_username = tkinter.Entry(window, width=50)
entry_username.grid(row=2, column=1, columnspan=2)

# crate password label
label_password = tkinter.Label(text="Password")
label_password.grid(row=3, column=0)
# create entry box for password
entry_password = tkinter.Entry(window, width=31)
entry_password.grid(row=3, column=1)
password = generate_password()

# create generate password button
generate_button = tkinter.Button(text="Generate Password", width=15, command=lambda: entry_password.insert(0, password))
generate_button.grid(row=3, column=2)

# create add password button
add_button = tkinter.Button(text="Add Password", width=42, command=add)
add_button.grid(row=4, column=1, columnspan=2)

tkinter.mainloop()
