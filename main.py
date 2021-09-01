import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import font

from nav.income import Income
from nav.expense import Expense
from nav.daily import Daily
from nav.monthly import Monthly


# create a class Menubar for navigation
class MenuBar(tk.Menu):
    def __init__(self, parent, controller):
        tk.Menu.__init__(self, parent)
        self.controller = controller
        transaction = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Transaction", menu=transaction)
        transaction.add_command(label="Income", command=lambda: controller.show_frame("Income"))
        transaction.add_command(label="Expense", command=lambda: controller.show_frame("Expense"))

        record = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Record", menu=record)
        record.add_command(label="Daily", command=lambda: controller.show_frame("Daily"))
        # TODO add a weekly tab
        # record.add_command(label="Weekly", command=record)
        record.add_command(label="Monthly", command=lambda: controller.show_frame("Monthly"))

        stats = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Stats", menu=stats)


class Expensely(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Expense.ly")
        tk.Tk.wm_geometry(self, "600x400")
        tk.Tk.wm_resizable(self, height=0, width=0)

        # TODO add logo for the app
        # define container
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="NSEW")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # setup menubar for navigation
        menubar = MenuBar(self, controller=self)
        self.config(menu=menubar)

        # to switch between different frames
        self.frames = {}
        for F in (StartPage, Income, Expense, Daily, Monthly):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        # page_name="StartPage"

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.lift()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        highlightFont = font.Font(family='Helvetica', size=20, weight='bold')
        label = tk.Label(self, text="Welcome to Expense.ly\nAn amazing way to track your expenses", font=highlightFont)
        label.grid(row=0, column=0, sticky="nesw")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    app = Expensely()
    app.mainloop()
