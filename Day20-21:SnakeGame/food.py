from turtle import Turtle
import random
from snake import Snake

snake = Snake()
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.speed('fastest')
        self.penup()
        self.shapesize(.5,.5, 1)
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.positions = [(rand_x, rand_y)]
        self.goto(rand_x, rand_y)
        self.snake = Snake()

    def generate_food(self):
            self.clear()
            self.penup()
            rand_x = random.randint(-280, 280)
            rand_y = random.randint(-280, 280)
            while (rand_x, rand_y) == self.positions[len(self.positions) - 1]:
                rand_x = random.randint(-280, 280)
                rand_y = random.randint(-280, 280)
            self.goto(rand_x, rand_y)
            self.positions.append((rand_x, rand_y))
