from food import Food
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal") 
class Scoreboard(Food):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.goto(0,280)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()        
        self.write(f"Score : {self.score} High Score : {self.high_score}", False, align=ALIGNMENT, font= FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", False, align=ALIGNMENT, font= FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()


    def increase_score(self):
        self.score+=1
        self.clear()
        self.write_score()
