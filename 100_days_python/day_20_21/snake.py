import turtle as t
STARTING_POSITION=[(20,0),(0,0),(-20,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.all_segment = []
        self.create_snake()
        self.head = self.all_segment[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, position):
        snake = t.Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.all_segment.append(snake)

    def extend_segment(self):
        self.add_segment(self.all_segment[-1].position())

    def move(self):
        for seg_num in range(len(self.all_segment)-1,0,-1):
            new_xcor = self.all_segment[seg_num-1].xcor()
            new_ycor = self.all_segment[seg_num-1].ycor()
            self.all_segment[seg_num].goto(new_xcor, new_ycor)

        self.head.forward(MOVE_DISTANCE)   
    
    def up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP) 

    def down(self):
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT: 
            self.head.setheading(RIGHT)


