from AppState import appState
import random

class LootServices:
    def __init__(self):
        pass  
    
    def generateAreaAroundPlayer(self, playerLocation, map):
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
        filteredList = []
        for x in map:
            for coords in x:
                for a in possibleLocations:
                    myStr = str(a).replace('[', "").replace(']', "").replace(' ', "")
                    if myStr == coords and x[coords][1] == 'gray':
                        filteredList.append(a)

        options = {
            "#7C501A": 0.8,
            "yellow": 0.02,
            "red": 0.1
        }
        for i in range(len(filteredList)):
            filteredList[i].append(random.choices(list(options.keys()), weights=list(options.values()))[0])
        return filteredList

lootServices = LootServices()