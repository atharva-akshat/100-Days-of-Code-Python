import csv
import turtle

import pandas as pandas

from state_manager import States

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("Guess the state")
screen.addshape(IMAGE)
turtle.shape(IMAGE)
screen.listen()
screen.tracer(0)

data = pandas.read_csv("50_states.csv")

score = 0
count = 0

state = States()
answer = ''


def click_coordinates(x, y):
    global score, answer
    answer = screen.textinput(title="{}/{} Guessed Correctly".format(
        score, len(state.turtles)), prompt="Enter name of the state")
    check_answer(answer, x, y)


def check_answer(guess, x, y):
    global score, count
    for point in state.turtles:
        if state.turtles[point].distance(x, y) < 10:
            correct_answer = point
            if correct_answer not in state.revealed:
                count += 1
                if correct_answer == guess.title():
                    score += 1
                state.reveal_answer(correct_answer)
                turtle.update()


while len(state.revealed) < 50:
    turtle.update()
    screen.onclick(click_coordinates)
    if answer == "exit":
        for s in state.data["state"]:
            if s not in state.revealed:
                state.incorrect_guess.append([s])
        with open("state_to_learn.csv", mode="w") as file:
            writer = csv.writer(file)
            writer.writerow(["State"])
            writer.writerows(state.incorrect_guess)
        break

screen.exitonclick()
