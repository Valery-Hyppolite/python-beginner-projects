# blind auction is a program that let's everyone bet in private and announce the winner, the person who pkace the highest price.

from replit import clear
from art import logo

print(logo)
auction = {}
max_price = 0
winner = ""
finish_bidding = False

while not finish_bidding :
    print(logo)
    name = str(input("what is your name?: "))
    if name.isdigit():
        print("Ivalid name, name shoud not contain only numbers. Try again")
    else:
            bid_price =(input('How much you want to bid?: $'))
            if bid_price.isdigit():
                bid_price1 = float(bid_price)
                auction[name] = bid_price1
            else:
                print("Ivalid number, price shoud only contain numbers. Try again")
    
        
    #print(auction)

    option = input("are there any other bidders type 'yes' or 'no' ")
    if option =='no':
        finish_bidding == True
        for name in auction:
            amount_bid= auction[name]
            if max_price < amount_bid:
                max_price = amount_bid
                winner = name
    
        print(f"the winning is {winner} with a bid price of {max_price}")
    elif option == 'yes':
        clear()
