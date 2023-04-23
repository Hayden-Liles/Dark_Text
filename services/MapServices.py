from AppState import appState


class MapServices:
    def __init__(self):
        pass

    def checkMap(self):
        appState.load_state('save.json')
        map = appState.get_data('curMap')
        return map

    def saveMap(self, mapData):
        map_data_to_save = mapData.get_map_data()
        for coords, data in map_data_to_save["area_map"].items():
            coords_list = list(coords)
            xCord, yCord = coords_list[0], coords_list[1]
            if xCord == 23 or xCord == 0 or yCord == 23 or yCord == 0:
                map_data_to_save["area_map"][coords] = ['outer', 'black']

        area_map_list = [{f"{k[0]},{k[1]}": v} for k, v in map_data_to_save["area_map"].items()]

        map_data_to_save["area_map"] = area_map_list
        appState.set_data('curMap', map_data_to_save)
        appState.save_state('save.json')

    def getMap(self):
        map = appState.get_data('curMap')
        return map

    def getInnerArea(self):
        map = self.getMap()
        inner = []
        for x in map["area_map"]:
            for a, b in x.items():
                if b[0] == "inner":
                    inner.append(a)
        return inner
    
    def saveLocationDetails(self, cell):
        appState.set_data('prevCellData', cell)
        appState.save_state('save.json')

    def getPreviousGroundColor(self):
        color = appState.get_data('prevCellData')[1]
        return color



mapServices = MapServices()