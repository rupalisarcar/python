import colorgram
import os

print(os.getcwd())
print(os.path.exists(r"D:\python\100_days_python\day_18\spot_image.jpg"))

colors = colorgram.extract(r'D:\python\100_days_python\day_18\spot_image.jpg',30)

new_colors=[]
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colors.append((r,g,b))


import turtle as t
import random
screen = t.Screen()
t.colormode(255)

t.penup()
t.hideturtle()

t.setheading(0)
t.setposition(-225,-225)
for row in range(10):
    for _ in range(10):
        color = random.choice(new_colors)
        t.dot(20, color)
        
        t.forward(50)
    t.setposition(-225,-225+(row+1)*50)
    


screen.exitonclick()