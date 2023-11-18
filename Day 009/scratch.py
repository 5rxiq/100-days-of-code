bids = [{'name': 'Cam', 'bid': '1000'}, {'name': 'Josh', 'bid': '72'}, {'name': 'Andy', 'bid': '47'}]

highest_bid = float(0)
highest_bidder = ""

for dict in bids:
    #print(dict)
    #print(dict["bid"])
    #print(dict["name"])
    if float(dict["bid"]) >= highest_bid:
        highest_bid = float(dict["bid"])
        highest_bidder = dict["name"]

print (highest_bidder)