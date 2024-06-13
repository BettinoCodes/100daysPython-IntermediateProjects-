from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car = []
        self.positions = [-240, -220, -200, -180, -160, -140, -120, -100, -80,
                          -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180,
                           200, 220, 240]

    def add_cars(self):
        random_chance = random.randint(1,4)
        if random_chance == 1:
            curr_car = []
            car_color = random.choice(COLORS)
            x_position = 300
            y_position = random.choice(self.positions)
            for i in range(2):
                i = Turtle("square")
                i.color(car_color)
                i.penup()
                i.goto(x_position, y_position)
                curr_car.append(i)
                x_position += 22
            self.car.append(curr_car)

    def move_cars(self):
        for car in self.car:
            for part in car:
                new_x = part.xcor() - STARTING_MOVE_DISTANCE
                part.goto(new_x, part.ycor())

