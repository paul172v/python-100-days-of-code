import turtle
import pandas
from state import State

# Load state data
state_data_file = pandas.read_csv("./50_states.csv")

states = state_data_file.state.tolist()
xs = state_data_file.x.tolist()
ys = state_data_file.y.tolist()

# Setup turtle screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Keep track of guessed states
guessed_states = []

# Game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What is another state's name?",
    )

    if answer_state is None:  # User clicked "Cancel"
        break

    answer_state = answer_state.title()

    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        index = state_data_file[state_data_file.state == answer_state].index[0]
        new_state = State(answer_state, xs[index], ys[index])

screen.exitonclick()
