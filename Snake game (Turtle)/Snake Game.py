
import time
from turtle import Screen
from snake import Snake

WIDTH = 800
HEIGHT = 800
GAME = True

screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor("black")
screen.colormode(255)
screen.listen()
screen.tracer(0)
snake = Snake()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
while GAME:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
