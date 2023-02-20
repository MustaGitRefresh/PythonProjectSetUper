from tkinter import Tk

root = Tk()
height = 500
width = 500
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)


root.geometry(f'{width}x{height}+{x}+{y}')
root.mainloop()
