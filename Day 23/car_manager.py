import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self, screen_width, screen_height):
        self.speed = STARTING_MOVE_DISTANCE
        self.lanes = range(-screen_height // 2 + 100, screen_height // 2 - 100, 20)
        self.cars = [Turtle(shape="square") for _ in range(len(self.lanes))]
        for i in range(len(self.lanes)):
            self.cars[i].color(random.choice(COLORS))
            self.cars[i].penup()
            self.cars[i].setheading(180)
            self.cars[i].shapesize(stretch_len=2, stretch_wid=0.8)
        self.cars_pos(screen_width)

    def move(self, screen_width):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -screen_width / 2:
                car.goto(screen_width / 2, car.ycor())

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def cars_pos(self, screen_width):
        for i in range(len(self.lanes)):
            self.cars[i].goto(random.randint(-screen_width / 2, screen_width / 2), self.lanes[i])
