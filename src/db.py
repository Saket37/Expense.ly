import sqlite3
import tkinter as tk


def connect():
    conn = sqlite3.connect("transactiondb.sqlite")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE if NOT exists transactions(
                        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        income_amount INTEGER ,
                        expense_amount INTEGER ,
                        category TEXT NOT NULL ,
                        date NUMERIC NOT NULL ,
                        note TEXT
                        )""")
    conn.commit()
    conn.close()


def insert_income(entrylabel, category, date_entrylabel, note):
    conn = sqlite3.connect("transactiondb.sqlite")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO transactions(income_amount,category,date,note) "
        "VALUES (:entrylabel, :category,:date_entrylabel,:note)",
        {
            'entrylabel': entrylabel.get(),
            'category': category.get(),
            'date_entrylabel': date_entrylabel.get(),
            'note': note.get()
        })
    conn.commit()
    conn.close()


def insert_expense(entrylabel, category, date_entrylabel, note):
    conn = sqlite3.connect("transactiondb.sqlite")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO transactions(expense_amount, category, date, note) "
        "VALUES (:entrylabel,:category,:date_entrylabel,:note)",
        {
            'entrylabel': entrylabel.get(),
            'category': category.get(),
            'date_entrylabel': date_entrylabel.get(),
            'note': note.get()
        })
    conn.commit()
    conn.close()


def view_daily_income(cal, tree):
    conn = sqlite3.connect("transactiondb.sqlite")
    cur = conn.cursor()

    cur.execute("SELECT  category,income_amount, note FROM transactions WHERE date = ? AND  income_amount != 'None' "
                , [cal.get()])
    rec = cur.fetchall()
    # print(rec)
    for row in rec:
        print(row)
        tree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()


def view_daily_expense(cal, tree):
    conn = sqlite3.connect("transactiondb.sqlite")
    cur = conn.cursor()

    cur.execute("SELECT  category,expense_amount, note FROM transactions WHERE date = ? AND  expense_amount != 'None' "
                , [cal.get()])
    rec = cur.fetchall()
    # print(rec)
    for row in rec:
        print(row)
        tree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()


def view_monthly_expense(month_selected, year_selected, tree):
    conn = sqlite3.connect("transactiondb.sqlite")
    cur = conn.cursor()
    cur.execute(
        "SELECT  category,expense_amount, note FROM transactions WHERE CAST((strftime('%m', date)) AS INTEGER) =?  "
        "AND CAST((strftime('%Y', date)) AS INTEGER) =? AND expense_amount != 'None' "
        , (str(month_selected), str(year_selected),))
    rec = cur.fetchall()
    # print(rec)
    for row in rec:
        print(row)
        tree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()


"""def view_monthly(getmonth, getyear, tree):
    conn = sqlite3.connect("transactiondb.sqlite")
    cur = conn.cursor()
    cur.execute(
        "SELECT  category,income_amount, note FROM transactions WHERE CAST((strftime('%m', date)) AS INTEGER) =?  AND CAST((strftime('%Y', date)) AS INTEGER) =? AND income_amount != 'None',"
        [getmonth],[getyear])
    rec = cur.fetchall()
    # print(rec)
    for row in rec:
        print(row)
        tree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()


def view_month(display_year, tree):
    conn = sqlite3.connect("transactiondb.sqlite")
    cur = conn.cursor()
    cur.execute(
        " SELECT category,income_amount, note FROM transactions WHERE CAST ((strftime('%Y', date))AS INTEGER ) =? AND income_amount != 'None',"
        [display_year])
    rec = cur.fetchall()
    # print(rec)
    for row in rec:
        print(row)
        tree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()"""

connect()
