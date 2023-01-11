############### Blackjack Project #####################
import os
import random

import art

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

user = []
computer = []
user_score = 0
computer_score = 0
end = True


def add_card(a):
    add = cards[random.randint(0, len(cards) - 1)]
    if add == 11 and sum(a) + add > 21:
        a.append(1)
    else:
        a.append(add)


def start():
    global end
    end = False
    user.clear()
    computer.clear()
    _ = os.system('cls')
    print(art.logo)
    for i in range(2):
        add_card(user)
        add_card(computer)
    compare(sum(user), sum(computer))
    if not end:
        print("Computer's first card: ", computer[0])


def compare(a, b):
    global end
    if not end:
        if sum(user) == 21:
            print("\nYou have Blackjack!!")
            print("You Won!")
            end = True
        elif sum(computer) == 21 and len(computer) == 2:
            print("\nComputer has Blackjack!!")
            print("You Lost!")
            end = True
    else:
        if a == b:
            print("\nIts a draw!")
            end = True
        elif 21 >= a > b or b > 21 > a or (21 < a < b and b > 21):
            print("\nYou Won!")
            end = True
        elif 21 >= b > a or a > 21 > b or (21 < b < a and a > 21):
            print("\nYou Lost!")
            end = True
    if end:
        print("Computer's cards: ", computer, "| Computer's total: ", b)
        print("Your cards: ", user, "| Your total: ", a)


while input("\nStart a game of Blackjack? (y/n): ") == 'y':
    if end:
        start()
        user_score, computer_score = sum(user), sum(computer)
    if not end:
        while not end:
            print("Your cards: ", user, "| Your total: ", user_score)
            while computer_score < 17:
                add_card(computer)
                computer_score = sum(computer)
            if input("Pick card? (y/n): ") == 'y':
                add_card(user)
                user_score = sum(user)
            else:
                end = True
        compare(user_score, computer_score)
print("Exiting!")

# Download and read this flow chart
# https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
