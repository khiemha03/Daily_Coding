from turtle import Turtle, Screen

def up():
    pen.forward(20)
def down():
    pen.back(20)
def left():
    pen.left(8)
def right():
    pen.right(8)
def clear():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()
pen = Turtle()
screen = Screen()
screen.listen()
screen.onkeypress(up,"w")
screen.onkeypress(down,"s")
screen.onkeypress(left,"a")
screen.onkeypress(right,"d")
screen.onkey(clear,"c")
screen.exitonclick()