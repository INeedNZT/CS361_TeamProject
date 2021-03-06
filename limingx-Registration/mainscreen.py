from tkinter import *
from tkinter import messagebox as mb
import tkinter as tk
# from tkcalendar import DateEntry
import csv
import os
import regform
import sys
def start(root):
    root.title("Registration System")
    regButton = tk.Button(root, text = "Register", width=20, height=2, command=change)
    regButton.place(x=150, y=10) 
    
    cleanButton = tk.Button(root, text = "Clean all data", width=20, height=2, command=clean).place(x=150, y=60)
 
    ssButton= tk.Button(root, text = "Search Student", padx=31, pady=10, command=searchStudent)
    ssButton.place(x=150, y=110)

    survey= Button(root, text = "Take a survey", padx=31, pady=10, command=surveyfile)
    survey.place(x=150, y=160)

    recover= Button(root, text = "Recover Data", padx=31, pady=10)
    recover.place(x=150, y=210)



def clean():
    file = 'Regfile.csv'
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
        print("file deleted")
        top = Toplevel()
        top.title("Course Registration System")
        top.geometry("60x100")    # By default, it is kept as the geometry of the main window, but you can change it.
        lab = Label(top, text="Data Cleaned!\n")
    
        lab.pack(pady=20)


    else:
        print("file not found")
        top = Toplevel()
        top.title("Course Registration System")
        top.geometry("60x100")    # By default, it is kept as the geometry of the main window, but you can change it.
        lab = Label(top, text="No file Found!\n")
    
        lab.pack(pady=20)

def searchStudent():
    print("There currently have ")
    file = open("Regfile.csv")
    reader = csv.reader(file)
    lines= len(list(reader))
    print(lines)
    print("registrations in the database. \n")
   
    with open('../limingx-CSV-web-scrap-service/Regfile.csv', "r") as csvfile:
        reader = csv.reader(csvfile)
        name = input('Enter student name: ')
        for row in reader:
            # print(row)
            if row[1] == name:
                print(row)
            else:
                print("Student Name found!")
    print("Total Credit of Courses are: 7")

def change():
    # root.destroy()
    exec(open("regform.py").read())

def surveyfile():
    exec(open("survey.py").read())

def call():
    root = Tk()
    start(root)
    root.geometry('520x540')
    root.title("Registration System")
    root.configure(background='grey')
    root.mainloop()

call()
