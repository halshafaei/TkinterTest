import tkinter as tk

from tkinter import *


class FinanceWindow1:
    def __init__(self, master, root):
        self.root = root

        self.window = master
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

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

        frameentries = Frame(self.window)
        Label(frameentries, text='Option 1').grid(row=0, column=0)
        Label(frameentries, text='Option 2').grid(row=0, column=1)

        framebuttons = Frame(self.window)
        buttonfinancescreen1 = Button(framebuttons, text='GotoFinanceScreen1', width=25, command=self.destroy_root)
        buttonfinancescreen1.pack()

        frameentries.grid(row=0)
        framelist.grid(row=1, column=0)
        framebuttons.grid(row=1, column=1)

    def double_click(self,x):
        items = map(int, self.listbox.curselection())
        for item in items:
            # do something
            print(item)

    def destroy_root(self):
        self.root.destroy()

    def on_closing(self):
        self.root.destroy()
