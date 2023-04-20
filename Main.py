import random
import tkinter as tk
import customtkinter


# Constants
mSize = 624
aSize = 26
aBorder = 1
groundRatio = 0.6
maxGround = int((mSize // aSize) * (mSize // aSize) * groundRatio)

# Colors
borderColor = "grey"
voidColor = "black"
groundColor = "#7C501A"


def random_start_point():
    return random.randint(0, mSize // aSize - 1)


def generate_area_map():
    area_map = {}
    
    # Define border cells
    for i in range(mSize // aSize):
        for j in range(mSize // aSize):
            is_border = i == 0 or j == 0 or i == (mSize // aSize - 1) or j == (mSize // aSize - 1)
            if is_border:
                area_map[(i, j)] = ("outer", voidColor)

    # Generate ground cells
    current_point = (random_start_point(), random_start_point())
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


def draw_map(canvas, area_map):
    for i in range(mSize // aSize):
        for j in range(mSize // aSize):
            x1 = i * (aSize + aBorder)
            y1 = j * (aSize + aBorder)
            x2 = x1 + aSize
            y2 = y1 + aSize

            is_border = i == 0 or j == 0 or i == (mSize // aSize - 1) or j == (mSize // aSize - 1)

            if is_border:
                color = voidColor
            elif (i, j) in area_map:
                area_type, color = area_map[(i, j)]
            else:
                area_type, color = "outer", voidColor

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=borderColor)


class MapFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        canvas_width = (mSize // aSize) * (aSize + aBorder) - 3
        canvas_height = (mSize // aSize) * (aSize + aBorder) - 3

        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height)
        self.canvas.pack()

        area_map = generate_area_map()
        draw_map(self.canvas, area_map)

def change_area_color(area_map, coordinates, new_color):
    if coordinates in area_map:
        area_type, _ = area_map[coordinates]
        area_map[coordinates] = (area_type, new_color)
    else:
        print("Coordinates not found in area map.")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x800")
        self.title("Map Frame Test")

        self.map_frame = MapFrame(self)
        self.map_frame.place(relx=0.5, rely=0.025, anchor=tk.N)

if __name__ == "__main__":
    app = App()
    app.mainloop()
