from services.MapServices import mapServices
from services.PlayerServices import playerServices
from services.LootServices import lootServices
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
        if (check):
            self.drawPlayerLocation(master)
        else:
            self.chooseStartLocation(master)

    def drawPlayerLocation(self, master):
        playerLocation = playerServices.getPlayerLocation()
        master.update_cell_color(
            (playerLocation[0], playerLocation[1]), "green")
        map = mapServices.getMap()["area_map"]
        locations = lootServices.generateAreaAroundPlayer(playerLocation, map)
        for x in locations:
            if self.checkLocationIsVoid(tuple(x)) == None:
                pass
            else:
                master.update_cell_color((x[0], x[1]), x[2])
        mapServices.saveMap(master)

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

        newLocation = (x, y)
        location = self.checkLocationIsVoid(newLocation)
        if (location == None):
            return
        self.revertGroundColor(currentLocation, master)
        self.saveLocationDetails(location)
        # TODO add a death sequence or an option to jump into the void :P or leave it whatever your feeling
        playerServices.saveLocation(newLocation)
        self.drawPlayerLocation(master)

    def checkLocationIsVoid(self, location):
        location = list(location)

        if len(location) > 2:
            location.pop(-1)
        location = tuple(location)

        location = re.sub(r'[() ]', '', str(location))

        inner = mapServices.getInnerArea()
        check = inner.count(location)
        if (check == 0):
            return None
        return location

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
        mapServices.saveLocationDetails(cell)


playerController = PlayerController()
