from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.speed("fastest")
        self.write("", align="center", font=("Arial", 16, "normal"))

    def show(self):
        self.clear()
        self.write("Game over!", align="center", font=("Arial", 16, "normal"))

    def hide(self):
        self.clear()
        self.write("", align="center", font=("Arial", 16, "normal"))
