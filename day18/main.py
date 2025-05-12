from turtle import Turtle, Screen, colormode
import random

colormode(255)  # Allows RGB values from 0–255

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")


def walk():
    # Generate random RGB color
    tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    direction_arr = ["forward", "left", "right", "backward"]
    direction = random.choice(direction_arr)

    timmy_the_turtle.pencolor(tup)

    if direction == "forward":
        timmy_the_turtle.forward(100)
    elif direction == "left":
        timmy_the_turtle.left(90)
        timmy_the_turtle.forward(100)
    elif direction == "right":
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(100)
    elif direction == "backward":
        timmy_the_turtle.backward(100)

    print(f"{direction=}, {tup=}")


def random_walk(steps):
    for _ in range(steps):
        walk()


random_walk(16)

screen = Screen()
screen.exitonclick()
