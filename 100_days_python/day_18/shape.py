from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()


colors = ["red", "blue", "green", "purple", "orange", "gold"]
def draw_shapes(no_of_sides):
    for j in range(no_of_sides):
        tim.forward(100)
        tim.right(360/no_of_sides)
        j+=1




for i in range(3,11):
    tim.color(random.choice(colors))
    draw_shapes(i)

screen.exitonclick()