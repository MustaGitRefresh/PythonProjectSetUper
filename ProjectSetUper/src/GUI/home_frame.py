# This file will have the code of the GUI application of project_set_upper

# Imports
from tkinter import Tk
from tkinter import Label


# Creating the Base class for the GUI app
class Home:
    def __init__(self, window):
        self.root = window

        # Calling the customizing methods
        self.set_size(height=500, width=500)

        # Components
        self.label_app()

        self.root.mainloop()

    def set_size(self, height, width):
        self.root.geometry(f'{height}x{width}')
        self.root.maxsize(600, 600)

    def label_app(self):
        label = Label(self.root, text="ProjectSetUpper")
        label.pack()

root = Tk()
Home(root)