import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

from src.db import insert_income


class Income(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # create a frame for input of amount and date
        eframe = tk.LabelFrame(self, padx=15, pady=15)
        eframe.grid(row=0, column=0, rowspan=10, columnspan=15)
        eframe.configure({"relief": "flat", "text": ""})

        # label for amount
        textlabel = ttk.Label(eframe, text="Amount", padding="5 5 5 5")
        textlabel.grid(row=1, column=2)

        # entry label for amount
        entrylabel = ttk.Entry(eframe)
        entrylabel.grid(row=1, column=5, padx=15)

        # date using tk calender for taking date input

        datelabel = ttk.Label(eframe, text="Date", padding="5 5 5 5")
        datelabel.grid(row=2, column=2)

        cal = DateEntry(eframe, width=12, background='darkblue', date_pattern='mm/dd/y',
                        foreground='white', borderwidth=2)
        cal.grid(row=2, column=5, padx=15)

        # frame for category
        cframe = tk.LabelFrame(self, padx=20, pady=15)
        cframe.grid(row=0, column=16, rowspan=5, columnspan=10, sticky=tk.E)
        cframe.configure({"relief": "flat", "text": ""})
        clabel = ttk.Label(cframe, text="Category", padding="15 15 15 15")
        clabel.grid(row=1, column=18)

        # radio buttons to take input for category options
        category = StringVar()
        category.get()
        salary = ttk.Radiobutton(cframe, text="Salary", variable=category, value='salary', padding="3 3 3 3")
        salary.grid(row=1, column=22, sticky=tk.W)
        bonus = ttk.Radiobutton(cframe, text="Bonus", variable=category, value='bonus', padding="3 3 3 3")
        bonus.grid(row=2, column=22, sticky=tk.W)
        gift = ttk.Radiobutton(cframe, text="Gift", variable=category, value='gift', padding="3 3 3 3")
        gift.grid(row=3, column=22, sticky=tk.W)
        other = ttk.Radiobutton(cframe, text="Others", variable=category, value='other', padding="3 3 3 3")
        other.grid(row=4, column=22, sticky=tk.W)

        # frame for any description for source of income
        extraframe = tk.LabelFrame(self, padx=10, pady=15)
        extraframe.grid(row=11, column=0, rowspan=5, columnspan=15)
        extraframe.configure({"relief": "flat", "text": ""})

        note_label = ttk.Label(extraframe, text="Note")
        note_label.grid(row=12, column=2, sticky=W)
        note = ttk.Entry(extraframe)
        note.grid(row=13, column=3, padx=10, sticky=W)

        # save button for entering info in database
        button = ttk.Button(extraframe, text="Save", command=lambda: [insert_income(entrylabel, category,
                                                                                    cal, note), clear()])
        button.grid(row=15, column=10, sticky=tk.E)

        # TODO turn off category widget

        def clear():
            entrylabel.delete(0, END)
            # date_entrylabel.delete(0, END)
            note.delete(0, END)
            # category.config(state=DISABLED)