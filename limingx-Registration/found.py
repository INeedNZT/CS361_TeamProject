from tkinter import *
from tkinter import messagebox as mb
# from tkcalendar import DateEntry
import datetime
import csv
from PIL import ImageTk,Image
import sqlite3
conn = sqlite3.connect("registration.db")
cursor = conn.cursor()

root = Tk()
root.geometry('450x200')
root.title("Course Registration System")
root.configure(background='white')

l5 = Label(root, text="3 results found! ", width=20, font=("times",12,"bold"),anchor="w",bg='white')
l5.place(x=10,y=0)

# radiobuttons
var = IntVar()
r1 = Radiobutton(root, text="Calculate Total credit", variable=var, value=1, font=("times",12),bg='white')
r1.place(x=35,y=45)



asd = Button(root, text='Submit',width=15,bg='green',fg='white',font=("times",12,"bold"))
asd.place(x=10,y=120)

asdf = Button(root, text='Cancel',command=root.destroy,width=15,bg='maroon',fg='white',font=("times",12,"bold"))
asdf.place(x=200,y=120)
    
root.mainloop()


