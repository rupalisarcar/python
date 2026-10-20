from food import Food
ALIGNMENT = "center"
FONT= ("Courier",10, "normal")
class Scoreboard(Food):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        
        self.hideturtle()
        self.goto(0,280)
        self.show_score()
        
    def show_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def updated_score(self):
        self.score+=1    
        self.clear()
        self.show_score()

    def quit_game(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
 