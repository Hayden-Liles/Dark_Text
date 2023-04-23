from AppState import appState

class LootServices:
    def __init__(self):
        pass  
    
    def generateAreaAroundPlayer(self, playerLocation):
        possibleLocations = [
            [playerLocation[0]-1, playerLocation[1]-1],
            [playerLocation[0], playerLocation[1]-1],
            [playerLocation[0]+1, playerLocation[1]-1],
            [playerLocation[0]+1, playerLocation[1]],
            [playerLocation[0]+1, playerLocation[1]+1],
            [playerLocation[0], playerLocation[1]+1],
            [playerLocation[0]-1, playerLocation[1]+1],
            [playerLocation[0]-1, playerLocation[1]],
        ]
        return possibleLocations

lootServices = LootServices()