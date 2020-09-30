#%%
from game import newDeck, generateBalance, deal
import random

deckFullSize=312

deck=newDeck()

def remainingDecks(currentDeck):
    #if/else statement is set to avoid rounding to zero and having no return value
    if (round(len(currentDeck)/52)) == 0:
        return 1
    else:
        return (round(len(currentDeck)/52))**-1


cardIndex = [0]
trueIndex = [cardIndex[0]*remainingDecks(deck)]


#Initial players money
MITeam = {
    "observer": 10**4,
    "bigPlayer": 10**4,
    "truePlayer": 10**4,
    "gorila": 1.5*10**4
}

MITActive = {}

def MITPlayers_Rounds(index, trueIndex):
    MITActive['observer'] = MITeam['observer']
    
    if index >=10:
        try:
          MITActive['bigPlayer'] = MITeam['bigPlayer']
        except KeyError:
          print("Key Error has occured")
    else:
        try:
          del MITActive['bigPlayer'] = MITeam['bigPlayer']
        except KeyError:
          print("Key Error has occured")

        
    if trueIndex >= 10:
        try:
          MITActive['truePlayer'] = MITeam['truePlayer']
        except KeyError:
          print("Key Error has occured")
    else:
        try:
          del MITActive['truePlayer']
        except KeyError:
          print("Key Error has occured")
          
    if index >= 8:
        try:
          MITActive['gorila'] = MITeam['gorila']
        except KeyError:
          print("Key Error has occured")
    else:
        try:
          del MITActive['gorila']
        except KeyError:
          print("Key Error has occured")

MITPlayers_Rounds(0,0)

MITmoney = lambda team: sum(team.values())

MITmoneyList = [MITmoney] #initi we only have the money start

random.shuffle(deck) #deck was shuffeled before the game started and kept the same order until the end of the cards

# Defining the bets for each round.

RoundBet = dict(zip(MITeam.keys(),[
    MITeam["observer"]*(1/100),
    MITeam["bigPlayer"]*(cardIndex[0]/100),
    MITeam["truePlayer"]*(trueIndex[0]/100),
    MITeam["gorila"]*(random.randrange(1,40)/100)
]))

def roundIndex(cardRound):
    indexRound=0
    for hand in cardRound.values(): 
        for card in hand: 
                if (card == 10 or card == "Jack" or card == "Queen" or card == "King" or card == "Ace"):indexRound += 1
                if (card == 2 or card == 3 or card == 4 or card == 5 or card == 6): indexRound -= 1
    return indexRound


def MITcards(deck):
    return map(deal, [deck]*len(MITeam.keys()))


#running simulation
counter=0
while len(deck) >= 8:
    counter += 1 #counter is set before usage because the 0th index is used in the cardIndex declaration
    RoundBet = dict(zip(MITeam.keys(),MITcards(deck)))

    cardIndex.append(roundIndex(RoundBet))
    trueIndex.append(cardIndex[counter]*remainingDecks(deck))

