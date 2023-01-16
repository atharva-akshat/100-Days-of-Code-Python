# Importing libraries and packages
import random

import art
from game_data import data


# Function to display item
def display(pos, x):
    print("Option {} -> Name: {} | Description: {} | Country: {}".format(
        pos, data[x]['name'], data[x]['description'], data[x]['country']))


# Function to check the user's answer
def check(a, b, score):
    if data[a]['follower_count'] > data[b]['follower_count']:
        score = score + 1
        print("\nCorrect Answer! | Score:", score)
        return True, score
    else:
        print("\nWrong Answer! | Final Score:", score)
        return False, score


# Function to select items from list
def select(a, b):
    if a == -1:
        a = random.randint(0, len(data) - 1)
        b = random.randint(0, len(data) - 1)
        # If both the picks are same, change the second one
        while a == b:
            b = random.randint(0, len(data) - 1)
    else:
        a = b
        while b == a:
            b = random.randint(0, len(data) - 1)
    return a, b


def game():
    print(art.logo)

    # Random first pick
    first = -1

    # Random second pick
    second = -1

    score = 0
    correct = True
    while correct:
        first, second = select(first, second)
        display('A', first)
        print(art.vs)
        display('B', second)
        choice = input("Which one has more Instagram followers? (A/B): ")
        if choice == 'A':
            correct, score = check(first, second, score)
        elif choice == 'B':
            correct, score = check(second, first, score)
        else:
            print("Wrong choice! Exiting...")
            break


game()
