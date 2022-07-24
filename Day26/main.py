import pandas

# create Nato dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

# generate nato code based on user input
name = input("Please enter your name: ").upper()
user_nato = {letter: nato_dict[letter] for letter in name}
print(user_nato)