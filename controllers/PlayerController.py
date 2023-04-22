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

    def changeColorToGround(self, location, master):
        master.update_cell_color((location[0], location[1]), "#7C501A")

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
        if(not check):
            return
        # TODO add a death sequence or an option to jump into the void :P or leave it whatever your feeling
        self.changeColorToGround(currentLocation, master)
        playerServices.saveLocation(newLocation)
        self.drawPlayerLocation(master)

    def checkLocationIsVoid(self, location):
        location = re.sub(r'[() ]', '', str(location))
        inner = mapServices.getInnerArea()
        check = inner.count(location)
        if(check == 0):
            return False
        return True
    
    def saveLocationColor(self, location):
        pass
        
        




playerController = PlayerController()