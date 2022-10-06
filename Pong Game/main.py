from turtle import Screen
from paddle import Paddle
from pong import Pong
import time
import keyboard

WIDTH = 1000
HEIGHT = 600


screen = Screen()
screen.title("Pong Game")
screen.listen()
screen.tracer(0)
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
paddle = Paddle()
pong = Pong()
GAME = True
while GAME:
    screen.update()
    paddle.checking()

screen.exitonclick()