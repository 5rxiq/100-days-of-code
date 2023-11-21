#keeping the script separate from the starter as to avoid hints. 

from art import logo 
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []

player_score = 0 
dealer_score = 0

keep_dealing = True
keep_playing = True
dealer_draw = True

#start of game deal()
def start_of_game():
    for i in range(0,2):
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))

    for card in player_cards:
        global player_score 
        player_score += card 
    
    for card in dealer_cards:
        global dealer_score 
        dealer_score += card 

    print(logo)
        

def deal():
    global keep_dealing
    global player_score
    global player_cards
    global dealer_score
    global dealer_cards
    global dealer_draw

    if player_score == 21 and len(player_cards) == 2:
        player_score = 0
        keep_dealing = False

    while keep_dealing == True:

        deal_another = input(f"""
Your cards: {player_cards}, current_score: {player_score}
The computer's first card: {dealer_cards[0]}
Type 'y' to get another card, type 'n' to pass: """)
        if deal_another == 'y':
            new_card = random.choice(cards)
            player_cards.append(new_card)
            player_score += new_card 

            if player_score > 21 and 11 in player_cards:
                player_cards[player_cards.index(11)] = 1
                player_score = player_score - 10

            if player_score >= 21:
                keep_dealing = False 
        else:
            keep_dealing = False

    while dealer_draw:
        if dealer_score < 17 and player_score != 0 and player_score <= 21:
            new_card = random.choice(cards)
            dealer_cards.append(new_card)
            dealer_score += new_card 

            if dealer_score > 21 and 11 in dealer_cards:
                dealer_cards[dealer_cards.index(11)] = 1
                dealer_score = dealer_score - 10

        else:
            dealer_draw = False


def score_evaluation():
    global player_cards
    global player_score
    global dealer_cards
    global dealer_score
    print(f"""
\nYour cards: {player_cards}, current_score: {player_score}
Computer's cards: {dealer_cards}, current score: {dealer_score})""")
    
    if player_score == 0:
        print("Blackjack!")
    
    elif player_score == dealer_score:
        print("You tied!")
    
    elif player_score > 21:
        print("You busted!")

    elif dealer_score > 21:
        print("You won!")

    elif player_score > dealer_score:
        print("You won!")

    else:
        print("You lost!")

def play():
    global keep_playing
    global player_cards
    global dealer_cards
    global player_score
    global dealer_score
    global keep_dealing
    global dealer_draw

    while keep_playing:
        start_of_game()
        deal()
        score_evaluation()

        play_again = input("\nWould you like to play again? y or n: ")

        if play_again == 'n':
            keep_playing = False
            print("Thank you for playng!")

        else:
            player_cards = []
            dealer_cards = []

            player_score = 0 
            dealer_score = 0

            keep_dealing = True
            dealer_draw = True

play()


