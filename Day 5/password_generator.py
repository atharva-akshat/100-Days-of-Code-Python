# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Write your code below this line 👇

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easyPassword = ""
for i in range(nr_letters):
    easyPassword = easyPassword + letters[random.randint(0, len(letters) - 1)]
for i in range(nr_symbols):
    easyPassword = easyPassword + symbols[random.randint(0, len(symbols) - 1)]
for i in range(nr_numbers):
    easyPassword = easyPassword + numbers[random.randint(0, len(numbers) - 1)]
print("Easy level password: ", easyPassword)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hardPassword = ''
combined = letters + symbols + numbers
random.shuffle(combined)  # Shuffle the elements in combined list
for i in range(nr_letters + nr_symbols + nr_numbers):
    hardPassword = hardPassword + combined[random.randint(0, len(combined) - 1)]
print("Hard level password: ", hardPassword)
