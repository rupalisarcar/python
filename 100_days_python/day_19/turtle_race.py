import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color : ")
print(user_choice)
colors = ["dark green", "brown", "coral", "dark cyan", "dark magenta", "blue"]
y_positions = [-90,-50,-10,30,70,110]
x=-240
y=0
all_turtles = []
is_race_on = False

for turtle_index in range(0,6):
    tim = t.Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x,y=y_positions[turtle_index])
    all_turtles.append(tim)
if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>235:
            win_turtle = turtle.pencolor()
            is_race_on = False
            if win_turtle == user_choice:
                print(f"You'have won! The {win_turtle} turtle is the winner")
            else:
                print(f"You'have lost! The {win_turtle} turtle is the winner")
        turtle.forward(random.randint(0,10))




screen.exitonclick()