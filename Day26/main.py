import pandas

# create Nato dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

# generate nato code based on user input
def generate_phonetics():
    name = input("Please enter your name: ").upper()
    try:
        user_nato = {letter: nato_dict[letter] for letter in name}
    except KeyError:
        print("Sorry, only letter in the alphabet please")
        generate_phonetics()
    else:
        print(user_nato)


generate_phonetics()