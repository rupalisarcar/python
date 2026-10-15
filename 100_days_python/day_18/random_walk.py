import turtle
import random

tim = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

direction = [0,90,180,270]
tim.pensize(10)
tim.speed(10)

def define_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r,g,b)
    return my_tuple

for i in range(200):
   
    tim.forward(30)
    tim.color(define_color())
    tim.setheading(random.choice(direction))
    i+=1

screen.exitonclick()