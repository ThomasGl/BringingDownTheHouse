#%%
from game import newDeck, generateBalance
import random

player=1 #assumed you are playing alone

def drunkPlayers(dictionary):
    drunkPlayers=random.randint(0,7-player) # effect of other players of the same type

    for drunk in range(drunkPlayers):
        dictionary['drunkPlayer'+str(drunk+1)]=generateBalance()

activePlayersDict=dict()
activePlayersDict['player']=generateBalance()

drunkPlayers(activePlayersDict)

def betValue(money):
    return random.randrange(50,money,50)

playersbet = list(map(betValue,activePlayersDict.values()))
RoundBet = dict(zip(activePlayersDict.keys(),playersbet))

surviving_rounds=0

# while sum(activePlayersDict.values())>0:


# print(activePlayersDict)
# currentDeck=NewDeck()