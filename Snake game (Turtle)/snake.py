from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
NEON_COLOR = (15, 255, 80)
SPEED = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.part = []
        self.create()
        self.head= self.part[0]
    def create(self):
        for position in STARTING_POSITION:
            snake_body = Turtle()
            snake_body.shape("square")
            snake_body.color(NEON_COLOR)
            snake_body.penup()
            snake_body.goto(position)
            snake_body.speed(5)
            self.part.append(snake_body)
    def move(self):
        for i in range(len(self.part)-1,0,-1):
            new_x = self.part[i-1].xcor()
            new_y = self.part[i-1].ycor()
            self.part[i].goto(new_x,new_y)
        self.head.forward(SPEED)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

