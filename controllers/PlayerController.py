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

    def movePlayer(self, direction):
        # currentLocation = playerServices.getPlayerLocation()
        match direction:
            case "Up":
                print('Up')
            case "Down":
                print('Down')
            case "Left":
                print('Left')
            case "Right":
                print('Right')




playerController = PlayerController()