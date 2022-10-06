from turtle import Screen
from paddle import Paddle
from pong import Pong
from scoreboard import Scoreboard
import time


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
score= Scoreboard()
GAME = True
while GAME:
    time.sleep(0.001)
    screen.update()
    paddle.checking()
    pong.moving()
    if pong.ball.ycor() > 280 or pong.ball.ycor() < -280:
        pong.ybounce()
    if (pong.ball.xcor()> 465 and pong.ball.distance(paddle.paddle_2) < 50) or (pong.ball.xcor() < -465 and pong.ball.distance(paddle.paddle_1) < 50):
        pong.xbounce()
    elif pong.ball.xcor() > 480:
        pong.reset()
        score.update_player1()
    elif pong.ball.xcor() < -480:
        pong.reset()
        score.update_player2()
screen.exitonclick()