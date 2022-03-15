from turtle import Turtle

FONT = ("Arial", 120, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.write(f"Score - Left:{self.l_score} - Right:{self.r_score}")

    def left_score(self):
        self.l_score += 1

    def right_score(self):
        self.r_score += 1