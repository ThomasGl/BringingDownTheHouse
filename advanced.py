#all rules knowledge, full usage of the statistics on the game, yet no memory usage on the players behalf

def advancedPlayers(dictionary):
    advancedPlayers=random.randint(0,7-player) # effect of other players of the same type

    for advanced in range(advancedPlayers):
        dictionary['advancedPlayer'+str(advanced+1)]=generateBalance()

activePlayersDict=dict()
activePlayersDict['player']=generateBalance()

advancedPlayers(activePlayersDict)
