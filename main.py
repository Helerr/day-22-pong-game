from turtle import Turtle, Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

paddle = Paddle()

screen.update()
time.sleep(0.01)

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

screen.exitonclick()