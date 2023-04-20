import tkinter as tk
import customtkinter

from controllers.mapController import MapFrame, mapController



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.configure_window()
        mapController.checkMap(self)

    def configure_window(self):
        self.geometry("1200x800")
        self.title("Map Frame Test")


if __name__ == "__main__":
    app = App()
    app.mainloop()
