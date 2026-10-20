import turtle as t
from snake import Snake
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
screen.listen()

snake = Snake()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.exitonclick()

