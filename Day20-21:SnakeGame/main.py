import time
import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
import random
from scoreboard import Scoreboard

#On these two days I worked on a snake game using my knowledge on OOP I was able to build the game from 0, making it it my own using a list

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

    if sn_head.xcor() > 300 or sn_head.xcor() < -300:
        scoreboard.game_over()
        game_on = False

    if sn_head.ycor() > 300 or sn_head.ycor() < -300:
        scoreboard.game_over()
        game_on = False

    for i in range(1, len(snake.body)):
        if sn_head.distance(snake.body[i].position()) < 10:
            game_on = False
            scoreboard.game_over()




screen.exitonclick()
