from array import array
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
import time

class Railway:
    def __init__(self, root, readings):
        self.root = root
        self.readings = readings
        self.railway_frame = self.add_frame(self.root)
        self.add_label(self.railway_frame)
        self.readings_button = self.add_take_readings_button(self.railway_frame)

    def get_railway_frame(self):
        return self.railway_frame

    @staticmethod
    def add_frame(root):
        frame = Frame(root)
        return frame

    @staticmethod
    def add_label(frame):
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
        #self.readings_button.state(['disabled'])

        # TODO replace with instruction call
        #feed_in_data = self.get_data()
        # simulate waiting for data
        #print(feed_in_data)
        print(str(self.readings))
        data = self.readings
        self.add_colour_mesh_chart(data)
        messagebox.showinfo("Data loaded", "Data loaded")

        self.readings_button.state(['!disabled'])

    def add_colour_mesh_chart(self, readings):
        coords = [
            [50, 80, 0.0019027228467166425],
            [50, 240, 0.0019050051923841238],
            [150, 80, 0.0017148582730442286],
            [150, 240, 0.0017062114784494042]
        ]
        print(type(coords))
        print(type(readings))

        print(coords)
        print(readings)

        plt.style.use('_mpl-gallery-nogrid')
        coord_data: (int, int, float) = self.generate_pcolourmesh_grid(readings)

        fig, ax = plt.subplots()
        x, y, z = zip(*readings)
        ax = np.array(z).reshape((3,3))

        plt.imshow(ax, cmap='Blues')

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()

        canvas.get_tk_widget().pack()

    def generate_pcolourmesh_grid(self, data: list[list[float]]):
        tray_width = 500
        tray_height = 800

        i = 0
        # coords: array[int, int, float] = []
        #
        # for x in range(2):
        #     for y in range(2):
        #         coords.append((
        #             int(((tray_width * x/5) + (tray_width * 1/2))),
        #             int(((tray_height * y/5) + (tray_height * 1/2))),
        #             (data[i])
        #         ))
        #         print("X: {}, Y: {}".format(x, y))
        #         i += 1

        coords = [
            [50, 80, 0.0019027228467166425],
            [50, 240, 0.0019050051923841238],
            [150, 80, 0.0017148582730442286],
            [150, 240, 0.0017062114784494042]
        ]

        return coords

    #def get_data(self, ):
        # return [
        #     [0, 1, 2, 3, 4],
        #     [0, 1, 2, 3, 4],
        #     [0, 1, 2, 3, 4],
        #     [0, 1, 2, 3, 4],
        #     [0, 1, 2, 3, 4]
        #  ]
        # return [
        #     [0, 1],
        #     [0, 1]
        # ]
        #return read
