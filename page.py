from tkinter import *

class Page():
    def __init__(self):
        return

    def create_window(self):
        top = Tk()
        self.add_textbox(top)
        top.mainloop()

    def add_textbox(self, top):
        text = Text(top)
        text.insert(INSERT, "hello")
        text.pack()

