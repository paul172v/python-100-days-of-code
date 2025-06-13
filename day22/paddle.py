from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.position_x = position_x
        self.position_y = 0
        self.goto(position_x, self.position_y)

    def go_up(self):
        self.position_y += 20
        self.goto(self.position_x, self.position_y)

    def go_down(self):
        self.position_y -= 20
        self.goto(self.position_x, self.position_y)
