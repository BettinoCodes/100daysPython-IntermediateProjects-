from turtle import Turtle
from food import Food

with open("my_file.txt") as file:
    high_num = file.read()

the_high = int(high_num)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = the_high
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
            with open("my_file.txt", 'w') as f:
                f.write(f"{self.highscore}")
        self.score = 0
        self.update_sb()

    def update_sb(self):
        self.clear()
        self.goto(-140, 240)
        self.write(f"Score: {self.score} High Score: {self.highscore}", True, align="left", font=("Arial", 24, "normal"))

    def check_board(self):
        self.score += 1
        self.update_sb()

