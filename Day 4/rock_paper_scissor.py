import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

game_images = [None, rock, paper, scissors]
choices = {1: "Rock", 2: "Paper", 3: "Scissor"}
player = int(input("\nWhat do you choose? (Type 1 for Rock, 2 for Paper or 3 for Scissors): "))
if player > 3 or player < 1:
    print("Invalid Choice!")
    exit()
print("\nPlayer: {}".format(choices[player]), game_images[player])
cpu = random.randint(1, 3)
print("CPU: {}".format(choices[cpu]), game_images[cpu])

if (player == 1 and cpu == 2) or (player == 2 and cpu == 3) or (player == 3 and cpu == 1):
    print("You lose!")
elif (player == 1 and cpu == 3) or (player == 3 and cpu == 2) or (player == 2 and cpu == 1):
    print("You win!")
elif player == cpu:
    print("Draw!")

####### Debugging challenge: ######### FIXED (INPUT VALIDATION ON LINE 35)
# Try running this code and type 5.
# It will give you an IndexError and point to line 32 as the issue.
# But on line 38 we are trying to prevent a crash by detecting
# any numbers greater than or equal to 3 or less than 0.
# So what's going on?
# Can you debug the code and fix it?
# Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end
