import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

from src.db import view_monthly_expense


# from datetime import datetime
# from tkcalendar import Calendar, DateEntry


class Monthly(tk.Frame):

    def month_selected(self, data):
        # month_val = self.display_month.get()
        indexval = self.display_month.current() + 1
        val = "%02d" % indexval
        print(val)

    def year_selected(self, data):
        val = self.display_year.get()
        print(val)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        eframe = tk.LabelFrame(self, padx=15, pady=15)
        eframe.grid(row=0, column=0, rowspan=5, columnspan=15)
        eframe.configure({"relief": "flat", "text": ""})

        datelabel = ttk.Label(eframe, text="Search", padding="5 5 5 5")
        datelabel.grid(row=2, column=2)

        self.display_month = ttk.Combobox(eframe, state='readonly', width=10)
        self.display_month.bind("<<ComboboxSelected>>", self.month_selected)
        self.display_month['value'] = ["January", "February",
                                       "March", "April",
                                       "May", "June",
                                       "July", "August",
                                       "September", "October",
                                       "November", "December"]
        self.display_month.grid(row=2, column=4, padx=15)
        self.display_month.current(0)

        self.display_year = ttk.Combobox(eframe, state='readonly', width=5)
        self.display_year.bind("<<ComboboxSelected>>", self.year_selected)
        self.display_year['value'] = (2020,
                                      2021,
                                      2022,
                                      2023,
                                      2024,
                                      2025)
        self.display_year.grid(row=2, column=5, padx=15)
        self.display_year.current(1)

        Button(eframe, text='View',
               command=lambda: view_monthly_expense(self.month_selected, self.year_selected, tree)).grid(row=2,
                                                                                                         column=6)

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
