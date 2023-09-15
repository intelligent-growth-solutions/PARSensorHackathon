import multiprocessing
import threading
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
        threading.Thread(target=mqtt.initialise, args=(self.widthEntry.get(), self.heightEntry.get(), self.xSteps.get(), self.ySteps.get())).start()
        messagebox.showinfo("Taking Readings...", "Measuring a {} by {} grid".format(self.xSteps.get(),self.ySteps.get(),))

    def add_display_readings_button(self, frame: Frame):
        button = ttk.Button(frame, text="Display readings", command=self.add_colour_mesh_chart)
        button.grid(column=0,
                    row=2,
                    padx=30,
                    pady=10)
        return button

    def add_colour_mesh_chart(self):
        readings = self.read_data()

        plt.style.use('_mpl-gallery-nogrid')

        fig, ax = plt.subplots(figsize=(4, 4))
        y, x, z = zip(*readings)

        data = np.array(z).reshape((int(self.xSteps.get()), int(self.ySteps.get())))
        im = ax.imshow(data, vmin=min(z), vmax=max(z), cmap='PiYG')

        fig.subplots_adjust(right=0.8)
        cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
        fig.colorbar(im, cax=cbar_ax)

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill='both', expand=True)

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
        widthEntry.insert(END, 842)
        widthEntry.grid(column=2,
                        row=0,
                        padx=30,
                        pady=10)
        return widthEntry

    @staticmethod
    def height_entry_box(frame: Frame):
        heightEntry = Entry(frame, textvariable="blockHeight")
        heightEntry.insert(END, 520)
        heightEntry.grid(column=2,
                         row=1,
                         padx=30,
                         pady=10)
        return heightEntry

    @staticmethod
    def x_steps_entry_box(frame: Frame):
        xStepsEntry = ttk.Entry(frame, textvariable="noXSteps")
        xStepsEntry.insert(END, 10)
        xStepsEntry.grid(column=2,
                         row=2,
                         padx=30,
                         pady=10)
        return xStepsEntry

    @staticmethod
    def y_steps_entry_box(frame: Frame):
        yStepsEntry = ttk.Entry(frame, textvariable="noYSteps")
        yStepsEntry.insert(END, 10)
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
