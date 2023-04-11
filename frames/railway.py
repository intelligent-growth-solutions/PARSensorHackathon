import multiprocessing
from tkinter import *
from tkinter import Entry
from tkinter import messagebox
from tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

from mqttController import MqttController


class Railway:
    def __init__(self, root):
        self.root = root

        self.railway_frame = self.add_frame(self.root)

        self.add_label(self.railway_frame)

        self.add_entry_labels(self.railway_frame)
        self.widthEntry = self.width_entry_box(self.railway_frame)
        self.heightEntry = self.height_entry_box(self.railway_frame)
        self.xSteps = self.x_steps_entry_box(self.railway_frame)
        self.ySteps = self.y_steps_entry_box(self.railway_frame)

        self.take_readings_button = self.add_take_readings_button(self.railway_frame)
        self.display_readings_button = self.add_display_readings_button(self.railway_frame)

    def get_railway_frame(self):
        return self.railway_frame

    @staticmethod
    def add_frame(root):
        frame = Frame(root)
        return frame

    def add_take_readings_button(self, frame: Frame):
        button = ttk.Button(frame, text="Take readings", command=self.take_readings)
        button.grid(
            column=0,
            row=1,
            padx=30,
            pady=10
        )
        return button

    def take_readings(self):
        mqtt = MqttController()
        multiprocessing.Process(
            mqtt.initialise(self.widthEntry.get(), self.heightEntry.get(), self.xSteps.get(), self.ySteps.get()))
        messagebox.showinfo("Data loaded", "Data loaded")
        #self.readings_button.state(['!disabled'])

    def add_display_readings_button(self, frame: Frame):
        button = ttk.Button(frame, text="Display readings", command=self.add_colour_mesh_chart)
        button.grid(column=0,
                    row=2,
                    padx=30,
                    pady=10)
        return button

    def add_colour_mesh_chart(self):
        readings = self.read_data()
        print(type(readings))
        print(readings)

        plt.style.use('_mpl-gallery-nogrid')

        fig, ax = plt.subplots()
        x, y, z = zip(*readings)

        ax = np.array(z).reshape((int(self.xSteps.get()), int(self.ySteps.get())))

        plt.imshow(ax, cmap='PiYG')

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()

        canvas.get_tk_widget().pack()

    @staticmethod
    def add_frame(root):
        frame = Frame(root)
        return frame

    @staticmethod
    def add_label(frame):
        label = ttk.Label(frame, text="On Par Sensor")
        label.grid(column=0,
                   row=0,
                   padx=30,
                   pady=10)

    @staticmethod
    def width_entry_box(frame: Frame):
        widthEntry = Entry(frame, textvariable="blockWidth")
        widthEntry.grid(column=2,
                        row=0,
                        padx=30,
                        pady=10)
        return widthEntry

    @staticmethod
    def height_entry_box(frame: Frame):
        heightEntry = Entry(frame, textvariable="blockHeight")
        heightEntry.grid(column=2,
                         row=1,
                         padx=30,
                         pady=10)
        return heightEntry

    @staticmethod
    def x_steps_entry_box(frame: Frame):
        xStepsEntry = ttk.Entry(frame, textvariable="noXSteps")
        xStepsEntry.grid(column=2,
                         row=2,
                         padx=30,
                         pady=10)
        return xStepsEntry

    @staticmethod
    def y_steps_entry_box(frame: Frame):
        yStepsEntry = ttk.Entry(frame, textvariable="noYSteps")
        yStepsEntry.grid(column=2,
                         row=3,
                         padx=30,
                         pady=10)
        return yStepsEntry

    @staticmethod
    def add_entry_labels(frame: Frame):
        widthLabel = ttk.Label(frame, text="X Axis Length(500)")
        heightLabel = ttk.Label(frame, text="Y Axis Length(800)")
        xSteps = ttk.Label(frame, text="No. X steps(3)")
        ySteps = ttk.Label(frame, text="No. Y steps(3)")

        widthLabel.grid(
            column=1,
            row=0,
            padx=30,
            pady=10
        )
        heightLabel.grid(
            column=1,
            row=1,
            padx=30,
            pady=10
        )
        xSteps.grid(
            column=1,
            row=2,
            padx=30,
            pady=10
        )
        ySteps.grid(
            column=1,
            row=3,
            padx=30,
            pady=10
        )

    @staticmethod
    def read_data():
        results = []
        df = pd.read_csv('results.csv', header=None)

        for i in df.iterrows():
            print(i[1][0])

            results.append((i[1][0], i[1][1], i[1][2]))

        print(results)
        return results
