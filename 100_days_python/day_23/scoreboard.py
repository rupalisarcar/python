from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier",18,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-285,275) 
        self.show_level()   
        
    def show_level(self):
        self.write(f"Level : {self.level}", align=ALIGNMENT, font= FONT)

    def level_up(self):
        self.level+=1
        self.clear()
        self.show_level()

    def quit_game(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font= FONT)