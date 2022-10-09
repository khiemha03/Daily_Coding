from turtle import Turtle, Screen
import pandas as pd

turtle = Turtle()
turtle.penup()
turtle.hideturtle()
screen = Screen()
screen.title("US States Quiz")
screen.bgpic("blank_states_img.gif")
Guess_correct = 0
GAME = True
data = pd.read_csv("50_states.csv")
state = data["state"].tolist()
while GAME:
    answer = screen.textinput("List out the states",f"{Guess_correct}/52 states correct")
    if answer == None:
        GAME = False
    if answer in state:
        state.remove(answer)
        Guess_correct += 1
        result = data[data["state"] == answer]
        x_cor = int(result.x)
        y_cor = int(result.y)
        turtle.goto(x_cor,y_cor)
        turtle.write(answer)
