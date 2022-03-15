from turtle import Turtle

FONT = ("Courier", 40, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.create_scoreboard()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.write(f"{self.l_score} - {self.r_score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.create_scoreboard()
        self.goto(0, 250)
        self.write(f"{self.l_score} - {self.r_score}", align=ALIGNMENT, font=FONT)

    def left_score(self):
        self.l_score += 1

    def right_score(self):
        self.r_score += 1

    def create_scoreboard(self):
        self.color("white")
        self.penup()
        self.hideturtle()
