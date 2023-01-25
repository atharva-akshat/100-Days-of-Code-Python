import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

leftPaddle = Paddle(-350, 0)
rightPaddle = Paddle(350, 0)
ball = Ball()
score = ScoreBoard(SCREEN_HEIGHT)


def game():
    time.sleep(ball.move_speed)
    screen.onkeypress(leftPaddle.go_up, 'w')
    screen.onkeypress(leftPaddle.go_down, 's')
    screen.onkeypress(leftPaddle.go_up, 'W')
    screen.onkeypress(leftPaddle.go_down, 'S')
    screen.onkeypress(rightPaddle.go_up, 'Up')
    screen.onkeypress(rightPaddle.go_down, 'Down')
    ball.move()

    # Bouncing when ball hits the upper/lower wall
    if ball.ycor() < -270 or ball.ycor() > 270:
        ball.bounce_y()

    # Bouncing when ball collides with the paddle
    if (ball.distance(rightPaddle) <= 50 and 340 > ball.xcor() > 320) or (
            ball.distance(leftPaddle) <= 50 and -340 < ball.xcor() < -320):
        ball.bounce_x()

    # Adding points
    # Right paddle missed
    if ball.xcor() > 340:
        score.add_point("left")
        ball.reset_ball()

    # Left paddle missed
    if ball.xcor() < -340:
        score.add_point("right")
        ball.reset_ball()

    score.show_score()

    screen.update()


while True:
    game()

# screen.exitonclick()
