import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

# Setting up the game screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()

# Creating objects for the game
cars = CarManager(SCREEN_WIDTH, SCREEN_HEIGHT)
player = Player()
score = Scoreboard(SCREEN_WIDTH, SCREEN_HEIGHT)

game_is_on = True
while game_is_on:

    # Displaying the level
    score.show_level()

    # Checking for collision
    for car in cars.cars:
        if player.distance(car) <= 20:
            game_is_on = False

    # Listening for user input
    screen.onkeypress(player.move_up, "Up")
    screen.onkeypress(player.move_down, "Down")
    screen.onkeypress(player.move_up, "W")
    screen.onkeypress(player.move_down, "S")
    screen.onkeypress(player.move_up, "w")
    screen.onkeypress(player.move_down, "s")

    # Moving cars
    cars.move(SCREEN_WIDTH)

    # Checking if player has crossed the road
    if player.next_level():
        cars.cars_pos(SCREEN_WIDTH)
        cars.increase_speed()
        score.level += 1

    # Updating the Turtle graphics Screen
    screen.update()
    time.sleep(0.1)

score.game_over()
screen.exitonclick()
