import imp
from turtle import Screen , Turtle
import turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"o")
screen.onkey(r_paddle.go_down,"l")
screen.onkey(l_paddle.go_up,"z")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
    # detect coullision with wall
    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce_y()
    
    # detect coulission with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # ball L is missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    # ball R is missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()