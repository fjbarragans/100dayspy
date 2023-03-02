import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")

bids = {}
restart = True

def highest_bidder(bids_record):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bids_record:
        bid_amount = bids_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

while restart:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    other_bidder = input("Are there any other bidder?: \n")
    other_bidder = other_bidder.lower()
    if other_bidder == "no":
        restart = False
        os.system('cls')
        highest_bidder(bids)
    elif other_bidder == "yes":
        os.system('cls')
