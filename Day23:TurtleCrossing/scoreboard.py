from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(-200, 260)
        self.hideturtle()
        self.update_sb()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over", True, align="center", font=FONT)

    def update_sb(self):
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", True, align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_sb()
