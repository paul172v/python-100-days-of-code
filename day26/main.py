import pandas

nato = pandas.read_csv("./nato_phonetic_alphabet.csv")

name = input("Please type in a name")
split_name = list(name)

coded_name = []

for letter in split_name:
    for index, row in nato.iterrows():
        if letter.upper() == row.letter:
            coded_name.append(row.code)

print(coded_name)
