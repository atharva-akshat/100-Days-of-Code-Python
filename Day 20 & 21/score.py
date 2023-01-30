import os.path
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
FILE_NAME = "highScore.txt"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        if os.path.isfile("./"+FILE_NAME):
            with open(FILE_NAME) as file:
                self.highScore = int(file.read())
        else:
            self.highScore = 0
        self.points = 0
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0, 250)

    def show_score(self):
        self.clear()
        self.write("High Score: {} | Score: {}".format(self.highScore, self.points), font=FONT, align=ALIGNMENT)

    def reset(self):
        if self.points > self.highScore:
            self.highScore = self.points
            with open(FILE_NAME, mode="w") as file:
                file.write(str(self.highScore))
        self.points = 0
