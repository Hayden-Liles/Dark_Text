from services.MapServices import mapServices
from services.PlayerServices import playerServices
import re

class PlayerController:
    def __init__(self):
        pass

    def chooseStartLocation(self, master):
        inner = mapServices.getInnerArea()
        playerServices.chooseStartLocation(inner)
        self.drawPlayerLocation(master)

    def checkPlayerLocation(self, master):
        check = playerServices.checkPlayerLocation()
        if(check):
            self.drawPlayerLocation(master)
        else:
            self.chooseStartLocation(master)

    def drawPlayerLocation(self, master):
        playerLocation = playerServices.getPlayerLocation()
        master.update_cell_color((playerLocation[0], playerLocation[1]), "green")

    def revertGroundColor(self, location, master):
        color = mapServices.getPreviousGroundColor()
        master.update_cell_color((location[0], location[1]), color)

    def movePlayer(self, direction, master):
        currentLocation = playerServices.getPlayerLocation()
        x, y = currentLocation

        match direction:
            case "Up":
                y -= 1
            case "Down":
                y += 1
            case "Left":
                x -= 1
            case "Right":
                x += 1
        # NOTE change "currentLocation" to previous color then move then save "previous color" 
        #                                                              AKA the current locations color
        newLocation = (x, y)
        check = self.checkLocationIsVoid(newLocation)
        if(check == None):
            return
        # TODO add a death sequence or an option to jump into the void :P or leave it whatever your feeling
        self.revertGroundColor(currentLocation, master) # rename function to changeColor to last
        playerServices.saveLocation(newLocation)
        self.drawPlayerLocation(master)

    def checkLocationIsVoid(self, location):
        location = re.sub(r'[() ]', '', str(location))
        inner = mapServices.getInnerArea()
        check = inner.count(location)
        if(check == 0):
            return None
        self.saveLocationDetails(location)
        return True
    
    def findIndexInMap(self, map, coords):
        for index, item in enumerate(map):
            if coords in item:
                return index
        return -1
    
    def saveLocationDetails(self, location):
        map = mapServices.getMap()
        index = self.findIndexInMap(map["area_map"], location)
        cell = map["area_map"][index]
        cell = list(cell.values())[0]
        # TODO
        # NEED TO save the cells color
        mapServices.saveLocationDetails(cell)




playerController = PlayerController()



# NOTE DELETE

# print(f'ORGINAL: {locationData}')
#         locationIndex = locationData[0]
#         locationValues = list(locationData[1].values())[0]
#         print(f'INDEX: {locationIndex}')
#         print(f'VALUES: {locationValues}')
#         locationValues[1] = "black"
#         print(f'Changed VALUES: {locationValues}')

#         print(f'ORGINAL???: {locationData}')