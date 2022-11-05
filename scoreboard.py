from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(x=-50, y=320)
        self.score = 0
        self.write(f"Score : {self.score}", move=False, font=FONT)

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", move=False, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=-50, y=0)
        self.write("GAME OVER", move=False, font=FONT)
