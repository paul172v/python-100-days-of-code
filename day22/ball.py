from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("slowest")
        self.movement_speed = 0.12
        self.direction = "initial-up-right"
        self.penup()
        self.position_x = 0
        self.position_y = 0
        self.goto(self.position_x, self.position_y)

    def initial_move_up_right(self):
        self.position_x += self.movement_speed
        self.position_y += self.movement_speed
        self.goto(self.position_x, self.position_y)

    def move_up_right(self):
        self.direction = "up-right"
        self.position_x += self.movement_speed
        self.position_y += self.movement_speed * 2
        self.goto(self.position_x, self.position_y)

    def move_up_left(self):
        self.direction = "up-left"
        self.position_x -= self.movement_speed
        self.position_y += self.movement_speed * 2
        self.goto(self.position_x, self.position_y)

    def move_down_right(self):
        self.direction = "down-right"
        self.position_x += self.movement_speed
        self.position_y -= self.movement_speed * 2
        self.goto(self.position_x, self.position_y)

    def move_down_left(self):
        self.direction = "down-left"
        self.position_x -= self.movement_speed
        self.position_y -= self.movement_speed * 2
        self.goto(self.position_x, self.position_y)

    def bounce_y(self):
        if self.direction == "up-right":
            self.direction = "down-right"
        elif self.direction == "up-left":
            self.direction = "down-left"
        elif self.direction == "down-right":
            self.direction = "up-right"
        elif self.direction == "down-left":
            self.direction = "up-left"
        elif self.direction == "initial-up-right":
            self.direction = "down-right"
