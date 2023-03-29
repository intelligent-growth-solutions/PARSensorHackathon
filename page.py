from tkinter import *
from tkinter import ttk

class Page():
    def __init__(self):
        return

    def create_window(self):
        root = Tk()
        self.add_tab_control(root)
        root.mainloop()

    def add_tab_control(self, root: Tk):
        tab_control = ttk.Notebook(root)

        sensor_frame = self.add_frame(root)
        tab_control.add(sensor_frame, text='Sensor')
        self.add_label(sensor_frame)

        railway_frame = self.add_frame(root)
        tab_control.add(railway_frame, text='Railway')
        self.add_label(railway_frame)

        tab_control.pack(expand=1, fill='both')

    def add_frame(self, root: Tk):
        frame = Frame(root)
        return frame

    def add_label(self, frame: Frame):
        label = ttk.Label(frame, text="Example tab")
        label.grid(column=0,
                   row=0,
                   padx=30,
                   pady=30)

