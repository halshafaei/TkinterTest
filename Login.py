import tkinter as tk
from Main_Screen import *

from tkinter import *


class LoginWindow:
    def __init__(self, master):
        self.window = master
        self.frame = Frame(self.window)
        self.varObj = Variable()

        w = 300  # width for the Tk window
        h = 200  # height for the Tk window

        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk window window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.resizable(height=FALSE, width=FALSE)
        self.window.title("Login")

        frameEntries = Frame(self.window)
        Label(frameEntries, text='Password').grid(row=1)
        e2 = Entry(frameEntries, show="*")
        e2.grid(row=1, column=1)
        self.Username = "root"
        self.Password = e2

        frameButton = Frame(self.window)
        button = Button(frameButton, text='Go!', width=25, command=self.login_check)
        button.grid(row=1)

        self.window.grid_rowconfigure(0, weight=2)
        self.window.grid_rowconfigure(1, weight=2)
        self.window.grid_columnconfigure(0, weight=3)
        self.window.grid_columnconfigure(1, weight=3)
        frameEntries.grid(row=0)
        frameButton.grid(row=1)

    def switch_window(self):
        self.newWindow = tk.Toplevel(self.window)
        MainWindow(self.newWindow, self.window)
        self.window.withdraw()

    # check passwords
    def login_check(self):
        print(self.Username )
        print(self.Password.get())
        if self.Password.get() == "root":
            self.switch_window()


def main():
    login_window = Tk()
    LoginWindow(login_window)
    login_window.mainloop()


if __name__ == '__main__':
    main()
