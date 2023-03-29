from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import numpy as np

class Railway():

    def __init__(self):
        return

    def create_railway_frame(self, root: Tk, tab_control):
        railway_frame = self.add_frame(root)
        self.add_label(railway_frame)
        self.add_colour_mesh_chart(railway_frame)
        return railway_frame

    def add_frame(self, root: Tk):
        frame = Frame(root)
        return frame

    def add_label(self, frame: Frame):
        label = ttk.Label(frame, text="Example tab")
        label.grid(column=0,
                   row=0,
                   padx=30,
                   pady=30)

    def add_colour_mesh_chart(self, frame: Frame):
        plt.style.use('_mpl-gallery-nogrid')

        data = self.get_data()
        x_coords, y_coords, z_coords = self.generate_pcolourmesh_grid(data)


        # make data with uneven sampling in x
        X, Y = np.meshgrid(x_coords, y_coords)
        Z = z_coords
        # Z = (1 - X / 2 + X ** 5 + Y ** 3) * np.exp(-X ** 2 - Y ** 2)

        # plot
        fig, ax = plt.subplots()

        ax.pcolormesh(X, Y, Z)

        canvas = FigureCanvasTkAgg(fig, master=frame.master)
        canvas.draw()

        canvas.get_tk_widget().pack()

    def generate_pcolourmesh_grid(self, data: list[list[float]]):
        tray_width = 500
        tray_height = 800

        x_coords = []
        y_coords = []
        z_coords = []

        for x in range(5):
            for y in range(5):
                x_coords.append((tray_width * x/5) + (tray_width * 1/2))
                y_coords.append((tray_height * y/5) + (tray_height * 1/2))
                z_coords.append(data[x][y])

        return x_coords, y_coords, z_coords

    def get_data(self):
        return [
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5]
         ]




