import random
from turtle import Turtle, Screen

from colorgram import extract

t = Turtle()
screen = Screen()
screen.colormode(255)

color = []
for c in extract("image.jpeg", 10):
    color.append((c.rgb.r, c.rgb.g, c.rgb.b))
print(color)


def dot_painting(dots_per_line, lines):
    t.penup()
    for i in range(lines):
        for _ in range(dots_per_line):
            t.dot(20, random.choice(color))
            t.forward(40)
        t.backward(40)
        if i % 2 == 0:
            t.left(90)
            t.forward(40)
            t.left(90)
        else:
            t.right(90)
            t.forward(40)
            t.right(90)
    t.hideturtle()


dot_painting(5, 5)
t.speed("fastest")
screen.exitonclick()
