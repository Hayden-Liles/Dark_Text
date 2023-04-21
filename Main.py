import tkinter as tk
import customtkinter

from controllers.MapController import mapController
from controllers.PlayerController import playerController

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.configure_window()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
        self.map_frame = mapController.checkMap(self)
        
        # SECTION TESTING LAYOUT
        self.button = customtkinter.CTkButton(self, text="test")
        self.button.grid(row=0, column=0, pady=(20, 0), padx=(20, 0), sticky='nw')

        # NOTE the binding for keypress event listener
        self.bind('<KeyRelease>', self.keyPress)

    def configure_window(self):
        self.geometry("1000x900")
        self.title("Dark Text")

    # SECTION KeyPress event Listener
    def keyPress(self, event):
        key = event.keysym
        if key in ('Up', 'Down', 'Left', 'Right'):
            playerController.movePlayer(key)

if __name__ == "__main__":
    app = App()
    app.mainloop()
