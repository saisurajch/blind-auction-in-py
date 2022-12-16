from art import logo

bidding_log = {}


satisfied = True
print(logo)
while (satisfied == True):
  name = input("What is your name: ")
  bid_amount = int(input("What is your bid amount: $"))
  bidding_log[name] = bid_amount
  bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
  if(bidders == 'yes'):
    os.system('cls')
    # for windows we use 'cls', if os is linux or Mac we use 'clear'
    satisfied = True
  else:
    os.system('cls')
    # for windows we use 'cls', if os is linux or Mac we use 'clear'
    satisfied = False
    max = 0
    winner = ''
    for bidder in bidding_log:
      bid = bidding_log[bidder]
      if(bid>max):
          max = bid
          winner = bidder
    print(f"The winner is {winner} with a bid of {max}")
