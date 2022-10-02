import colorgram
from turtle import Turtle, Screen
import random

COLOR = []
color_list = colorgram.extract("painting.jpg",35)
WIDTH = 500
LENGTH = 500
for rgb in color_list:
    r = rgb.rgb.r
    g = rgb.rgb.g
    b = rgb.rgb.b
    COLOR.append((r,g,b))

pen = Turtle()
screen = Screen()
screen.colormode(255)
# screen.screensize(WIDTH, LENGTH)
pen.penup()
pen.goto(-410, -310)
for i in range(8):
    for i in range(7):
        pen.forward(100)
        color = random.choice(COLOR)
        pen.dot(50, color)
    pen.left(90)
    pen.forward(100)
    pen.right(90)
    pen.back(700)


screen.exitonclick()