from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids = {}

def highest_bidder(biddings):
	'''Finds the highest bidder'''
	highest_bid = 0
	winner = ""
	for bidder in bids:
		bid_price = bids[bidder]
		if bid_price > highest_bid:
			highest_bid = bid_price
			winner = bidder
			
	message = f"The winner is {winner} with a bid of ${highest_bid}"
	print(message)

		  
more_bidders = True
	
while more_bidders:
	name = input("what is your name? ")
	bid = int(input("What is your bid? $"))

	bids[name] = bid
	
	response = input("Are there any more bidders? Type 'yes' or 'no'\n")

	if response == "no":
		more_bidders = False
		highest_bidder(bids)
	elif response == "yes":
		clear()


