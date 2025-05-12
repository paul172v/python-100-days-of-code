class User:
    def __init__(self, name):
        self.name = name

    def vroom(self):
        print("Vroom, vroom!")


user_1 = User("Jonas")
user_2 = User("Angela")

print(f"{user_1.name} {user_2.name}")

user_1.vroom()
