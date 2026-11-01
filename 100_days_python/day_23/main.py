from turtle import Turtle, Screen
import time
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = Screen()

screen.setup(height=600, width=600)
screen.tracer(0)

player = Player()
cars = Car()
level = Scoreboard()

screen.listen()
screen.onkey(player.move,'Up')

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.car_move()

    #Detect collision with car
    for car in cars.all_cars:
        if car.distance(player)<20:
            is_game_on = False
            level.quit_game()
            player.starting_position()


    # detect player hits the wall
    if player.end_position():
        player.starting_position()
        cars.car_speed_increase()
        level.level_up()

screen.exitonclick()