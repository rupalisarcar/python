import turtle as t
tim = t.Turtle()
screen = t.Screen()
tim.pensize(3)
def move_forward():
    tim.forward(40)
def move_backward():
    tim.backward(40)

def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def move(x,y):
    tim.ondrag(None)
    tim.goto(x,y)
    tim.ondrag(move)

tim.ondrag(fun=move, btn=1, add=True)
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear_screen)
screen.mainloop()