from tkinter import *
from showData import *

def fun(db):
    # declare the window
    top = tk.Tk()
    #messagebox.showinfo("Fantastic Sardines", "Button clicked")
    top.geometry('400x200+100+200')
    top.title('Fantastic Sardines')

    b1 = Button(top, text="Music", activeforeground="red", activebackground="pink", pady=30, padx=25)
    b2 = Button(top, text="Video", activeforeground="blue", activebackground="pink", pady=30, padx=25)
    b3 = Button(top, text="Notes", activeforeground="green", activebackground="pink", pady=30, padx=25)
    b4 = Button(top, text="Show Users", activeforeground="yellow", activebackground="pink", pady=30, padx=25,command=showSQL)

    b1.pack(side=LEFT)
    b2.pack(side=RIGHT)
    b3.pack(side=LEFT)
    b4.pack(side=RIGHT)

    top.mainloop()



