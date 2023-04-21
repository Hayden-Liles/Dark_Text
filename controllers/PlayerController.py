from services.MapServices import mapServices
from services.PlayerServices import playerServices

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
        self.changeColorToGround(currentLocation, master)

        match direction:
            case "Up":
                y -= 1
            case "Down":
                y += 1
            case "Left":
                x -= 1
            case "Right":
                x += 1

        newLocation = (x, y)
        playerServices.saveLocation(newLocation)
        self.drawPlayerLocation(master)




playerController = PlayerController()