import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S Stat Game")
image = "blank_states_img.gif"
# screen.bgpic(image)
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
#
# if answer_state in data["state"]:
#     ans = Turtle()
#     ans.write(answer_state)
#     x = data[data["state"] == 'Alabama'].x
#     y = data[data["state"] == 'Alabama'].y
#     ans.goto(x,y)

def get_mouse_click_coor(x, y):
    print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

correct_states = []
while len(correct_states) != 50:
    answer_state = screen.textinput(title=f"Guess the state {len(correct_states)}/50", prompt="Write a state below: ").title()

    if answer_state == "Exit":
        missed_states = [state for state in data["state"].tolist() if state not in correct_states]
        dict_states = {
            "Missed States": missed_states
        }
        df = pandas.DataFrame(dict_states)
        df.to_csv("missed_states")

        break

    if answer_state in data["state"].tolist():
        ans = Turtle()
        ans.penup()
        ans.hideturtle()
        state_data = data[data.state == answer_state]
        ans.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        ans.write(answer_state)
        correct_states.append(answer_state)


screen.exitonclick()
