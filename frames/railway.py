from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import time

class Railway:
    def __init__(self, root):
        self.root = root
        self.railway_frame = self.add_frame(self.root)
        self.add_label(self.railway_frame)
        self.readings_button = self.add_take_readings_button(self.railway_frame)

    def get_railway_frame(self):
        return self.railway_frame

    @staticmethod
    def add_frame(root: Tk):
        frame = Frame(root)
        return frame

    @staticmethod
    def add_label(frame: Frame):
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
        return button

    def take_readings(self):
        self.readings_button.state(['disabled'])

        # TODO replace with instruction call
        messagebox.showinfo("Button pressed", "Button pressed")
        
        self.readings_button.state(['!disabled'])

