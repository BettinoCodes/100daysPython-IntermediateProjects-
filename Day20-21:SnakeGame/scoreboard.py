from turtle import Turtle
from food import Food


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-60, 240)
        self.hideturtle()
        self.update_sb()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over", True, align="center", font=("Arial", 24, "normal"))

    def update_sb(self):
        self.goto(-60, 240)
        self.write(f"Score: {self.score}", True, align="left", font=("Arial", 24, "normal"))

    def check_board(self):
        self.score += 1
        self.clear()
        self.update_sb()
