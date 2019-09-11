import tkinter as tk

from tkinter import *


class Finance_Window:
    def __init__(self, master,  root):
        self.root = root
        self.window = master
        self.frame = Frame(self.window)
        self.varObj = Variable()

        w = 900  # width for the Tk window
        h = 700  # height for the Tk window

        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk window window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.resizable(height=FALSE, width=FALSE)
        self.window.title("Finance")

        frameEntries = Frame(self.window)
        Label(frameEntries, text='Username').grid(row=0)
        Label(frameEntries, text='Password').grid(row=1)
        e1 = Entry(frameEntries).grid(row=0, column=1)
        e2 = Entry(frameEntries).grid(row=1, column=1)

        frameButton = Frame(self.window)
        button = Button(frameButton, text='Close', width=25, command=self.destroy_root)
        button.grid(row=4)

        frameEntries.grid(row=0)
        frameButton.grid(row=1)

    def destroy_root(self):
        self.root.destroy()
