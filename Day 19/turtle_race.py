import random
from turtle import Turtle, Screen

color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = [Turtle(shape='turtle') for _ in range(len(color))]
screen = Screen()
screen.setup(width=500, height=500)

userBet = screen.textinput(title="Select Turtle", prompt="Pick Turtle Colour (red / orange / yellow / green / blue / "
                                                         "purple)")

for i in range(len(color)):
    turtles[i].penup()
    turtles[i].color(color[i])
    turtles[i].goto(x=-200, y=200 - i * 80)

raceStarted = False

if userBet:
    raceStarted = True

while raceStarted:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 200:
            raceStarted = False
            turtle.goto(x=-200, y=0)
            turtle.hideturtle()
            if turtle.pencolor() == userBet:
                turtle.write("Your selected turtle won! You won the bet!")
            else:
                turtle.write(
                    "The {} turtle won. You lost the bet as you had selected {}!".format(turtle.pencolor(), userBet))
            break

screen.exitonclick()
