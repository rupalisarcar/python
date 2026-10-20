import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect food
    if snake.head.distance(food)<15:
        food.refresh_food()
        scoreboard.updated_score()
        snake.extend_snake()

    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        is_game_on=False
        scoreboard.quit_game()

    #detect collision with own tail
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment)<10:
            is_game_on=False
            scoreboard.quit_game()



screen.exitonclick()

