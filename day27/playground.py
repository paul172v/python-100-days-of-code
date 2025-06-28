def add(*args):
    tally = 0
    for n in args:
        tally += n
    print(tally)


add(5, 5, 10)


def calculate(**kwargs):
    tally = 0
    for key, value in kwargs.items():
        if key == "add":
            tally += value
        if key == "multiply":
            tally *= value
    print(tally)


calculate(add=2, multiply=3)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GTR")

his_car = Car()

print(my_car.make, my_car.model)
print(his_car.make, his_car.model)
