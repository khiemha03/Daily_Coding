from turtle import Turtle
import random
class Food:
    def __init__(self):
        self.creat()

    def creat(self):
        food = Turtle()
        xcor = (random.randint(1,10)-1)*20
        ycor = (random.randint(1,10)-1)*20
        food.penup()
        food.color("orange")
        food.shape("circle")
        food.goto(xcor,ycor)


