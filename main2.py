import tkinter as tk
from functools import partial
import MySQLdb as mdb
from importData import *
from showData import *
from cookiesRequest import *
from newWindow import *
from registrationForm import *

def mainWindow():

    global root
    global call_connection
    global entry_user
    global entry_pass

    root = tk.Tk()  # call tkinter library to create the window
    root.geometry("500x500")
    root.title('Fantastic Sardines')

    varUser = StringVar()
    # this creates 'Label' widget for Username and uses place() method.
    label_1 = Label(root, text="Username", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    # this will accept the input string text from the user.
    entry_user = Entry(root, textvariable=varUser)
    entry_user.place(x=240, y=130)

    varPass = StringVar()
    # this creates 'Label' widget for password and uses place() method.
    label_2 = Label(root, text="Password", width=20, font=("bold", 10))
    label_2.place(x=80, y=170)
    # this will accept the input string text from the user.
    entry_pass = Entry(root, textvariable=varPass)
    entry_pass.place(x=240, y=170)


    Button(root, text='Login', width=20, bg="black", fg='white', command=call_connection).place(x=180,y=220)


def call_connection():        # Create function to connect and show result

    userN = entry_user.get()
    passN = entry_pass.get()

    try:
        db = mdb.connect(host='localhost', user='root', password='lineage38', database='python', port=3307)  #connect to database

        cursordb = db.cursor()
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        val = (userN, passN)
        cursordb.execute(sql, val)
        results = cursordb.fetchall()
        print(results)
        if results:
            for row in results:
                fun(db)
                break
        else:
            print("Not found")
            Button(root, text='Register', width=20, bg="black", fg='white', command=registerAccount).place(x=180, y=250)



    except mdb.Error as e:
        label_connection.configure(text="Not Successfully Connected \n Register an account?")
        buttonReg = tk.Button(root, text="Register", command=registerAccount).grid(row=3,column=1)


    return

mainWindow()
root.mainloop()

