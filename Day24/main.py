with open(r"./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

with open("./Input/Names/invited_names.txt") as invited_names:
    name_list = invited_names.readlines()

for name in name_list:
    name = name.strip()
    title = f"invite_to_{name}.txt"
    path = f"./Output/ReadyToSend/{title}"
    content = letter.replace("[name]", name)
    with open(path, "w") as file:
        file.write(content)
