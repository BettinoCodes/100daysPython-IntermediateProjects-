from turtle import Turtle
from food import Food


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(-140, 240)
        self.hideturtle()
        self.update_sb()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game over", True, align="center", font=("Arial", 24, "normal"))
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_sb()

    def update_sb(self):
        self.clear()
        self.goto(-140, 240)
        self.write(f"Score: {self.score} High Score: {self.highscore}", True, align="left", font=("Arial", 24, "normal"))

    def check_board(self):
        self.score += 1
        self.update_sb()
