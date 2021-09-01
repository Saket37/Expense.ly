import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkcalendar import DateEntry
from src.db import view_daily_income
from src.db import view_daily_expense


class Daily(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        eframe = tk.LabelFrame(self, padx=15, pady=15)
        eframe.grid(row=0, column=0, rowspan=5, columnspan=15)
        eframe.configure({"relief": "flat", "text": ""})

        datelabel = ttk.Label(eframe, text="Date", padding="5 5 5 5")
        datelabel.grid(row=2, column=2, rowspan=2)

        cal = DateEntry(eframe, width=12, background='darkblue', date_pattern='mm/dd/y',
                        foreground='white', borderwidth=2)
        cal.grid(row=2, column=5, rowspan=2, padx=15)

        Button(eframe, text="Income", command=lambda: view_daily_income(cal, tree)).grid(row=2, column=6)
        Button(eframe, text="Expense", command=lambda: view_daily_expense(cal, tree)).grid(row=3, column=6, pady=5)

        treeframe = tk.LabelFrame(self, padx=15, pady=15)
        treeframe.grid(row=5, column=0, columnspan=20)
        treeframe.configure({"relief": "flat", "text": ""})

        tree = ttk.Treeview(treeframe, selectmode="extended", column=("c1", "c2", "c3"))
        tree.column("#1", minwidth=200, width=150, stretch=False)

        tree.heading("#1", text="Category")

        tree.column("#2", minwidth=200, width=150, stretch=False)

        tree.heading("#2", text="Amount")

        tree.column("#3", minwidth=250, width=200)

        tree.heading("#3", text="Note")
        tree['show'] = 'headings'

        tree.grid(row=0, column=0, columnspan=10)
