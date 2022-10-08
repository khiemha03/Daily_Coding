from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current = 0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 360)
        self.hideturtle()
        self.score()
    def score(self):
        self.clear()
        self.write(f"Score: {self.current}| Highscore: {self.highscore}",False,"center", font=("Times",24,"normal") )

    def update_score(self):
        self.score()

    def update_highscore(self):
        if self.current > self.highscore:
            self.highscore = self.current
            self.current = 0

    def gameover(self):
        self.update_highscore()
        self.home()
        self.write("Game Over",False,"center", font=("Times",24,"normal") )
        with open("highscore.txt","w") as file:
            file.write(f"{self.highscore}")