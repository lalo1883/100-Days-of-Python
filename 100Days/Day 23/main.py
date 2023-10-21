import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()

car_manager = CarManager()
screen.bgcolor('#87CEEB')
p1 = Player()
screen.listen()
screen.onkey(p1.move_f, 'w')
screen.onkey(p1.move_l, 'a')
screen.onkey(p1.move_r, 'd')


game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_c()
    for car in car_manager.all_cars:
        if car.distance(p1) < 20:
            score.game_over()
            game_is_on = False

    if p1.is_at_end():
        p1.go_to_start()
        car_manager.increae_speed()
        score.increase_level()
        score.update_score()

screen.exitonclick()