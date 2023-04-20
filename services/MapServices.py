from AppState import appState

class MapServices:
    def __init__(self):
        pass

    def checkMap(self):
        appState.load_state('save')
        map = appState.get_data('curMap')
        return map


    def saveMap(self, mapData):
        map_data_to_save = mapData.get_map_data()
        map_data_to_save["area_map"] = {f"{k[0]},{k[1]}": v for k, v in map_data_to_save["area_map"].items()}
        appState.set_data('curMap', map_data_to_save)
        appState.save_state('save')
    
        


mapServices = MapServices()