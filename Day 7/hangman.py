# Step 5

# Update the word list to use the 'word_list' from hangman_words.py
import random

from hangman_words import word_list

# Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Import the stages from hangman_art.py and make this error go away.
# Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages

word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Starting hint
initial = random.randint(0, word_length - 1)

# Create blanks
display = [None] * word_length

# Initialise the game with starting letters revealed
for i in range(word_length):
    if chosen_word[i] == chosen_word[initial]:
        display[i] = chosen_word[initial]
    else:
        display[i] = "_"

print(" ".join(display))

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print("Guessed letter {} has already been revealed".format(guess))
        continue

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            print("You guessed {}, that's in the word!.".format(guess))

    # Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print("You guessed {}, that's not in the word. You lose a life.".format(guess))

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(' '.join(display))

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        break

    print(stages[lives])
