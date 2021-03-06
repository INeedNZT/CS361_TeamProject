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
root.geometry('540x600')
root.title("Registration Form")
root.configure(background='white')

img = ImageTk.PhotoImage(Image.open('boy.png'))
panel = Label(root,image=img)
panel.place(x=220,y=23)
panel.config(image = img)

def help_window():
    top = Toplevel()
    top.title("Featured New Extensions")
    top.geometry("400x100")    # By default, it is kept as the geometry of the main window, but you can change it.
    lab = Label(top, text="This is a Course Registration System for student \n which you can Add Delete Search Student and courses!\n Let's filled in your information and got the registration done!\n")
    
    lab.pack(pady=20)

b = Button(root, text="I Need Help", command=help_window)
b.pack(pady=50)
b.place(x=320,y=43)

# creating labels and entry widgets

#defining function msg() using messagebox
def msg():
    course = cvar.get()
    select = var.get()
    if(select == 1 or select == 2):
        # get the index of the last character in the widget,if it is zero,it is empty
        if (e1.index("end") == 0):
            mb.showwarning('Missing details', 'enter your name')
        elif(e2.index("end") == 0):
            mb.showwarning('Missing details', 'enter your email id')
        elif(e3.index("end") == 0):
            mb.showwarning('Missing details', 'enter your contact number')
        else:
            mb.showinfo('Success', 'Registration done successfully for the course '+ course)
    else:
            mb.showinfo('Missing details', 'enter your gender')

#exporting entered data
def save():
    g = var.get()
    course = cvar.get()
    credit = cvar.get()
    # db = dob.get_date()
    # d = db.strftime('%d/%m/%Y')
    now = datetime.datetime.now()
    if(g==1):
        gender ='male'
    else:
        gender ='female'

    #save data in txt file

    # s='\n'+now.strftime("%d-%m-%Y %H:%M")+'\t'+e1.get()+'\t'+e2.get()+'\t '+e3.get()+'\t'+ d+'\t'+gender+' \t'+course
    s='\n'+now.strftime("%d-%m-%Y %H:%M")+'\t'+e1.get()+'\t'+e2.get()+'\t '+e3.get()+'\t'+'\t'+gender+' \t'+course +' \t'+credit
    f = open(('regdetails.txt'), 'a')
    f.write(s)
    f.close()

    #save data in csv file
    with open('../limingx-CSV-web-scrap-service/Regfile.csv', 'a') as fs:
        w = csv.writer(fs, dialect='excel-tab')
        # w.writerow([now.strftime("%d-%m-%Y %H:%M"), e1.get(),e2.get(),e3.get(),d,gender,course])
        w.writerow([now.strftime("%d-%m-%Y %H:%M"), (","),e1.get(), (","),e2.get(), (","),e3.get(), (","),gender, (","),course, (","), credit ])
        fs.close()




def saveinfo():
    save()
    msg()

l1 = Label(root, text="Course Registration form",width=25,font=("times",20,"bold"),bg='blue',fg='white')
l1.place(x=70,y=130)
l2 = Label(root, text="Full Name",width=20,font=("times",12,"bold"),anchor="w",bg='white')
l2.place(x=70,y=180)
e1 = Entry(root,width=30,bd=2)
e1.place(x=240,y=180)
l3 = Label(root, text="Email",width=20,font=("times",12,"bold"),anchor="w",bg='white')
l3.place(x=70,y=230)
e2 = Entry(root,width=30,bd=2)
e2.place(x=240,y=230)
# l4 = Label(root, text="DOB",width=20,font=("times",12,"bold"),anchor="w",bg='white')
# l4.place(x=70,y=230)

# dateEntry -Date selection entry with drop-down calendar
# dob = DateEntry(root, width=27, background='brown', foreground='white',date_pattern='dd/mm/Y', borderwidth=3)
# dob.place(x=240,y=230)

l5 = Label(root, text="Gender", width=20, font=("times",12,"bold"),anchor="w",bg='white')
l5.place(x=70,y=320)

# radiobuttons
var = IntVar()
r1 = Radiobutton(root, text="Male", variable=var, value=1, font=("times",12),bg='white')
r1.place(x=235,y=320)
r2 = Radiobutton(root, text="Female", variable=var, value=2, font=("times",12),bg='white')
r2.place(x=315,y=320)

l6 = Label(root, text="Contact no.",width=20,font=("times",12,"bold"),anchor="w",bg='white')
l6.place(x=70,y=270)
e3 = Entry(root,width=30,bd=2)
e3.place(x=240,y=270)




l7 = Label(root, text="Select course",width=20,font=("times",12,"bold"),anchor="w",bg='white')
l7.place(x=70,y=420)



# create a dropdown menu with the OptionMenu widget
cvar = StringVar()
cvar.set("Select course")
option = ("Python", "Javascript", "Perl","Java")
o = OptionMenu(root,cvar, *option)
o.config(font=("times",11),bd=3)
o.place(x=240,y=420,width=190)







l8 = Label(root, text="Credit Registered",width=20,font=("times",12,"bold"),anchor="w",bg='white')
l8.place(x=70,y=370)






# create a dropdown menu with the OptionMenu widget
cvar = StringVar()
cvar.set("Credit Registered")
option = ("3", "4", "5")
o = OptionMenu(root,cvar, *option)
o.config(font=("times",11),bd=3)
o.place(x=240,y=370,width=190)
# submit and cancel buttons

asd = Button(root, text='Submit',command=saveinfo,width=15,bg='green',fg='white',font=("times",12,"bold"))
asd.place(x=120,y=500)
asdf = Button(root, text='Cancel',command=root.destroy,width=15,bg='maroon',fg='white',font=("times",12,"bold"))
asdf.place(x=320,y=500)
    
root.mainloop()


