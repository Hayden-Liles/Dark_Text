from services.MapServices import mapServices
from services.PlayerServices import playerServices

class PlayerController:
    def __init__(self):
        pass

    def chooseStartLocation(self, master):
        inner = mapServices.getInnerArea()
        playerServices.chooseStartLocation(inner)
        self.changePlayerLocation(master)

    def checkPlayerLocation(self, master):
        check = playerServices.checkPlayerLocation()
        if(check):
            self.changePlayerLocation(master)
        else:
            self.chooseStartLocation(master)

    def changePlayerLocation(self, master):
        playerLocation = playerServices.getPlayerLocation()
        master.update_cell_color((playerLocation[0], playerLocation[1]), "green")
        pass




playerController = PlayerController()