from turtle import Turtle

class PlayerBar:
    def __init__(self):
        self.player_body = []
        # self.head = self.player_body[0]
        # self.head.setheading(90)
        self.x_position = 380

    def add_bar(self):
        x_value = 0
        height = 0
        for i in range(5):
            self.player_body.append(Turtle("square"))
            self.player_body[i].shapesize(stretch_wid=3, stretch_len=1)
            self.player_body[i].penup()
            self.player_body[i].goto(self.x_position, height)
            height -= 20

    def move_up(self):
        for body in self.player_body:
            new_y = body.ycor() + 20
            body.goto(self.x_position, new_y)

    def move_down(self):
        for body in self.player_body:
            new_y = body.ycor() - 10
            body.goto(self.x_position, new_y)
