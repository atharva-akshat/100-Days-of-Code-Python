from turtle import Turtle

FONT = ("Arial",30, "normal")


class ScoreBoard():
    def __init__(self, screen_y):
        y_pos = screen_y / 2 - 50
        self.scores = [Turtle() for _ in range(2)]
        self.p1 = 0
        self.p2 = 0
        for player in self.scores:
            player.points = 1
            player.color("white")
            player.hideturtle()
            player.speed("fastest")
            player.penup()
            self.scores[0].goto(-50, y_pos)
            self.scores[1].goto(50, y_pos)

    def show_score(self):
        self.scores[0].clear()
        self.scores[1].clear()
        self.scores[0].write(self.p1, font=FONT)
        self.scores[1].write(self.p2, font=FONT)

    def add_point(self,side):
        if side == 'left':
            self.p1 +=1
        else:
            self.p2 += 1
        return True
