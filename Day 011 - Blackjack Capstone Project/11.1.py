import random
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealt_cards = {
    "player": [2, 3],
    "dealer": [4, 5],
}

score = {
    "player": 0,
    "dealer": 0,
}


def initial_deal():
    for i in range(0, 2):
        dealt_cards["player"].append(random.choice(cards))
        dealt_cards["dealer"].append(random.choice(cards))

print(dealt_cards)

# initial_deal()
# print(cards)

# def initial_deal():
#     for i in range(0, 2):
#         my_card = random.choice(cards)
#         my_cards.append(my_card)
#         dealer_card = random.choice(cards)
#         dealer_cards.append(dealer_card)
#
#
# for card in cards:
#     my_sum += card
#
# initial_deal()
#
# for card in my_cards:
#     my_sum += card
#
# for card in dealer_cards:
#     dealer_sum += card

# print(f"You cards: {my_cards}, current_score: {my_sum}")
# print(f"Dealer's first card: {dealer_cards[0]}")
# cont = input("Would you like to hit or pass?")
#
# while keep_playing:
#     my_sum = 0
#     dealer_sum = 0
#
#     for card in my_cards:
#         my_sum += card
#
#     for card in dealer_cards:
#         dealer_sum += card
#
#     print(f"You cards: {my_cards}, current_score: {my_sum}")
#     print(f"Dealer's first card: {dealer_cards[0]}")
#     cont = input("Would you like to hit or pass?")
#
#     if cont == "pass":
#         keep_playing = False





    # for card in my_cards:
    #     player_sum = player + card
    #     return player_sum

# score_sum()
# initial_deal()
# print(my_cards)
# score_sum(my_sum)
# print(my_sum)

    # for card in dealer_cards:
    #     dealer_sum = dealer + card


    # dealer_sum = dealer_sum

    # print(dealer_sum)




# initial_deal()
# score_sum(my_sum, dealer_sum).dealer_sum
# print(dealer_cards)
# print(dealer_sum)

