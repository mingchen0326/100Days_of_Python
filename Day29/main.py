import string
import tkinter
import random
import json
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
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    # check empty input
    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Blank Input", message="Entry cannot be empty")

    else:
        try:
            with open("data.json", "r") as data_file:
                # Reloading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Reloading old data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, "end")
            entry_username.delete(0, "end")
            entry_password.delete(0, "end")


# ------------------------------ Search ------------------------------- #
def search():
    website = entry_website.get()
    # loading old data
    with open("data.json", "r") as data_file:
        if len(website) == 0:
            messagebox.showinfo(title="Blank Input", message="Input Cannot Be Blank")
        elif website in data_file:
            data = json.load(data_file)
            saved_username = data[website]["username"]
            saved_password = data[website]["password"]
            messagebox.showinfo(title="Password Information", message=f"username: {saved_username}\n"
                                                                      f"password: {saved_password}")
        else:
            messagebox.showinfo(title="Password Information", message="No Data File Found")


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
entry_website = tkinter.Entry(window, width=31)
entry_website.grid(row=1, column=1)

# crate username label
label_username = tkinter.Label(text="Email/Username")
label_username.grid(row=2, column=0)
# create entry box for username
entry_username = tkinter.Entry(window, width=48)
entry_username.grid(row=2, column=1, columnspan=3)

# crate password label
label_password = tkinter.Label(text="Password")
label_password.grid(row=3, column=0)
# create entry box for password
entry_password = tkinter.Entry(window, width=31)
entry_password.grid(row=3, column=1)
password = generate_password()

# create generate password button
generate_button = tkinter.Button(text="Create Password", width=13, command=lambda: entry_password.insert(0, password))
generate_button.grid(row=3, column=2)

# create add password button
add_button = tkinter.Button(text="Add Password", width=42)
add_button.grid(row=4, column=1, columnspan=3)

# add password search button
search_button = tkinter.Button(text="Search", width=13, command=search)
search_button.grid(row=1, column=2)

tkinter.mainloop()
