

class InputController:
    def __init__(self):
        pass
    
    def getInput(self, event):
        entry = event.widget
        text = entry.get()
        print(text)
        
        


inputController = InputController()