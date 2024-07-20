from turtle import Turtle


ALIGNMENT = "left"
FONT = ("Courier", 24, "bold")
GAME_OVER_FONT = ('impact', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(x=-280, y=255)
        self.write(arg= f"Level: {self.level}", align= ALIGNMENT, font= FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.color("limegreen")
        self.write(arg= "GAME OVER", align= "center", font= GAME_OVER_FONT)