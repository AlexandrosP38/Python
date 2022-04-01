import tkinter  as tk
from tkinter import *
import MySQLdb as mdb

def showSQL():

    my_w = tk.Tk()
    my_w.geometry('600x400')
    my_w.title('Fantastic Sardines')

    db = mdb.connect(host='localhost', user='root', password='lineage38', database='python', port=3307)
    sql_select_Query = "select * from user "
    cursor = db.cursor()
    cursor.execute(sql_select_Query)

    i=0
    for row in cursor:
        for j in range(len(row)):
            e = Entry(my_w, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, row[j])
        i = i + 1

    my_w.mainloop()




