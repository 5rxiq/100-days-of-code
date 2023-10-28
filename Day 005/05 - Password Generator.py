import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pw_selection = []

# for each user input, this will randomly grab the desired numbers of characters from each list and 
# apenend them to the pw_selection list 
for i in range(0,nr_letters):
    pw_selection.append(letters[random.randint(0,len(letters)-1)])

for i in range(0,nr_symbols):
    pw_selection.append(symbols[random.randint(0,len(symbols)-1)])

for i in range(0,nr_numbers):
    pw_selection.append(numbers[random.randint(0,len(numbers)-1)])

#print(pw_selection)

password = []

# For randomizing the characters, a new list, password, is created.
# This will grab a random character from pw_selection and appened it to password. 
# Then it will remove that character from pw_selection. 
# This loops until pw_selection is empty
for i in range(0,len(pw_selection)):
    character = int(random.randint(0,len(pw_selection)-1))
    password.append(pw_selection[character])
    pw_selection.remove(pw_selection[character])

#This transforms the list into a string
pw_output = ""
for char in password:
    pw_output += char

print("\n" + f"Your password is: {pw_output}")