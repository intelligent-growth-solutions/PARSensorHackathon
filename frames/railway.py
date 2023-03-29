from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Railway():
    def __init__(self):
        return

    def create_railway_frame(self, root: Tk, tab_control):
        railway_frame = self.add_frame(root)
        self.add_label(railway_frame)
        self.add_take_readings_button(railway_frame)
        return railway_frame

    def add_frame(self, root: Tk):
        frame = Frame(root)
        return frame

    def add_label(self, frame: Frame):
        label = ttk.Label(frame, text="Example tab")
        label.grid(column=0,
                   row=0,
                   padx=30,
                   pady=10)

    def add_take_readings_button(self, frame: Frame):
        button = ttk.Button(frame, text="Take readings", command=self.take_readings)
        button.grid(column=0,
                   row=1,
                   padx=30,
                   pady=10)

    def take_readings(self):
        # TODO replace with instruction call
        messagebox.showinfo("Button pressed", "Button pressed")
