import tkinter as tk
from functools import partial
import MySQLdb as mdb
from importData import *
from showData import *
from cookiesRequest import *
from newWindow import *
from registrationForm import *


def call_connection(label_connection, username, passw):        # Create function to connect and show result
    user = (username.get())                                    # using get to retrieve user info
    password = (passw.get())

    try:
        db = mdb.connect(host='localhost', user=user, password=password, database='python', port=3307)  #connect to database
        label_connection.configure(text="Connected Successfully")


        root.destroy()
        fun(db)


    except mdb.Error as e:
        label_connection.configure(text="Not Successfully Connected \n Register an account?")
        buttonReg = tk.Button(root, text="Register", command=registerAccount).grid(row=3,column=1)

        #importSQL(user,password)

        root.after(7000, lambda: root.destroy())

    return


root = tk.Tk()                                                            # call tkinter library to create the window
root.geometry('400x200+100+200')
root.title('Fantastic Sardines')

userN = tk.StringVar()                                                     # the variables that user enters in box as string
passW = tk.StringVar()

labelUser = tk.Label(root, text="Username").grid(row=1, column=0)          # create the boxes for user to fill in
labelPass = tk.Label(root, text="Password").grid(row=2, column=0)

labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(root, textvariable=userN).grid(row=1, column=2)         # take the user input with Entry and pass it to variables
entryNum2 = tk.Entry(root, textvariable=passW).grid(row=2, column=2)

call_connection = partial(call_connection, labelResult, userN, passW)                        # parse the user input in function

buttonCal = tk.Button(root, text="Login", command=call_connection).grid(row=3, column=0)    # and call it when button is clicked

root.mainloop()
