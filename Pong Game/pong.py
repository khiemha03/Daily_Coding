from turtle import Turtle
import random
import time
class Pong:
    def __init__(self):
        self.score = 0
        # self.x_cor = random.uniform(0, 10)
        # self.y_cor = random.uniform(0, 10)
        self.x_cor = 3
        self.y_cor = 3
        self.line()
        self.pong()
    def line(self):
        self.pen = Turtle()
        self.pen.penup()
        self.pen.color("white")
        self.pen.pensize(4)
        self.pen.goto(0,340)
        self.pen.setheading(270)
        for i in range(20):
            self.pen.pendown()
            self.pen.forward(30)
            self.pen.penup()
            self.pen.forward(20)
    def pong(self):
        self.ball = Turtle()
        self.ball.penup()
        self.ball.color("white")
        self.ball.shape("circle")
    def ybounce(self):
        self.y_cor *= -1
    def xbounce(self):
        self.x_cor *= -1
    def moving(self):
        self.new_xcor = self.ball.xcor() + self.x_cor
        self.new_ycor = self.ball.ycor() + self.y_cor
        self.ball.goto(self.new_xcor, self.new_ycor)
    def reset(self):
        self.ball.home()
        self.moving()