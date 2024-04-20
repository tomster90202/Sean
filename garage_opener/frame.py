import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master: tk.Misc):
        super().__init__(master)
        self.populate_frame()
    
    def populate_frame(self):
        label = tk.Label(self, text="Welcome to the Garage Door Opener!")
        label.pack()

        button = tk.Button(self, text="Open the Garage", command=self.open_garage)
        button.pack()
    
    def open_garage(self):
        print("OPENING THE GARAGE!!!")