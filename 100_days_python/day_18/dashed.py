from turtle import Turtle, Screen

mini_turtle = Turtle()
screen = Screen()

# mini_turtle.forward(100)
# mini_turtle.up()
# mini_turtle.goto(150, 0)
mini_turtle.speed(2)

for i in range(15):
    mini_turtle.forward(10)
    mini_turtle.up()
    mini_turtle.forward(10)
    mini_turtle.down()
    i+=1
screen.mainloop()
screen.exitonclick()