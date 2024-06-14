import time
import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
import random
from scoreboard import Scoreboard


snake = Snake()
screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)
screen.listen()
screen.tracer(0)
screen.listen()
screen.title("Bs 100 Day Python Snake Game")


def snake_control():
    screen.onkey(snake.move_up, "w")
    screen.onkey(snake.move_left, "a")
    screen.onkey(snake.move_down, "s")
    screen.onkey(snake.move_right, "d")


snake.snake_starting_body()
food = Food()
scoreboard = Scoreboard()
game_on = True
while game_on :
    screen.update()
    time.sleep(.1)
    snake.move_snake()
    snake_control()
    snake_head = snake.body
    sn_head = snake_head[0]
    sn_head.color("blue")
    if sn_head.distance(food) < 15:
        food.generate_food()
        scoreboard.check_board()
        snake_head[len(snake_head) - 1].penup()
        snake_head.append(Turtle("square"))
        snake_head[len(snake_head) - 1].color('white')
        snake.no_pen_body()

    if sn_head.xcor() > 290 or sn_head.xcor() < -290:
        scoreboard.reset()
        snake.reset()

    if sn_head.ycor() > 300 or sn_head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for i in range(1, len(snake.body)):
        if sn_head.distance(snake.body[i].position()) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


