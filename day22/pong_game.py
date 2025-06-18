from turtle import Screen
import random
from paddle import Paddle
from ball import Ball
from game_over import GameOver

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

LEFT_PADDLE_STARTING_POSITION_X = -450
RIGHT_PADDLE_STARTING_POSITION_X = 450


right_paddle = Paddle(RIGHT_PADDLE_STARTING_POSITION_X)
left_paddle = Paddle(LEFT_PADDLE_STARTING_POSITION_X)
ball = Ball()
game_over = GameOver()

### Direction controls
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "W")
screen.onkey(left_paddle.go_down, "S")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    if ball.direction == "initial-up-right":
        ball.initial_move_up_right()

    ### Ball bouncing off top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.direction == "initial-up-right":
        ball.initial_move_up_right()
    elif ball.direction == "up-right":
        ball.move_up_right()
    elif ball.direction == "up-left":
        ball.move_up_left()
    elif ball.direction == "down-right":
        ball.move_down_right()
    elif ball.direction == "down-left":
        ball.move_down_left()

    ### Ball bouncing off of paddles
    ## Towards right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() >= 270:
        direction = ["down_left", "up_left"]
        direction_choice = random.choice(direction)

        if direction_choice == "down_left":
            ball.move_down_left()
        elif direction_choice == "up_left":
            ball.move_up_left()

    ## Towards left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() <= -270:
        direction = ["down_right", "up_right"]
        direction_choice = random.choice(direction)

        if direction_choice == "down_right":
            ball.move_down_right()
        elif direction_choice == "up_right":
            ball.move_up_right()

    ### Ball collides with left or right wall
    if ball.xcor() > 500:
        game_is_on = False
        game_over.show_left_wins()

    if ball.xcor() < -500:
        game_is_on = False
        game_over.show_right_wins()

    screen.update()

screen.exitonclick()
