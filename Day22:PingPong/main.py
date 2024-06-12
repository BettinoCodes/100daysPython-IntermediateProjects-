from turtle import Turtle, Screen
from player_bar import PlayerBar
import time
from aibar import AiBar
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title("Bs Pong Game")
screen.tracer(0)
screen.listen()
screen.setup(800, 600)

player_bar = PlayerBar()
aibar = AiBar()
ball = Ball()
scoreboard = Scoreboard()

def player_control():
    screen.onkeypress(player_bar.move_up, "w")
    screen.onkeypress(player_bar.move_down, "s")


player_bar.add_bar()
aibar.add_bar()

# for i in range(1, len(snake.body)):
#         if sn_head.distance(snake.body[i].position()) < 10:
# sn_head.distance(snake.body[i].position())

game_on = True
while game_on:
    screen.update()
    time.sleep(.07)
    player_control()
    aibar.move_up_down()
    ball.move_ball()

    for i in range(len(player_bar.player_body)):
        if ball.distance(player_bar.player_body[i]) < 25 and ball.xcor() > 370:
            ball.bounce_pad()
            print("hit")

    for i in range(len(aibar.player_body)):
        if ball.distance(aibar.player_body[i]) < 15 and ball.xcor() < -370:
            ball.bounce_pad()
            print("hit2")

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 450:
        ball.ball_reset()
        scoreboard.l_point()
        
    if ball.xcor() < -410:
        ball.ball_reset()
        scoreboard.r_point()


screen.exitonclick()
