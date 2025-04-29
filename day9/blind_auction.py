list = []

def calc_highest_bidder():
    highest_bidder = ''
    highest_bid = 0

    for bidder in list:
        if (bidder['bid'] > highest_bid):
            highest_bid = bidder['bid']
            highest_bidder = bidder['name']
        else:
            ''
    print(f"{highest_bidder} has won the auction with a bid of £{highest_bid}")

def enter_bid():
    name = input('What is your name?')
    bid = int(input('What is your bid?'))
    list.append({'name': name, 'bid': bid})

    next_bidder = input('Is there another bidder?')

    if (next_bidder == 'yes'):
        print('\n' * 20)
        enter_bid()
    else:
        print('\n' * 20)
        calc_highest_bidder()

print('Blind Auction App')
print('......')
enter_bid()