import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food    
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_segment()

    #detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        is_game_on = False
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.all_segment[1:]:
        distance = snake.head.distance(segment)
        if distance<10:            
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()