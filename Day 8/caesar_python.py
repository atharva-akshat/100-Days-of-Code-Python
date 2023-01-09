# Import and print the logo from art.py when the program starts.
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

def encrypt(text, shift):
    encrypted = []
    for i in text:
        # What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if i in alphabet:
            if alphabet.index(i) + shift > 25:
                encrypted.append(alphabet[shift - (25 - alphabet.index(i)) - 1])
            else:
                encrypted.append(alphabet[alphabet.index(i) + shift])
        else:
            encrypted.append(i)
    return ''.join(encrypted)


##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# e.g.
# cipher_text = "mjqqt"
# shift = 5
# plain_text = "hello"
# print output: "The decoded text is hello"
def decrypt(text, shift):
    decrypted = []
    for i in text:
        if i in alphabet:
            if alphabet.index(i) - shift < 0:
                decrypted.append(alphabet[26 - (shift - alphabet.index(i))])
            else:
                decrypted.append(alphabet[alphabet.index(i) - shift])
        else:
            decrypted.append(i)
    return ''.join(decrypted)


# Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(text, shift, direction):
    if direction == 'encode':
        print("Encrypted Message: {}".format(encrypt(text, shift)))
    else:
        print("Decrypted Message: {}".format(decrypt(text, shift)))


# Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
restart = 'yes'
while restart == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()

    # What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    shift = int(input("Type the shift number: "))
    if shift > 26:
        shift = shift % 26
    caesar(text, shift, direction)
    restart = input("Restart program?(yes/no): ")
