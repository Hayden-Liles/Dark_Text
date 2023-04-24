from AppState import appState
import random

class PlayerServices:
    def __init__(self):
        pass

    def chooseStartLocation(self, inner):
        playerLocation = tuple(map(int, random.choice(inner).split(',')))
        portalLocation = tuple(map(int, random.choice(inner).split(',')))
        if(playerLocation == portalLocation):
            playerLocation = tuple(map(int, random.choice(inner).split(',')))
            portalLocation = tuple(map(int, random.choice(inner).split(',')))
        appState.set_data('playerLocation', playerLocation)
        appState.set_data('prevCellData', ["inner", "#7C501A"])
        appState.set_data('portal', portalLocation)
        appState.save_state('save.json')

    def getPlayerLocation(self):
        playerLocation = appState.get_data('playerLocation')
        return playerLocation
    
    def checkPlayerLocation(self):
        if(self.getPlayerLocation() == None):
            return False
        else:
            return True
        
    def saveLocation(self, location):
        appState.set_data('playerLocation', location)
        appState.save_state('save.json')


playerServices = PlayerServices()