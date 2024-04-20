import tkinter as tk

from frame import MainFrame

class TkController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window()
        self.create_frame()
    
    def config_window(self):
        self.title("Garage Door Opener")
        self.minsize(width=640, height=480)
    
    def create_frame(self):
        frame = MainFrame(self)
        frame.pack()

def main():
    root = TkController()
    root.mainloop()

if __name__ == '__main__':
    main()