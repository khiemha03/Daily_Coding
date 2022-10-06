from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.player_1 = 0
        self.player_2 = 0
        self.display()
    def display(self):
        self.score = Turtle()
        self.score.penup()
        self.score.color("white")
        self.score.hideturtle()
        self.score.goto(0,240)
        self.score.write(f"{self.player_1}           {self.player_2}",False, "center",("Times",40,"normal"))
    def update_player1(self):
        self.player_1 += 1
        self.score.clear()
        self.display()
    def update_player2(self):
        self.player_2 += 1
        self.score.clear()
        self.display()
