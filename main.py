import turtle
import pandas
count = 0
cor = -1
Ture = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S. States name quizz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

x_cor = data["x"].to_list()
y_cor = data["y"].to_list()
list_states = data["state"].to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{count}/50 States Correct", prompt="Whats another state")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        # missing_state = []
        missing_state = [state for state in list_states if state not in guessed_states ]
        # for state in list_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("State_to_learn.csv")
        break
    if answer_state in list_states:
        guessed_states.append(answer_state)
        index = list_states.index(answer_state)
        count = count + 1
        Ture.penup()

        Ture.goto(x_cor[index], y_cor[index])
        Ture.write(answer_state)
