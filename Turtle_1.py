    # This is a sample Python script.

from turtle import Turtle, Screen


def square():
    for i in range(4):
        pen.forward(100)
        pen.right(90)
pen = Turtle()
for _ in range(36):
    square()
    pen.left(10)
pen.hideturtle()
screen = Screen()
screen.exitonclick()