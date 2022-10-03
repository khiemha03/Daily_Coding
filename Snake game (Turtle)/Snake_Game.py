
import time
from turtle import Screen
from snake import Snake
from food import Food
WIDTH = 800
HEIGHT = 800


screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor("black")
screen.colormode(255)
screen.listen()
screen.tracer(0)
snake = Snake()
food = Food()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
while snake.state:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if food.food.distance(snake.head) < 10:
        snake.eat()
screen.exitonclick()
