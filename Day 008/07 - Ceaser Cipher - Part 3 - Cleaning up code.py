alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(text,shift,direction):
    message = ""

    if direction == "decode":
        alphabet.reverse()

    for letter in text:
        index = alphabet.index(letter)
        new_index = index + shift

        if new_index > (len(alphabet)-1):
            new_index = new_index % 26

        message += alphabet[new_index]

    print(message)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text,shift,direction)