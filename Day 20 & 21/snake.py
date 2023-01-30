from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Snake:
    def __init__(self):
        self.body = []
        for i in range(3):
            self.add_body(STARTING_POS[i][0], STARTING_POS[i][1])

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].xcor(), self.body[i - 1].ycor())

        self.body[0].forward(20)

    def left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def right(self):
        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)

    def up(self):
        if self.body[0].heading() != DOWN:
            self.body[0].setheading(UP)

    def down(self):
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

    def add_body(self, x, y):
        self.body.append(Turtle(shape="circle"))
        self.body[-1].color("white")
        self.body[-1].penup()
        self.body[-1].goto((x, y))
        pass

    def check(self):
        if self.body[0].xcor() > 280 or self.body[0].xcor() < -280 or self.body[0].ycor() > 280 or self.body[
            0].ycor() < -280:
            # self.end_game("You hit the wall!")
            return False
        for seg in self.body[len(self.body)//2:]:
            if self.body[0].distance(seg) < 5:
                # self.end_game("You ate your own body!")
                return False
        return True

    # def end_game(self, condition):
    #     self.body[0].home()
    #     for i in range(len(self.body)):
    #         self.body[i].hideturtle()
    #     self.body[0].write(condition, font=FONT, align=ALIGNMENT)
    #     self.body[0].goto(0, 40)
    #     self.body[0].write("GAME OVER!", font=FONT, align=ALIGNMENT)

    def reset(self):
        for i in self.body:
            i.reset()
        self.body.clear()
        for i in range(3):
            self.add_body(STARTING_POS[i][0], STARTING_POS[i][1])
        self.body[0].goto(STARTING_POS[0][0], STARTING_POS[0][1])
