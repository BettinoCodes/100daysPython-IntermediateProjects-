from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.l_score =  0
        self.r_score = 0
        self.update_sb()

    def update_sb(self):
        self.goto(-100, 200)
        self.write(f"Score: {self.l_score}", True, align="center", font=("Arial", 24, "normal"))
        self.goto(100, 200)
        self.write(f"Score: {self.r_score}", True, align="center", font=("Arial", 24, "normal"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_sb()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_sb()
