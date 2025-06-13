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

    def show_left_wins(self):
        self.clear()
        self.write("Left Paddle wins!", align="center", font=("Arial", 16, "normal"))

    def show_right_wins(self):
        self.clear()
        self.write("Right Paddle wins!", align="center", font=("Arial", 16, "normal"))

    def hide(self):
        self.clear()
        self.write("", align="center", font=("Arial", 16, "normal"))
