import art
import os
# HINT: You can call clear() to clear the output in the console.
bids = {}
restart = 1
while restart == 1:
    print(art.text, art.logo)
    print("Welcome to the Secret Auction!")
    name = input("Enter Name: ")
    bid = float(input("Enter Bid: "))
    bids.update({name: bid})
    if input("Add/Update Bidder? (y/n)") == 'y':
        _ = os.system('cls')
    else:
        restart = 0
        for k in bids:
            if bids[k] == max(bids.values()):
                print(art.sold)
                print("\nThe winner is {}!".format(k))
