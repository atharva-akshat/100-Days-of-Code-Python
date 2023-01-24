import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.penup()
        self.reset_food()

    def reset_food(self):
        self.goto((random.randint(-250, 250), random.randint(-250, 250)))
