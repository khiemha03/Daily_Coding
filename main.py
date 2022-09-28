    # This is a sample Python script.

from turtle import Turtle, Screen


def square():
    for i in range(4):
        pen.forward(100)
        pen.right(90)


pen = Turtle()
square()
screen = Screen()
screen.exitonclick()