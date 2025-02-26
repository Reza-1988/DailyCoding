import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
data_states = data["state"].tolist()

guessed_states_list = []
missing_states_list = []

while len(guessed_states_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states_list)}/50 States Correct", prompt="What's another state's name?").title()

    # for exit of game and make a list of states that should be learn
    if answer_state == "Exit":
        for state in data_states:
            if state not in guessed_states_list:
                missing_states_list.append(state)
        missing_data = pd.DataFrame(missing_states_list)
        missing_data.to_csv("states_should_learn.csv")
        break

    if answer_state in data_states:
        guessed_states_list.append(answer_state)
        w = turtle.Turtle() # making this turtle just for write states in map
        w.penup()
        w.hideturtle()
        w.goto(float(data[data["state"] == answer_state]["x"].iloc[0]), float(data[data["state"] == answer_state]["y"].iloc[0]))
        w.write(answer_state, align="center", font=("Arial", 8, "bold"))

