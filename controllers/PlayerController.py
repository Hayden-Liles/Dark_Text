from services.MapServices import mapServices
from controllers.MapController import MapFrame
import random

class PlayerController:
    def __init__(self):
        pass

    def chooseStartLocation(self, master):
        inner = mapServices.getInnerArea()
        randomLocation = tuple(map(int, random.choice(inner).split(',')))
        master.update_cell_color((randomLocation[0], randomLocation[1]), "green")
        # master.update_cell_color((23, 7), "green")



playerController = PlayerController()