from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(350, 0)

    def up(self):
        if self.ycor() < 250:
            self.goto(350, y=self.ycor() + 20)

    def down(self):
        if self.ycor() > - 250:
            self.goto(350, y=self.ycor() - 20)
