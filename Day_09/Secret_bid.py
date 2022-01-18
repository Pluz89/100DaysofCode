from replit import clear

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
print('Welcome to Secret Bid Auction')
dictionary = []
amount = []
max_bid = 0
def secret_bid_dictionary(input_name, input_bid):
    global max_bid, max_bidder
    new_bidder={
        'Name':input_name,
        'Bid:':input_bid,
    }
    dictionary.append(new_bidder)
    for qty_of_bidders in range(len(dictionary)):
        amount=dictionary[qty_of_bidders]['Bid:']
        if amount > max_bid:
            max_bid=amount
            max_bidder=dictionary[qty_of_bidders]['Name']
keep_bid=True

while keep_bid:
    #Make questions
    name = input('Please introduce your name: \n')
    bid_amount = int(input('What is your bid amount? \n$'))
    #Add to dictionary
    secret_bid_dictionary(input_name = name, input_bid = bid_amount)
    #Ask if more
    more_ppl = input('Are there any other bidders? Type "Yes" or "No"').lower()
    if more_ppl == 'no':
        keep_bid=False
    clear()

clear()
print(f'The winner is {max_bidder} with a bid amount of ${max_bid}')
#print(dictionary[0]['Bid:'])
# print(max(dictionary[0][max()]))
#HINT: You can call clear() to clear the output in the console.

