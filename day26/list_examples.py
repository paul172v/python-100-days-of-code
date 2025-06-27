# numbers = [1, 2, 3]

# new_list = [n + 1 for n in numbers]

# name = "Angela"

# letters_list = [letter for letter in name]

# range_list = [number * 2 for number in range(1, 5)]

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# short_names = [name for name in names if len(name) < 5]

# capped_names = [name.upper() for name in names if len(name) > 4]


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number**2 for number in numbers]
# print(squared_numbers)

# list_of_strings = ["9", "0", "32", "8", "2", "8", "64", "29", "42", "99"]
# result = []
# numbers = [
#     result.append(string) for string in list_of_strings if (int(string) % 2 == 0)
# ]
# print(result)


file1_list = []
file2_list = []

with open("file1.txt") as file1:
    file1_list = file1.readlines()
file1_list = [string.replace("\n", "") for string in file1_list]

with open("file2.txt") as file2:
    file2_list = file2.readlines()
file2_list = [string.replace("\n", "") for string in file2_list]


results = []

for string1 in file1_list:
    for string2 in file2_list:
        if string1 == string2:
            results.append(int(string1))

print(results)
