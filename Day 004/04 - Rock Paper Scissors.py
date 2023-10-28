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

#Write your code below this line 👇

options = [rock,paper,scissors]
options_english = ["Rock", "Paper", "Scissors"]

user_choice = input("Choose Rock, Paper, or Scissors: ")

if user_choice.lower() == "rock":
    user_choice = 0
elif user_choice.lower() == "paper":
    user_choice = 1 
elif user_choice.lower() == "scissors":
    user_choice = 2
else:
    user_choice = 3
    print("Incorrect selection. Please start over.")

computer_choice = random.randint(0,2)

if user_choice >= 0 and user_choice <= 2:
    print("\n" + f"You chose {options_english[user_choice]}"+ "\n")
    print(options[user_choice] + "\n")

    print("\n" + f"The Computer chose {options_english[computer_choice]}"+ "\n")
    print(options[computer_choice] + "\n")

    if user_choice == computer_choice:
        print("\n" + "You Tied! Try again.")

    if user_choice == 0 and computer_choice == 1: 
        print("\n" + "Paper beats Rock. You lose!")

    if user_choice == 0 and computer_choice == 2: 
        print("\n" + "Rock beats Scissors! You win!")

    if user_choice == 1 and computer_choice == 0: 
        print("\n" + "Paper beats Rock! You win!")

    if user_choice == 1 and computer_choice == 2: 
        print("\n" + "Scissors beats Paper! You lose!")

    if user_choice == 2 and computer_choice == 0: 
        print("\n" + "Rock beats Scissors! You lose!")

    if user_choice == 2 and computer_choice == 1: 
        print("\n" + "Scissors beats Paper! You win!")