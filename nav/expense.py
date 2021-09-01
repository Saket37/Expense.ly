import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

from src.db import insert_expense


class Expense(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # create a frame for input of amount and date

        eframe = tk.LabelFrame(self)
        eframe.grid(row=0, column=0, columnspan=15)
        eframe.configure({"relief": "flat", "text": ""})

        # label for expenditure

        textlabel = ttk.Label(eframe, text="Expenditure", padding="5 5 5 5")
        textlabel.grid(row=1, column=2)
        # entry label for amount
        entrylabel = ttk.Entry(eframe)
        entrylabel.grid(row=1, column=5)

        # date using tk calender for taking date input

        datelabel = ttk.Label(eframe, text="Date", padding="5 5 5 5")
        datelabel.grid(row=2, column=2)

        cal = DateEntry(eframe, width=12, background='darkblue', date_pattern='mm/dd/y',
                        foreground='white', borderwidth=2)
        cal.grid(row=2, column=5, padx=15)

        # frame for category

        cframe = tk.LabelFrame(self)
        cframe.grid(row=0, column=16, rowspan=5, columnspan=10, sticky=tk.E, padx=20, pady=15)
        cframe.configure({"relief": "flat", "text": ""})
        clabel = ttk.Label(cframe, text="Category", padding="15 15 15 15")
        clabel.grid(row=1, column=18)

        # radio buttons to take input for category options

        category = StringVar()
        category.get()
        grocery = ttk.Radiobutton(cframe, text="Grocery", variable=category, value='grocery', padding="3 3 3 3")
        grocery.grid(row=1, column=22, sticky=tk.W)

        electricity = ttk.Radiobutton(cframe, text="Electricity", variable=category, value='electricity',
                                      padding="3 3 3 3")
        electricity.grid(row=2, column=22, sticky=tk.W)

        education = ttk.Radiobutton(cframe, text="Education", variable=category, value='education', padding="3 3 3 3")
        education.grid(row=3, column=22, sticky=tk.W)

        travel = ttk.Radiobutton(cframe, text="Travel", variable=category, value='travel', padding="3 3 3 3")
        travel.grid(row=4, column=22, sticky=tk.W)

        health = ttk.Radiobutton(cframe, text="Health", variable=category, value='health', padding="3 3 3 3")
        health.grid(row=5, column=22, sticky=tk.W)

        selfDevelopment = ttk.Radiobutton(cframe, text="Self - Development", variable=category, value='selfDevelopment',
                                          padding="3 3 3 3")
        selfDevelopment.grid(row=6, column=22, sticky=tk.W)

        luxury = ttk.Radiobutton(cframe, text="Luxury", variable=category, value='luxury',
                                 padding="3 3 3 3")
        luxury.grid(row=7, column=22, sticky=tk.W)

        other = ttk.Radiobutton(cframe, text="Other", variable=category, value='other',
                                padding="3 3 3 3")
        other.grid(row=8, column=22, sticky=tk.W)

        # frame for any description for source of expense

        extraframe = tk.LabelFrame(self, padx=10, pady=15)
        extraframe.grid(row=6, column=0, rowspan=5, columnspan=15)
        extraframe.configure({"relief": "flat", "text": ""})

        note_label = ttk.Label(extraframe, text="Note")
        note_label.grid(row=7, column=2, sticky=W)
        note = ttk.Entry(extraframe)
        note.grid(row=7, column=3, padx=10, sticky=W)

        # save button for entering info in database

        button = ttk.Button(extraframe, text="Save",
                            command=lambda: [insert_expense(entrylabel, category, cal, note), clear()])
        button.grid(row=9, column=10, sticky=tk.E)

        # TODO turn off category widget
        def clear():
            entrylabel.delete(0, END)
            # date_entrylabel.delete(0, END)
            note.delete(0, END)