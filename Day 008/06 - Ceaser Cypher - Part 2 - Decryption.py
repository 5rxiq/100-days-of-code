alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    encrypted = ""
    for letter in text:
        index = alphabet.index(letter)
        new_index = index + shift

        if new_index > (len(alphabet)-1):
            new_index = new_index % 26

        encrypted += alphabet[new_index]

    print(encrypted)

def decrypt(text,shift):
    decrypted = ""
    alphabet.reverse()
    for letter in text:
        index = alphabet.index(letter)
        new_index = index + shift

        if new_index > (len(alphabet)-1):
            new_index = new_index % 26

        decrypted += alphabet[new_index]

    print(alphabet)
    print(decrypted)


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
#encrypt(plain_text=text, shift_amount=shift)
#encrypt(text,shift)
#decrypt(text,shift)

if direction == "encode":
    encrypt(text,shift)
else:
    decrypt(text,shift)

