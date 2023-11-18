import os
import art

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

print(art.logo)
bids = []

def first_bid():
    your_name = input("What is your name?: ")
    your_bid = input("What is your bid?: $")

    my_bid = {}
    my_bid["name"] = your_name
    my_bid["bid"] = your_bid
    bids.append(my_bid)
    #print(bids)

def following_bids():
    clear()
    their_name = input("What is their name?: ")
    their_bid = input("What is their bid?: $")

    following_bid = {}
    following_bid["name"] = their_name
    following_bid["bid"] = their_bid
    bids.append(following_bid)
    #print(bids)

def highest_bidder():
    highest_bid = 0
    highest_bidder = ""

    for dict in bids:
        if float(dict["bid"]) >= highest_bid:
            highest_bid = float(dict["bid"])
            highest_bidder = dict["name"]

    clear()
    print (f"{highest_bidder} is the highest bidder ")
    print(bids)


first_bid()

subsequent_bids = True

while subsequent_bids == True:
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if other_bidders.lower() == "no":
        subsequent_bids = False 
        highest_bidder()
    else:
        following_bids()





