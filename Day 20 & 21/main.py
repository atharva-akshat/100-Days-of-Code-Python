import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

# Setting up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.listen()
screen.tracer(0)

# Objects for the classes
snake = Snake()
food = Food()
score = Score()

# Run the game code in a loop if it is not over
while True:
    screen.update()
    snake.move()

    # Listening for user input
    screen.onkeypress(snake.left, 'a')
    screen.onkeypress(snake.right, 'd')
    screen.onkeypress(snake.up, 'w')
    screen.onkeypress(snake.down, 's')
    screen.onkeypress(snake.left, 'A')
    screen.onkeypress(snake.right, 'D')
    screen.onkeypress(snake.up, 'W')
    screen.onkeypress(snake.down, 'S')
    screen.onkeypress(snake.left, 'Left')
    screen.onkeypress(snake.right, 'Right')
    screen.onkeypress(snake.up, 'Up')
    screen.onkeypress(snake.down, 'Down')

    # Displaying score
    score.show_score()

    # Waiting for 0.1s before updating the screen
    time.sleep(0.1)

    # Checking if snake ate the food and increasing the score
    if snake.body[0].distance(food) < 15:
        food.reset_food()
        snake.add_body(snake.body[-1].xcor(), snake.body[-1].ycor())
        score.points += 1

    if not snake.check():
        snake.reset()
        score.reset()

# Waiting for mouse click to close game window
# screen.exitonclick()
