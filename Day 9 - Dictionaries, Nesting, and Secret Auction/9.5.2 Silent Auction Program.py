from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.

print(logo)

keep_going = "Yes"
bids = {}


def highest_bid(bid_list):
    top_bid = 0
    top_bidder = ""

    for key in bid_list:
        if bid_list[key] > top_bid:
            top_bid = bid_list[key]
            top_bidder = key
    print(top_bid)
    print(top_bidder)
    print(f"The top bidder is {top_bidder} with a winning bid of {top_bid}!")


while keep_going == "Yes":
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))

    bids[name] = bid

    keep_going = input("Are there any other bidders? Yes / No\n")
    clear()

highest_bid(bids)

