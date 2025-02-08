import silent_auction_art
print(art.logo)


def find_highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        if bidding_dict[bidder] > highest_bid:
            highest_bid = bidding_dict[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids_dict = {}
should_continue = True
while should_continue:
    name =input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bids_dict[name] = bid
    should_continue = input("Would you like to bid another bid? y/n: ").lower()
    if should_continue == "n":
        should_continue = False
        find_highest_bidder(bids_dict)
    elif should_continue == "y":
        should_continue = True
        print("\n" * 100)
