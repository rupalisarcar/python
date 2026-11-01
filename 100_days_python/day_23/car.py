COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class Car():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        random_num = random.randint(1,6)
        if random_num == 2:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            # new_car.setheading(180)
                    
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-230,230)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    def car_move(self):    
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def car_speed_increase(self):
        self.car_speed +=MOVE_INCREMENT 