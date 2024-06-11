from turtle import Turtle

class Snake():

    def __init__(self):
        self.body = []
        self.positions = []

    def snake_starting_body(self):
        x_position = 0
        for i in range(3):
            self.body.append(Turtle())
            self.body[i].shape('square')
            self.body[i].color('white')
            self.body[i].penup()
            self.body[i].goto(x_position, 0)
            x_position += -20

    def move_snake(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.body[0].forward(20)

    def move_up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def move_left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def move_down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def move_right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def no_pen_body(self):
        for body in self.body:
            body.penup()
