from tkinter import *
from tkinter import ttk

class Railway():
    def __init__(self):
        return

    def create_railway_frame(self, root: Tk, tab_control):
        railway_frame = self.add_frame(root)
        tab_control.add(railway_frame, text='Railway')
        self.add_label(railway_frame)

    def add_frame(self, root: Tk):
        frame = Frame(root)
        return frame

    def add_label(self, frame: Frame):
        label = ttk.Label(frame, text="Example tab")
        label.grid(column=0,
                   row=0,
                   padx=30,
                   pady=30)