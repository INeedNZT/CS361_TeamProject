from tkinter import *
from tkinter import messagebox as mb
# from tkcalendar import DateEntry
import csv
from regform import *

def start(root):
    root.title("Registration System")
    regButton= Button(root, text = "Register", padx=31, pady=10, command=lambda: change(root)).grid()
    # regButton.pack()
    
    # regButton = Button(root, text = "Search Student", padx=31, pady=10)
    # regButton.pack()

    # regButton = Button(root, text = "Search Course", padx=33, pady=10)
    # regButton.pack()

    # regButton = Button(root, text = "Delete Student", padx=33, pady=10)
    # regButton.pack()

    # regButton = Button(root, text = "Delete Course", padx=35, pady=10)
    # regButton.pack()

#myLabel1 = Label(root, text= "There are ")
#myLabel2 = Label(root, text= "and ")
#myLabel3 = Label(root, text= "courses in the database.")

def change(root):
    # root.destroy()
    fun()

def call():
    root = Tk()
    start(root)
    root.geometry('520x540')
    root.title("Registration System")
    root.configure(background='grey')
    root.mainloop()

call()


