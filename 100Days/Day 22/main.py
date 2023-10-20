from turtle import *
from paddle import Paddle
from ball import  ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle(350,0)
left_paddle = Paddle(-350,0)

screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')


ball1 = ball()

score = Scoreboard()


left_points = 0
right_points = 0

game_is_on = True
while game_is_on:

    time.sleep(ball1.move_speed)
    if ball1.ycor() > 280 or ball1.ycor() < -280:
        ball1.bounce()

    if ball1.distance(right_paddle) < 50 and ball1.xcor() > 320 or ball1.distance(left_paddle) < 50 and ball1.xcor() < -320:
        # ball1.increase_speed()
        ball1.bounce_paddle()

    if ball1.xcor() > 380:
        # time.sleep(1)
        ball1.reset_p()
        score.leftPoint()

    if ball1.xcor() < -380:
        ball1.reset_p()
        # time.sleep(1)
        score.rightPoint()


    ball1.move()
    screen.update()
