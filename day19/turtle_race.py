from turtle import Turtle, Screen
import random

red = Turtle()
blue = Turtle()
orange = Turtle()
purple = Turtle()

red_distance = 0
blue_distance = 0
orange_distance = 0
purple_distance = 0


def setup_turtle(turtle, color, starting_height):
    turtle.color(color)
    turtle.shape("turtle")
    turtle.penup()
    turtle.setpos(-200, starting_height)
    turtle.pendown()


def race(turtle):
    distance = random.randrange(0, 50)
    turtle.forward(distance)
    return distance


screen = Screen()

## screen is 250 width edge
## Setup turtles
setup_turtle(red, "red", 150)
setup_turtle(blue, "blue", 50)
setup_turtle(orange, "orange", -50)
setup_turtle(purple, "purple", -150)

## enter bet
screen.setup(width=500, height=500)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color:\n"
)
print(user_bet)

## distance moved
while (
    red_distance < 450
    and blue_distance < 450
    and orange_distance < 450
    and purple_distance < 450
):
    red_distance += race(red)
    blue_distance += race(blue)
    orange_distance += race(orange)
    purple_distance += race(purple)

## if race has ended
if red_distance >= 449 and user_bet == "red":
    print("red wins, bet successful")
elif red_distance >= 449 and user_bet != "red":
    print("red wins, bet unsuccessful")

if blue_distance >= 449 and user_bet == "blue":
    print("blue wins, bet successful")
elif blue_distance >= 449 and user_bet != "blue":
    print("blue wins, bet unsuccessful")

if orange_distance >= 449 and user_bet == "orange":
    print("orange wins, bet successful")
elif orange_distance >= 449 and user_bet != "orange":
    print("orange wins, bet unsuccessful")

if purple_distance >= 449 and user_bet == "purple":
    print("purple wins, bet successful")
elif purple_distance >= 449 and user_bet != "purple":
    print("purple wins, bet unsuccessful")


screen.exitonclick()
