# Number Guessing Game Objectives:
import random

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import art

print(art.logo)
lives = 0
num = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")
if input("Select Difficulty (easy/hard): ") == "easy":
    lives = 10
else:
    lives = 5
print("You have {} attempts!".format(lives))
while lives > 0:
    guess = int(input("\nMake a guess: "))
    if guess == num:
        print("\nYou got it! The number was", num)
        break
    elif guess > num:
        print("Your guess is high")
    elif guess < num:
        print("Your guess is low")
    lives = lives - 1
    print("You have {} attempts remaining!".format(lives))

if lives == 0:
    print("\nNo more attempts, you lose!")
    print("The correct number was", num)
