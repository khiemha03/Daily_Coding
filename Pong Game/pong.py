from turtle import Turtle

class Pong:
    def __init__(self):
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