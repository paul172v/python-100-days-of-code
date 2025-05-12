from turtle import Turtle, Screen, colormode
import random

colormode(255)  # Allows RGB values from 0–255

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")


def walk(radius):
    # Generate random RGB color
    tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy_the_turtle.pencolor(tup)
    timmy_the_turtle.circle(radius)


def random_circle(radius):
    for _ in range(18):
        walk(radius)
        timmy_the_turtle.left(20)


random_circle(50)

screen = Screen()
screen.exitonclick()
