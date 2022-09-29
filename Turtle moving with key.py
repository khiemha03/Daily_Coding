from turtle import Turtle, Screen
import keyboard

def move_up():
    pen.forward(20)
    screen.update()
def move_left():
    pen.left(10)
    screen.update()
def move_right():
    pen.right(5)
    screen.update()
def move_down():
    pen.left(180)
    screen.update()
pen = Turtle()
screen = Screen()

keyboard.add_hotkey("w",move_up)
keyboard.add_hotkey("a", move_left)
keyboard.add_hotkey("s",move_down)
keyboard.add_hotkey("d", move_right)
screen.exitonclick()
