
from turtle import Turtle, Screen, color
import random


def square():
    x = random.randint(0,255)
    y = random.randint(0,255)
    z = random.randint(0,255)
    pen.color(x,y,z)
    for i in range(4):
        pen.forward(100)
        pen.right(90)


pen = Turtle()
screen = Screen()
screen.colormode(255)
for _ in range(36):
    square()
    pen.left(10)


pen.hideturtle()
screen.exitonclick()
