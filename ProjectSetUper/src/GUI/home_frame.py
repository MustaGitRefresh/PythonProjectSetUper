# This file will have the code of the GUI application of project_set_upper

# Imports
from tkinter import Tk
from tkinter import Label, Frame, Entry, Button
from tkinter import RIDGE, RIGHT, GROOVE


# Creating the Base class for the GUI app
class Home:
    def __init__(self, window):
        self.root = window

        # Calling the customizing methods
        self.set_size(height=500, width=500)

        # Components
        self.label_title()
        # Frame
        self.frame = self.inputFrame()
        self.frame.pack()
        # Entry label and entry fields
        self.label_entry(text="Enter the path", padding=[50, 50])
        user_entry_path = self.entryFields()
        self.label_entry(text='Enter the project name', padding=[50, 50])
        user_entry_project_name = self.entryFields()
        # 'create' button
        self.creator_button()
        self.root.mainloop()

    def set_size(self, height, width):
        screen_height = root.winfo_screenheight()
        screen_width = root.winfo_screenwidth()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.root.geometry(f'{height}x{width}+{x}+{y}')
        self.root.resizable(False, False)

    def label_title(self):
        font = "Helvetica 25 bold"
        label = Label(self.root, text="Project Set Upper", font=font,
                      fg='#324ea8',
                      bg='#42a832',
                      borderwidth=1,
                      width=100,
                      relief=RIDGE)
        label.pack(pady=50)

    def label_entry(self, text, padding: list, font="Helvetica 15 bold"):
        entry_label = Label(
            self.frame,
            text=text,
            font=font,
        )
        entry_label.pack(
            pady=padding[0],
            padx=padding[1]
        )

    def inputFrame(self):
        entry_frame = Frame(self.root)
        return entry_frame

    def entryFields(self, font="Helvetica 15 bold"):
        user_entry = Entry(
            self.frame,
            font=font
        )

        user_entry.pack()

        return user_entry

    def creator_button(self, font="Helvetica 15 bold"):
        creator_button = Button(
            self.root,
            text="create",
            font=font,
            fg='white',
            bg='purple',
            relief=GROOVE,
        )

        # bind with the function
        # creator_button.bind('<Button-1>', self.create_project)

        creator_button.pack(side=RIGHT)


root = Tk()
Home(root)
