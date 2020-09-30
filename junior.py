#basic rules knowledge, still some randomness on decision making.

def juniorPlayers(dictionary):
    juniorPlayers=random.randint(0,7-player) # effect of other players of the same type

    for junior in range(juniorPlayers):
        dictionary['juniorPlayer'+str(junior+1)]=generateBalance()

activePlayersDict=dict()
activePlayersDict['player']=generateBalance()

juniorPlayers(activePlayersDict)
