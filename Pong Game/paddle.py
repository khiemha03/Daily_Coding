from turtle import Turtle
import time
import keyboard
COORDINATE = [(-480,0),(480,0)]
class Paddle:
    def __init__(self):
        self.paddle = []
        self.create_paddle()
    def create_paddle(self):
        self.paddle_1 = Turtle()
        self.paddle_2 = Turtle()
        self.paddle.append(self.paddle_1)
        self.paddle.append(self.paddle_2)
        for i in range(2):
            self.paddle[i].color("white")
            self.paddle[i].shape("square")
            self.paddle[i].penup()
            self.paddle[i].setheading(90)
            self.paddle[i].shapesize(1,5)
            self.paddle[i].goto(COORDINATE[i])
    def move_up_paddle_1(self):
        if self.paddle_1.ycor() < 250:
            self.paddle_1.forward(10)
    def move_down_paddle_1(self):
        if self.paddle_1.ycor() > -240:
            self.paddle_1.back(10)
    def move_up_paddle_2(self):
        if self.paddle_2.ycor() < 250:
            self.paddle_2.forward(10)
    def move_down_paddle_2(self):
        if self.paddle_2.ycor() > -240:
            self.paddle_2.back(10)
    def checking(self):
        if keyboard.is_pressed("w"):
            self.move_up_paddle_1()
        if keyboard.is_pressed("s"):
            self.move_down_paddle_1()
        if keyboard.is_pressed("Up"):
            self.move_up_paddle_2()
        if keyboard.is_pressed("Down"):
            self.move_down_paddle_2()

