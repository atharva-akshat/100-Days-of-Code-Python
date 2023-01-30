import turtle

import pandas


class States:
    def __init__(self):
        self.turtles = {}
        self.data = pandas.read_csv("50_states.csv")
        self.revealed = []
        self.incorrect_guess = []
        for i in range(len(self.data)):
            self.turtles[self.data["state"][i]] = turtle.Turtle(shape="circle")
            self.turtles[self.data["state"][i]].color("red")
            self.turtles[self.data["state"][i]].penup()
            self.turtles[self.data["state"][i]].goto(self.data["x"][i], self.data["y"][i])

    def reveal_answer(self, state):
        self.turtles[state].clear()
        self.turtles[state].hideturtle()
        self.turtles[state].write(state)
        self.revealed.append(state)
