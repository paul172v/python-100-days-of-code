# try:
#     file = open("a_text_file.txt")
#     # a_dictionary = {"key": "value"}
#     # print(a_dictionary["sdfgweg"])
# except FileNotFoundError:
#     file = open("a_text_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / (height * height)
print(bmi)
