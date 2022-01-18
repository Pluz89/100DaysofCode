print("Welcome to Pablo's Blackjack")
print('_____________________________')
import random
import time

# Constants

player_bank = 1000
list_tokens = []
player_bet = 0
dealer_hand = []
player_hand = []
Ace = 0
blackjack=False
player_ace=False

#1st round Face cards and Ace definition
def face_cards(current_hand):
    for card_in_hand in range(len(current_hand)):
        if 'Joker' == current_hand[card_in_hand] or 'Queen' == current_hand[card_in_hand]  or 'King' == current_hand[card_in_hand]:
            current_hand[card_in_hand] = 10
    for card_in_hand in range(len(current_hand)):
        if 'Ace' == current_hand[card_in_hand] and len(current_hand)<=2:
            current_hand[card_in_hand] = 11
            while sum(current_hand)>21:
                current_hand[card_in_hand]=1
        elif 'Ace' == current_hand[card_in_hand] and len(current_hand) > 2 and player_ace==True:#true hit is stand from dealer, false hit is player
            current_hand[card_in_hand] = 11
            while sum(current_hand) > 21:
                current_hand[card_in_hand] = 1
        elif 'Ace' == current_hand[card_in_hand] and len(current_hand) > 2 and player_ace == False:
            current_hand[card_in_hand] = 11
    return current_hand

#Dealer play stand
def dealers_play_stand(input_dealer_hand, input_dealer_score):
    print(f'Dealer hand is: {input_dealer_hand}')
    time.sleep(1)
    while input_dealer_score < 17:
        print(f'Dealer score is {input_dealer_score}, dealer must draw a card.')
        time.sleep(1)
        time.sleep(1)
        input_dealer_hand.append(played_deck[0])
        played_deck.pop(0)
        print(f'Dealer hand score: {input_dealer_hand}')
        time.sleep(1)
        player_ace=False
        face_cards(current_hand=input_dealer_hand)
        input_dealer_score=sum(input_dealer_hand)
    print(f'Dealer score is {input_dealer_score}')
    time.sleep(1)
    return input_dealer_score


original_deck = 8 * ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Joker', 'Queen', 'King', ]
played_deck = original_deck


# Token definition
def tokens(input_bank):
    total_tokens = [5, 25, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
    for max_tokens in range(len(total_tokens)):
        if total_tokens[max_tokens] <= input_bank:
            list_tokens.append(total_tokens[max_tokens])
    return list_tokens


# Betting
def bet(bet_or_help, input_player_bank, input_player_bet):
    global player_bank, player_bet
    # All in
    if bet_or_help == 'all':
        player_bet = input_player_bank
        player_bank = 0
        return f'Your bank is now ${player_bank}', f'Your bet: ${player_bet}', player_bank, player_bet
    # Manual tokens
    elif bet_or_help == 'tokens':
        selecting_tokens = True
        while selecting_tokens:
            token = int(input('Type the token \n'))
            if token in list_tokens:
                amt_tokens = int(input(f'How many tokens of ${token}? \n'))
                if token * amt_tokens > input_player_bank:
                    print('You cannot bet more than what you have in your bank!')
                elif token * amt_tokens <= input_player_bank:
                    input_player_bet += token * amt_tokens
                    player_bank -= token * amt_tokens
                    player_bet = input_player_bet
                    bet_more = input(
                        f'You have ${player_bank} left in your bank, your bet is: ${player_bet}, do you want to bet more? (Y/N)\n').lower()
                    if bet_more == 'n':
                        selecting_tokens = False

            elif token not in list_tokens:
                print('The token is not available!')
#Game definition
def game_over(is_blackjack):
    global player_bank, player_bet
    if player_score > 21:
        print('You lose!')
    elif dealer_score_stand>21 or dealer_score_stand < player_score:
        print('You win')
        if is_blackjack:
            player_bet *= 2.5
            player_bank += player_bet
        else:
            player_bet *= 2
            player_bank += player_bet
    elif dealer_score_stand == player_score:
        print('Its a draw!')
        player_bank += player_bet
    elif dealer_score_stand>player_score:
        print('You lose!')

#Player uses HIT
def dealers_play_hit(input_player_hand, input_player_score):
    global is_hit, player_ace
    while is_hit:
        input_player_hand.append(played_deck[0])
        played_deck.pop(0)
        print('You drawed a: ', input_player_hand[len(input_player_hand)-1])
        print(f'Your hand: {input_player_hand}')
        time.sleep(1)
        player_ace=True
        face_cards(current_hand=input_player_hand)
        input_player_score = sum(input_player_hand)
        print('Your score is: ', input_player_score)
        if input_player_score>20:
            is_hit=False
            return input_player_score
        elif input_player_score<=20:
            continue_hitting = input(f'Type H to hit, or type S to stand. Deck has {len(played_deck)} cards.').lower()
            if continue_hitting=='s':
                is_hit=False
                return input_player_score
while player_bank>0:
    list_tokens = []
    print(f'Your bank is ${player_bank}. How much you want to bet?.')
    print(f'These are your available tokens: {tokens(input_bank=player_bank)}')
    player_bet=0
    dealer_hand = []
    player_hand = []
    help = True
    while help:
        bet_or_help = input(
            'Type "tokens" to manually set the amount. Type "all" to go all in or type "help" to know the rules of how to play.\n')
        if bet_or_help == 'help':
            print('type the rules here')
        elif bet_or_help == 'tokens':
            help = False
        elif bet_or_help == 'all':
            help = False

    bet(bet_or_help, player_bank, player_bet)
    print(f'You have ${player_bank} left in your bank and your bet is ${player_bet}')
    print('Shuffling the deck... please wait')
    time.sleep(2)
    random.shuffle(played_deck)

    # Deal cards
    # 1st card to player
    player_hand.append(played_deck[0])
    played_deck.pop(0)
    print('Dealer gives you:\n', player_hand)
    time.sleep(1)
    # 2nd card to dealer
    dealer_hand.append(played_deck[0])
    played_deck.pop(0)
    print(f'Dealer has now:{dealer_hand}, and a folded card.')
    time.sleep(1)
    # 3rd card to player
    player_hand.append(played_deck[0])
    played_deck.pop(0)
    print('Your hand is:\n', player_hand)
    # Sum player cards
    player_score = face_cards(current_hand=player_hand)
    player_score = sum(player_score)
    print('Your score is:', player_score)
    if player_score==21:
        print('You have a BlackJack 21!, Your prize will be higher!')
        blackjack=True
    # 4th card to dealer
    dealer_hand.append(played_deck[0])
    played_deck.pop(0)
    # Sum Dealer cards
    dealer_score=face_cards(current_hand=dealer_hand)
    dealer_score=sum(dealer_score)
    print(f'Pssst.... dealer cards: {dealer_hand}, dealer score: {dealer_score}')
    must_select=True
    while must_select:
        hit_or_stand = input(f'Type H to hit, or type S to stand, the deck has now {len(played_deck)} cards.').lower()
        if hit_or_stand == 's':
            dealer_score_stand=dealers_play_stand(input_dealer_hand=dealer_hand, input_dealer_score=dealer_score)
            must_select=False
        elif hit_or_stand =='h':
            is_hit=True
            player_score=dealers_play_hit(input_player_hand=player_hand, input_player_score=player_score)
            dealer_score_stand = dealers_play_stand(input_dealer_hand=dealer_hand, input_dealer_score=dealer_score)
            must_select=False
    game_over(is_blackjack=blackjack)
    if len(played_deck)<=12:
        print('Reshuffling deck...')
        time.sleep(5)
        played_deck= 8 * ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Joker', 'Queen', 'King', ]
