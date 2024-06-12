from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("circle")
        self.speed = 10
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_pad(self):
        self.x_move *= -1

    def ball_reset(self):
        self.home()
        self.x_move *= -1
