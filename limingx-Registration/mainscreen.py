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

    # scButton= Button(root, text = "Search Course", padx=31, pady=10)
    # dsButton= Button(root, text = "Delete Student", padx=31, pady=10) 
   
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

def clean():
    file = '../limingx-CSV-database-service/Regfile.csv'
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
        print("file deleted")
    else:
        print("file not found")


def searchStudent():
    print("There currently have ")
    file = open("../limingx-CSV-database-service/Regfile.csv")
    reader = csv.reader(file)
    lines= len(list(reader))
    print(lines)
    print("registrations in the database. \n")

    
    # number = input('Enter student name: \n')

    # #read csv, and split on "," the line
    # csv_file = csv.reader(open('../limingx-CSV-database-service/Regfile.csv', "r"), delimiter=",")

    

   
   
    with open('../limingx-CSV-database-service/Regfile.csv', "r") as csvfile:
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
    exec(open("../limingx-Registration/regform.py").read())

def call():
    root = Tk()
    start(root)
    root.geometry('520x540')
    root.title("Registration System")
    root.configure(background='grey')
    root.mainloop()

call()

