from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.

print(logo)

keep_going = "Yes"
bids = {}

while keep_going == "Yes":
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))

    bids[name] = bid

    keep_going = input("Are there any other bidders? Yes / No\n")
    clear()

max_value = max(bids.values())

max_key = max(bids, key=bids.get)

print(f"Congratulations, {max_key}, you are the winner with a bid of {max_value}!")

