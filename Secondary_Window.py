import tkinter as tk

from tkinter import *


class Finance_Window:
    def __init__(self, master, root):
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

        framelist = Frame(self.window)
        listbox = Listbox(framelist, selectmode=EXTENDED)
        listbox.pack()
        self.listbox = listbox
        listbox.bind("<Double-Button-1>", self.double_click)
        listbox.insert(END, "a list entry")
        listbox.insert(END, "a second list entry")


        frameEntries = Frame(self.window)
        Label(frameEntries, text='Option 1').grid(row=0, column=0)
        Label(frameEntries, text='Option 2').grid(row=0, column=1)

        frameButton = Frame(self.window)
        button = Button(frameButton, text='Close', width=25, command=self.destroy_root)
        button.pack()


        frameEntries.grid(row=0)
        framelist .grid(row=1,column = 0)
        frameButton.grid(row=1, column = 1)

    def double_click(self,x):
        print(x)
        items = map(int, self.listbox.curselection())
        for item in items:
            # do something
            print(item)
    def destroy_root(self):
        self.root.destroy()
