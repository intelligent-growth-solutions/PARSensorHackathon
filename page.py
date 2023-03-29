from tkinter import *
from tkinter import ttk
from frames import railway

class Page():
    def __init__(self):
        return

    def create_window(self):
        root = Tk()
        self.add_tabs(root)
        root.mainloop()

    def add_tabs(self, root: Tk):
        tab_control = ttk.Notebook(root)

        rail_gen = railway.Railway()
        railway_frame = rail_gen.create_railway_frame(root, tab_control)
        tab_control.add(railway_frame, text='Railway')

        tab_control.pack(expand=1, fill='both')

