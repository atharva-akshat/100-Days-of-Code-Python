from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self, screen_width, screen_height):
        self.level = 1
        self.scoreBoard = [Turtle() for _ in range(2)]
        self.scoreBoard[0].penup()
        self.scoreBoard[0].hideturtle()
        self.scoreBoard[0].color("black")
        self.scoreBoard[0].goto(-screen_width / 2 + 50, screen_height / 2 - 50)
        self.scoreBoard[1].penup()
        self.scoreBoard[1].hideturtle()
        self.scoreBoard[1].color("black")

    def show_level(self):
        self.scoreBoard[0].clear()
        self.scoreBoard[0].write("Level: {}".format(self.level), font=FONT)

    def game_over(self):
        self.scoreBoard[1].home()
        self.scoreBoard[1].write("GAME OVER", font=FONT, align="center")
