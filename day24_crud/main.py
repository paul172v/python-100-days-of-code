# with open(r"C:\Users\paul1\Desktop\08-python-course\day24_crud\my_file.txt") as file:    ### LONG WAY
# with open("day24_crud/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open(
#     r"C:\Users\paul1\Desktop\08-python-course\day24_crud\my_file.txt",
#     mode="a",  # w = write, a = append
# ) as file:
#     file.write("\nNew text.")

with open('day24_crud/new_file.txt', mode='w') as file:
    file.write('Even newer text.')