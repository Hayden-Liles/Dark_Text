import tkinter as tk
import random

# Constants
MAP_SIZE = 624
AREA_SIZE = 26
BORDER_SIZE = 1
INNER_AREA_RATIO = 0.6
MAX_INNER_AREA = int((MAP_SIZE // AREA_SIZE) * (MAP_SIZE // AREA_SIZE) * INNER_AREA_RATIO)

# Colors
BORDER_COLOR = "light grey"
OUTER_AREA_COLOR = "black"
INNER_AREA_COLOR = "#7C501A"

def random_start_point():
    return random.randint(0, MAP_SIZE // AREA_SIZE - 1)

def generate_area_map():
    area_map = {}
    
    for i in range(MAP_SIZE // AREA_SIZE):
        for j in range(MAP_SIZE // AREA_SIZE):
            is_border = i == 0 or j == 0 or i == (MAP_SIZE // AREA_SIZE - 1) or j == (MAP_SIZE // AREA_SIZE - 1)
            if is_border:
                area_map[(i, j)] = ("outer", OUTER_AREA_COLOR)

    current_point = (random_start_point(), random_start_point())
    area_map[current_point] = ("inner", INNER_AREA_COLOR)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while len([coord for coord, (area_type, _) in area_map.items() if area_type == "inner"]) < MAX_INNER_AREA:
        dx, dy = random.choice(directions)
        x, y = current_point
        x += dx
        y += dy

        if 0 <= x < MAP_SIZE // AREA_SIZE and 0 <= y < MAP_SIZE // AREA_SIZE:
            current_point = (x, y)
            area_map[current_point] = ("inner", INNER_AREA_COLOR)

    return area_map

def draw_map(canvas, area_map):
    for i in range(MAP_SIZE // AREA_SIZE):
        for j in range(MAP_SIZE // AREA_SIZE):
            x1 = i * (AREA_SIZE + BORDER_SIZE)
            y1 = j * (AREA_SIZE + BORDER_SIZE)
            x2 = x1 + AREA_SIZE
            y2 = y1 + AREA_SIZE

            is_border = i == 0 or j == 0 or i == (MAP_SIZE // AREA_SIZE - 1) or j == (MAP_SIZE // AREA_SIZE - 1)

            if is_border:
                color = OUTER_AREA_COLOR
            elif (i, j) in area_map:
                area_type, color = area_map[(i, j)]
            else:
                area_type, color = "outer", OUTER_AREA_COLOR

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=BORDER_COLOR)

def change_area_color(area_map, coordinates, new_color):
    if coordinates in area_map:
        area_type, _ = area_map[coordinates]
        area_map[coordinates] = (area_type, new_color)
    else:
        print("Coordinates not found in area map.")

def main():
    root = tk.Tk()
    root.title("Random Inner-Area Map")

    canvas_width = (MAP_SIZE // AREA_SIZE) * (AREA_SIZE + BORDER_SIZE) + BORDER_SIZE
    canvas_height = (MAP_SIZE // AREA_SIZE) * (AREA_SIZE + BORDER_SIZE) + BORDER_SIZE

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    area_map = generate_area_map()
    draw_map(canvas, area_map)
    root.mainloop()

if __name__ == "__main__":
    main()
