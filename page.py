from tkinter import *
from tkinter import ttk
from frames import railway

class Page():
    def __init__(self):
        return

    def create_window(self):
        root = Tk()
        self.add_tab_control(root)
        root.mainloop()

    def add_tab_control(self, root: Tk):
        tab_control = ttk.Notebook(root)
        rail_gen = railway.Railway()
        rail_gen.create_railway_frame(root, tab_control)

        tab_control.pack(expand=1, fill='both')

