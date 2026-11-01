from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",40,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.color("White")
        self.penup()        
        self.hideturtle()
        self.show_score()
        
    def show_score(self):
        self.goto(-120,240)
        self.write(f"{self.l_score}", align=ALIGNMENT, font= FONT)
        self.goto(120,240)
        self.write(f"{self.r_score}", align=ALIGNMENT, font= FONT)
        

    def update_left_score(self):
        self.l_score+=1
        self.clear()
        self.show_score()

    def update_right_score(self):
        self.r_score+=1
        self.clear()
        self.show_score()