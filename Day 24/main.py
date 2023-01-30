# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
startingLetter = None

with open("Input/Names/invited_names.txt") as file:
    for name in (file.readlines()):
        names.append(name.strip())

with open("Input/Letters/starting_letter.txt") as file:
    startingLetter = file.readlines()

for name in names:
    with open("Output/ReadyToSend/letter_to_{}.txt".format(name), mode="w") as file:
        file.write(("".join(startingLetter).replace("[name]", name)))
