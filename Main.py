import tkinter as tk
import customtkinter

from controllers.mapController import mapController


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.configure_window()
        self.map_frame = mapController.checkMap(self)

    def configure_window(self):
        self.geometry("1200x800")
        self.title("Dark Text")


if __name__ == "__main__":
    app = App()
    app.mainloop()
