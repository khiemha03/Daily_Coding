
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
WIDTH = 800
HEIGHT = 800


screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor("black")
screen.colormode(255)
screen.listen()
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
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
        score.current +=1
        score.update_score()
        while food.food.distance(snake.head) < 10:
            food.clear()
else:
    score.gameover()
    print(f"You have scored: {score.current}")
screen.exitonclick()
