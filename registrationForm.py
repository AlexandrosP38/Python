from tkinter import *
import MySQLdb as mdb


def registerAccount():

    global entry_user
    global entry_pass
    global entry_email

    root = Tk()
    root.geometry("500x500")
    root.title('Registration form')

    label_0 =Label(root,text="Registration form", width=20,font=("bold",20))
    label_0.place(x=90,y=60)

    varUser = StringVar()
    #this creates 'Label' widget for Username and uses place() method.
    label_1 =Label(root,text="Username",  width=20,font=("bold",10))
    label_1.place(x=80,y=130)
     #this will accept the input string text from the user.
    entry_user=Entry(root,textvariable=varUser)
    entry_user.place(x=240,y=130)

    varPass = StringVar()
    # this creates 'Label' widget for password and uses place() method.
    label_2 = Label(root, text="Password", width=20, font=("bold", 10))
    label_2.place(x=80, y=170)
    # this will accept the input string text from the user.
    entry_pass = Entry(root,textvariable=varPass)
    entry_pass.place(x=240, y=170)

    varEmail = StringVar()
    #this creates 'Label' widget for Email and uses place() method.
    label_3 =Label(root,text="Email", width=20,font=("bold",10))
    label_3.place(x=68,y=200)
    entry_email=Entry(root, textvariable=varEmail)
    entry_email.place(x=240,y=200)

    #this creates 'Label' widget for Gender and uses place() method.
    label_4 =Label(root,text="Gender", width=20,font=("bold",10))
    label_4.place(x=70,y=230)


    #the variable 'var' mentioned here holds Integer Value, by deault 0
    var=IntVar()

    #this creates 'Radio button' widget and uses place() method
    Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=235,y=230)
    Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=290,y=230)


    ##this creates 'Label' widget for country and uses place() method.
    label_5=Label(root,text="Country",width=20,font=("bold",10))
    label_5.place(x=70,y=280)
    #this creates list of countries available in the dropdownlist.
    list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']

    #the variable 'c' mentioned here holds String Value, by default ""
    c=StringVar()
    droplist=OptionMenu(root,c, *list_of_country)
    droplist.config(width=15)
    c.set('Select your Country')
    droplist.place(x=240,y=280)

    ##this creates 'Label' widget for Language and uses place() method.
    label_6=Label(root,text="Language",width=20,font=('bold',10))
    label_6.place(x=75,y=330)
    #the variable 'var1' mentioned here holds Integer Value, by default 0
    var1=IntVar()
    #this creates Checkbutton widget and uses place() method.
    Checkbutton(root,text="English", variable=var1).place(x=230,y=330)


    #the variable 'var2' mentioned here holds Integer Value, by default 0
    var2=IntVar()
    Checkbutton(root,text="German", variable=var2).place(x=290,y=330)

    #this creates button for submitting the details provides by the user
    Button(root, text='Submit' , width=20,bg="black",fg='white', command = insertData).place(x=180,y=380)

    root.mainloop()


def insertData():

    userN = entry_user.get()
    passN = entry_pass.get()
    emailN = entry_email.get()

    db = mdb.connect(host='localhost', user='root', password='lineage38', database='python',
                     port=3307)  # connect to database

    cursorInsert = db.cursor()

    sql_insert_Query = "INSERT INTO users (username,password,email) VALUES (%s,%s,%s)"
    val = (userN, passN,emailN)
    try:
        # executing the sql command
        cursorInsert.execute(sql_insert_Query, val)
        # commit changes in database
        db.commit()
    except:
        db.rollback()

