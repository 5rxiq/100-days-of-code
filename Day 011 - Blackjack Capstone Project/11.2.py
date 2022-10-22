import random

player = []
computer = []
keep_playing = True

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def appending(user):
    user.append(deal())


while keep_playing:
    player_sum = 0
    computer_sum = 0
    initial_deal = True

    if len(player) == 0:
        for i in range(0, 2):
            appending(player)
            appending(computer)
    else:
        for i in range(1):
            appending(player)

# add in logic for 11 here.

    for card in player:
        player_sum += card

    for card in computer:
        computer_sum += card

    print(f"Your cards are: {player}; Your score is {player_sum}")
    print(f"The dealer's first card is: {computer[0]}")

    if player_sum > 21:
        print("Bust!")
        keep_playing = False
    else:
        cont = input("Would you like to 'hit' or 'pass'?")

    if cont == "pass":
        print(f"Your cards are: {player}; Your score is {player_sum}")
        print(f"The dealer's cards are: {computer}; The dealer's score is {computer_sum}")
        if player_sum > computer_sum and player_sum <= 21:
            print("You won!")
        elif player_sum == computer_sum:
            print("You tied.")
        else:
            print("You lost.")
        keep_playing = False
