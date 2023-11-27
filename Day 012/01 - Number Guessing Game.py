import random 

#the answer
secret = random.randint(1,100)

difficulty = input("""\nWelcome to the Number Guessing Game!
\nI'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': """)

#the number of guesses remaining
guesses_remaining = 0

if difficulty == 'easy':
    guesses_remaining = 10 
else:
    guesses_remaining = 5

#the current guess
guess = 0

def gameplay():
    global secret
    global guess
    global guesses_remaining
    while int(guess) != int(secret) and guesses_remaining >0:
        print(f"\nYou have {guesses_remaining} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        
        if int(guess) == int(secret):
            print(f"{secret} is the correct number. You win!")
        elif int(guess) > int(secret):
            print("Too high. \nGuess again!")
            guesses_remaining += -1
        else:
            print("Too low. \nGuess again!")
            guesses_remaining += -1

    if guesses_remaining == 0:
        print("\nYou ran out of guesses. Game Over.")

gameplay()