import turtle as t
import random

screen = t.Screen()
t.colormode(255)

# t.begin_fill()
# t.tilt(10)
# t.circle(100)
# t.shape("circle")
# t.shapesize(4,2)
t.speed("fastest")

def define_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r,g,b)
    return my_tuple

def draw_spinograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        t.color(define_color())
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)

draw_spinograph(15)



screen.exitonclick()



