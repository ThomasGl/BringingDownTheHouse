#%%

import os
import random
import numpy as np
# pesquisar itertools

decks = 6 #classic setup of a blackjack game in a casino

def generateBalance():
    return random.randint(1,10)*1000 #random values between 1k and 10k USD

# user chooses number of decks of cards to use
def newDeck():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]*(decks)*4


def deal(deck):
    hand = []
    for i in range(2):
        card = deck.pop()
        hand.append(card)
    return hand

deck = newDeck()
random.shuffle(deck) #deck was shuffeled before the game started and kept the same order until the end of the cards

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += card
    return total

def hit(hand):
    card = currentDeck.pop()
    hand.append(card)
    return hand

def split(hand):
    hand = {'first':hand[0], 'second':hand[1]}
    hand['first']=hand['first']+currentDeck.pop()
    hand['second']=hand['second']+currentDeck.pop()

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()

    print("\n    WELCOME TO BLACKJACK!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-"*30+"\n")
    print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Congratulations! You got a Blackjack!\n")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Sorry, you lose. The dealer got a blackjack.\n")
        losses += 1
        play_again()

def score(dealer_hand, player_hand):
        # score function now updates to global win/loss variables
        global wins
        global losses
        if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Congratulations! You got a Blackjack!\n")
            wins += 1
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Sorry, you lose. The dealer got a blackjack.\n")
            losses += 1
        elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Sorry. You busted. You lose.\n")
            losses += 1
        elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Dealer busts. You win!\n")
            wins += 1
        elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
            losses += 1
        elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Congratulations. Your score is higher than the dealer. You win\n")
            wins += 1

def game():
    
    currentDeck = random.shuffle(decks) #deck was shuffeled before the game started and kept the same order until the end of the cards

    #start loop here
    
    #assumed rules:

    #   - only one person can play at a time 


    if len(currentDeck)>4*(players+extraPlayers+1):

        extraPlayersList = []
        for extra in range(extraPlayers):
            extraPlayersList.append(deal(currentDeck))

        dealer_hand = deal(deck)
        player_hand = deal(deck)


        print ("The dealer is showing a " + str(dealer_hand[0]))
        print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand)
        quit=False
        while not quit:
            choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
            if choice == 'h':
                hit(player_hand)
                print(player_hand)
                print("Hand total: " + str(total(player_hand)))
                if total(player_hand)>21:
                    print('You busted')
                    losses += 1
                    play_again()
            elif choice=='s':
                while total(dealer_hand)<17:
                    hit(dealer_hand)
                    print(dealer_hand)
                    if total(dealer_hand)>21:
                        print('Dealer busts, you win!')
                        wins += 1
                        play_again()
                score(dealer_hand,player_hand)
                play_again()
            elif choice == "q":
                print("Bye!")
                quit=True
                exit()

    else:
        currentDeck=NewDeck()

if __name__ == "__main__":
   game()
