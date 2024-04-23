import os
clear = lambda: os.system('clear')

end_auction = False

bidders = {}

def find_highest_bidder():
    max_bid = {
        'name': '',
        'bid': 0
    }
    for bid in bidders:
        if bidders[bid] > max_bid['bid']:
            max_bid['name'] = bid
            max_bid['bid'] = bidders[bid]
    
    clear()
    print(f"The highest bid is from {max_bid['name']} with {max_bid['bid']} $.")
            
while not end_auction:
    clear()
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))
    
    bidders[name] = bid
    
    end = input("Are there more bidders? (yes/no) ")
    
    if end == "no":
        end_auction = True
        find_highest_bidder()
        