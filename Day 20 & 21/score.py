from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0, 250)

    def show_score(self):
        self.clear()
        self.write("Score: {}".format(self.points), font=FONT, align=ALIGNMENT)
