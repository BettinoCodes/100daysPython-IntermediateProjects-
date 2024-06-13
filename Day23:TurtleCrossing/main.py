import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import car_manager
import player
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_1 = Player()
cars = CarManager()
scoreboard = Scoreboard()


def turtle_control():
    screen.onkeypress(player_1.move_up, "w")
    screen.onkeypress(player_1.move_left, "a")
    screen.onkeypress(player_1.move_down, "s")
    screen.onkeypress(player_1.move_right, "d")


turtle_control()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_cars()
    cars.add_cars()

    for car in cars.car:
        for part in car:
            if player_1.distance(part) < 20:
                scoreboard.game_over()
                game_is_on = False
                break

    if player_1.ycor() >= 290:
        scoreboard.level_up()

        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT
        player_1.goto(player.STARTING_POSITION)

screen.exitonclick()
