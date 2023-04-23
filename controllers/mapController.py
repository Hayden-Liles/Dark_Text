import random
import tkinter as tk
import customtkinter
from services.MapServices import mapServices
from controllers.PlayerController import playerController


mSize = 624
aSize = 26
aBorder = 1
groundRatio = .6
maxGround = int((mSize // aSize) * (mSize // aSize) * groundRatio)
borderColor = "grey"
voidColor = "black"
groundColor = "#7C501A"


def setMap(map_frame):
    map_frame.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="nw")


class MapFrameController:
    def __init__(self):
        pass

    def random_start_point(self):
        return random.randint(0, mSize // aSize - 1)

    def generate_area_map(self):
        area_map = {}

        # Define border cells
        for i in range(mSize // aSize):
            for j in range(mSize // aSize):
                is_border = i == 0 or j == 0 or i == (
                    mSize // aSize - 1) or j == (mSize // aSize - 1)
                if is_border:
                    area_map[(i, j)] = ("outer", voidColor)

        # Generate ground cells
        current_point = (self.random_start_point(), self.random_start_point())
        area_map[current_point] = ("inner", groundColor)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while len([coord for coord, (area_type, _) in area_map.items() if area_type == "inner"]) < maxGround:
            dx, dy = random.choice(directions)
            x, y = current_point
            x += dx
            y += dy

            if 0 <= x < mSize // aSize and 0 <= y < mSize // aSize:
                current_point = (x, y)
                area_map[current_point] = ("inner", groundColor)

        return area_map

    def draw_map(self, canvas, area_map):
        for i in range(mSize // aSize):
            for j in range(mSize // aSize):
                x1 = i * (aSize + aBorder)
                y1 = j * (aSize + aBorder)
                x2 = x1 + aSize
                y2 = y1 + aSize

                is_border = i == 0 or j == 0 or i == (
                    mSize // aSize - 1) or j == (mSize // aSize - 1)

                if is_border:
                    color = voidColor
                elif (i, j) in area_map:
                    area_type, color = area_map[(i, j)]
                else:
                    area_type, color = "outer", voidColor

                canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color, outline=borderColor)

    def update_cell_color(self, area_map, cell, new_color):
        if cell in area_map:
            area_map[cell] = (area_map[cell][0], new_color)
        else:
            area_map[cell] = ("inner", new_color)


mapFrameController = MapFrameController()


class MapFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.map_frame_controller = MapFrameController()

        canvas_width = (mSize // aSize) * (aSize + aBorder) - 3
        canvas_height = (mSize // aSize) * (aSize + aBorder) - 3

        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height)
        self.canvas.pack()

        self.area_map = self.map_frame_controller.generate_area_map()
        self.map_frame_controller.draw_map(self.canvas, self.area_map)

    def get_map_data(self):
        return {
            "area_map": self.area_map
        }

    def load_map_data(self, map_data):
        self.area_map = {tuple(map(int, k.split(
            ','))): v for item in map_data["area_map"] for k, v in item.items()}
        self.map_frame_controller.draw_map(self.canvas, self.area_map)
        return self

    def update_cell_color(self, cell, new_color):
        self.map_frame_controller.update_cell_color(
            self.area_map, cell, new_color)
        x, y = cell
        x1 = x * (aSize + aBorder)
        y1 = y * (aSize + aBorder)
        x2 = x1 + aSize
        y2 = y1 + aSize
        self.canvas.create_rectangle(
            x1, y1, x2, y2, fill=new_color, outline=borderColor)


class MapController:
    def __init__(self):
        pass

    def checkMap(self, master):
        map = mapServices.checkMap()
        if (map == None):
            self.map_frame = self.create_map_frame(master)
            return self.map_frame
        else:
            self.map_frame = MapFrame(master)
            map = mapServices.getMap()
            setMap(self.map_frame.load_map_data(map))
            playerController.checkPlayerLocation(self.map_frame)
            return self.map_frame

    def create_map_frame(self, master):
        self.map_frame = MapFrame(master)
        mapServices.saveMap(self.map_frame)
        map = mapServices.getMap()
        setMap(self.map_frame.load_map_data(map))
        playerController.checkPlayerLocation(self.map_frame)
        return self.map_frame


mapController = MapController()
