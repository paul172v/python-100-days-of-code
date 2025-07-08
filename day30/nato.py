# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    word = input("Enter a word: ").upper()
    if word.isalpha():
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
    else:
        print("Only letters in the alphabet may be entered.")
        generate_phonetic()


generate_phonetic()
