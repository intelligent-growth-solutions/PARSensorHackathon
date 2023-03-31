from tkinter import *
from tkinter import ttk
from frames import railway

class Page():
    def __init__(self):
        return

    def create_window(self, readings):
        root = Tk()
        self.add_tabs(root, readings)
        root.mainloop()

    def add_tabs(self, root: Tk, readings):
        tab_control = ttk.Notebook(root)

        railway_frame = railway.Railway(root, readings).get_railway_frame()
        tab_control.add(railway_frame, text='Railway')

        tab_control.pack(expand=1, fill='both')

