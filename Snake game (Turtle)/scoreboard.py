from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current = 0
        self.color("white")
        self.penup()
        self.goto(0, 360)
        self.hideturtle()
        self.score()
    def score(self):
        self.write(f"Score: {self.current}",False,"center", font=("Times",24,"normal") )

    def update_score(self):
        self.clear()
        self.score()

    def gameover(self):
        self.home()
        self.write("Game Over",False,"center", font=("Times",24,"normal") )