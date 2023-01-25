import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y_move = None
        self.move_speed = None
        self.x_move = None
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])
        self.reset_ball()

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.move_speed = 0.1
        self.home()
        self.bounce_x()
