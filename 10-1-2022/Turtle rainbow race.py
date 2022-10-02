import time
from turtle import Turtle, Screen
import random

COLOR = ["red", "green", "blue", "black", "purple", "orange", "yellow"]
YCOR = [-225,-150,-75,0,75,150,225]
XCOR = -250
GAME = True
WINNER = ""
CAR = []
class Turtlecreation:
    def __init__(self,color,xcor,ycor):
        self.color = color
        self.car = Turtle()
        self.speed = random.randint(1,10)
        self.car.color(self.color)
        self.car.shape("turtle")
        self.car.penup()
        self.car.goto(xcor,ycor)
        self.car.speed(10)
    def move(self):
        if self.car.xcor() < 280:
            self.car.forward(self.speed)
        else:
            global GAME, WINNER
            GAME = False
            WINNER = self.color


screen = Screen()
screen.setup(width=600, height=500)
guess = screen.textinput(title="Race guessing",prompt="What is your winning turtle")

for i in range(7):
    CAR.append(Turtlecreation(COLOR[i],XCOR,YCOR[i]))
while GAME:
    CAR[0].move()
    CAR[1].move()
    CAR[2].move()
    CAR[3].move()
    CAR[4].move()
    CAR[5].move()
    CAR[6].move()
else:
    if WINNER == guess:
        print("You are correct in guessing")
    else:
        print("Your guess is wrong. Sorry !")
screen.exitonclick()
