from turtle import Turtle
import random
class Food:
    def __init__(self):
        self.creat()

    def creat(self):
        self.food = Turtle()
        self.xcor = (random.randint(1,10)-1)*20
        self.ycor = (random.randint(1,10)-1)*20
        self.food_cor = (self.xcor,self.ycor)
        self.food.penup()
        self.food.color("orange")
        self.food.shape("circle")
        self.food.goto(self.xcor,self.ycor)


