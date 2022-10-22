import random

player = []
computer = []
keep_playing = True
cont = None


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

        if 11 in player:
            player.remove(11)
            player.append(1)

    for card in player:
        player_sum += card

    for card in computer:
        computer_sum += card

    print(f"\nYour cards are: {player}; Your score is {player_sum}")

    if player_sum > 21:
        print(f"The dealer's cards are: {computer}; The dealer's total is {computer_sum}")
        print("Bust!")
        keep_playing = False
    elif player_sum == 21 and computer_sum < 21:
        print(f"The dealer's cards are: {computer}; The dealer's total is {computer_sum}")
        print("You win!")
        keep_playing = False
    elif player_sum == 21 and computer_sum == 21:
        print(f"The dealer's cards are: {computer}; The dealer's total is {computer_sum}")
        print("You tied!")
        keep_playing = False
    else:
        print(f"The dealer's first card is: {computer[0]}")
        cont = input("Would you like to 'hit' or 'pass'? ")

    if cont == "pass":
        print(f"\nYour cards are: {player}; Your total is {player_sum}")
        print(f"The dealer's cards are: {computer}; The dealer's total is {computer_sum}")
        if computer_sum < player_sum <= 21:
            print("You won!")
        elif player_sum == computer_sum:
            print("You tied.")
        else:
            print("You lost.")
        keep_playing = False
