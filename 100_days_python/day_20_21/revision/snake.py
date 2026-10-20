import turtle as t
ALL_POSITIONS = [(20,0),(0,0),(-20,0)]
MOVING_DISTANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]
    def create_snake(self):
        for pos in ALL_POSITIONS:
            self.snake_add(pos)

    def snake_add(self,position):
        new_segment = t.Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def extend_snake(self):
        self.snake_add(self.all_segments[-1].position())

    def move(self):
        for i in range(len(self.all_segments)-1,0,-1):
            new_xcor = self.all_segments[i-1].xcor()
            new_ycor = self.all_segments[i-1].ycor()
            self.all_segments[i].goto(new_xcor, new_ycor)
            
        self.head.forward(MOVING_DISTANCE)  

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)