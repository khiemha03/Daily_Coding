from turtle import Turtle, Screen
import random
import keyboard


def turn_left():
    pen.left(90)
    pen.forward(LENGTH_PATH)
def turn_right():
    pen.right(90)
    pen.forward(LENGTH_PATH)
def turn_down():
    pen.left(180)
    pen.forward(LENGTH_PATH)
def turn_up():
    pen.forward(LENGTH_PATH)


THICKNESS = 15
LENGTH_PATH = 30
DIRECTION = ["left","right","up","down"]
SCREEN_WIDTH = 500
pen = Turtle()
screen = Screen()
# Change the colormode to RBG
screen.colormode(255)
screen.screensize(SCREEN_WIDTH,SCREEN_WIDTH)
pen.width(THICKNESS)
pen.speed(10)
while not keyboard.is_pressed("esc"):
    x = random.randint(0,255)
    y = random.randint(0,255)
    z = random.randint(0,255)
    pen.color(x,y,z)
    if random.choice(DIRECTION) == "left":
        turn_left()
    elif random.choice(DIRECTION) == "right":
        turn_right()
    elif random.choice(DIRECTION) == "up":
        turn_up()
    else:
        turn_down()
    if pen.xcor() > 350 or pen.xcor()<-350:
        pen.penup()
        pen.goto(0,0)
        pen.pendown()
    if pen.ycor() > 350 or pen.ycor()<-350:
        pen.penup()
        pen.goto(0,0)
        pen.pendown()
screen.exitonclick()