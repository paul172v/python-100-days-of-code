from turtle import Turtle, Screen


class State(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.name = name  # Use the string directly
        self.x = x  # Use the numeric value directly
        self.y = y
        self.font = ("Arial", 12, "normal")
        self.hideturtle()  # Hide the default turtle shape
        self.penup()  # Prevent drawing lines when moving
        self.move_to(self.x, self.y)

    def move_to(self, x, y):
        self.clear()  # Clear previous writings
        self.goto(x, y)
        self.write(self.name, font=self.font, align="center")
