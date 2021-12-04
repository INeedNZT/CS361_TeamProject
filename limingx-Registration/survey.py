from tkinter import *
import tkinter.messagebox as messagebox

class TkDemo():
    def __init__(self):
        master = Tk()
        master.title('Course Registration Survey')
        # 创建菜单栏 (Menu)
        menubar = Menu(master)
        master.config(menu=menubar)
        # 创建文件下拉菜单
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New···", command=self.newfile)
       
        filemenu.add_command(label="Save", command=self.savefile)
        filemenu.add_command(label="Close", command=master.quit)
        editmenu.add_command(label="Advanced Options", command=self.nomal)
        # 创建编辑下拉菜单
        editmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Red", command=self.red)
        editmenu.add_command(label="Blue", command=self.blue)
        editmenu.add_command(label="Yellow", command=self.yellow)
        editmenu.add_command(label="Default", command=self.nomal)
        # 创建帮助下拉菜单
        helpmenu = Menu(menubar,tearoff=0)
        menubar.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='Instruction', command=self.description)
        helpmenu.add_command(label='About', command=self.about)

        textmenu = Menu(menubar,tearoff=0)
        menubar.add_cascade(label='<--Please read before you start the survey', menu=helpmenu)

        # 文字 (Label)
        title = Label(master, text='Course Registration Survey', font='15', bg='white', fg='red')
        title.pack()

        # 问题1放在frame1中 (Frame)
        frame1 = Frame(master)
        frame1.pack(fill=X)
        # 问题
        label1 = Label(frame1, text='1、Enter Your Name：   ')
        label1.grid(row=1, column=0)
        # 输入框 (Entry)
        self.name = StringVar()
        entryname = Entry(frame1, textvariable=self.name)
        entryname.grid(row=1, column=1)
        # 按钮  (Button)
        getname = Button(frame1, text='Confirm', command=self.getname)
        getname.grid(row=1, column=3)

        # 问题2放在frame2中
        frame2 = Frame(master)
        frame2.pack(fill=X)
        # 问题
        label2 = Label(frame2, text='2、Your Gender：   ')
        label2.grid(row=1, column=0)
        # 选择按钮 (Radiobutton)
        self.sex = StringVar()
        sex_male = Radiobutton(frame2, text='Male', fg='blue', variable=self.sex, value='男', command=self.getsex)
        sex_male.grid(row=1, column=2)
        sex_female = Radiobutton(frame2, text='Female', fg='red', variable=self.sex, value='女', command=self.getsex)
        sex_female.grid(row=1, column=4)

        # 问题3放在frame3中
        frame3 = Frame(master)
        frame3.pack(fill=X)
        # 问题
        label2 = Label(frame3, text='3、Enter Your Age：   ')
        label2.grid(row=1, column=0)
        # 滑动条 (Scale)
        self.age = Scale(frame3, from_=0, to=100, orient=HORIZONTAL, resolution=1)   # 默认垂直
        self.age.grid(row=1, column=1)
        # 按钮  (Button)
        getage = Button(frame3, text='Confirm', command=self.getage)
        getage.grid(row=1, column=2)

        # 问题4放在frame4中
        frame4 = Frame(master)
        frame4.pack(fill=X)
        # 问题
        label4 = Label(frame4, text='4、Please Delete the Programming Course You dont like：   ')
        label4.grid(row=1, column=0)
        # 列表  (Listbox)
        self.listbox = Listbox(frame4)
        self.listbox.grid(row=1, column=1)
        for item in ["C", "C++", 'JAVA', 'Python', 'R', 'SQL', 'JS']:
            self.listbox.insert(END, item)
        # 删除按钮
        DELE = Button(frame4, text="Delete", command=lambda listbox=self.listbox: listbox.delete(ANCHOR))
        DELE.grid(row=1, column=2)
        # 确定按钮
        language = Button(frame4, text="Confirm", command=self.getlanguage)
        language.grid(row=2, column=1)

        # 问题5放在frame5中
        frame5 = Frame(master)
        frame5.pack(fill=X)
        # 问题
        label5 = Label(frame5, text='5、What is your favorite shape：   ')
        label5.grid(row=1, column=0)
        # 画板  (Canvas)
        self.canvas = Canvas(frame5, width=200, height=100, bg="White")
        self.canvas.grid(row=1, column=1)
        self.pattern = StringVar()
        # 图案选择按钮
        btRectangle = Button(frame5, text = "rectangle", command = self.displayRect)
        btOval = Button(frame5, text="Ellipse", command=self.displayOval)
        btArc = Button(frame5, text = "Arc", command = self.displayArc)
        btPolygon = Button(frame5, text="Polygon", command=self.displayPolygon)
        btLine = Button(frame5, text=" Line ", command=self.displayLine)
        btString = Button(frame5, text="Confirm", command=self.displayString)
        btClear = Button(frame5, text="Clear", command=self.clearCanvas)
        btRectangle.grid(row = 2, column = 6)
        btOval.grid(row=2, column=2)
        btArc.grid(row=2, column=3)
        btPolygon.grid(row=2, column=4)
        btLine.grid(row=2, column=5)
        btString.grid(row=2, column=1)
        btClear.grid(row=2, column=7)

        # 问题6放在frame6中
        frame6 = Frame(master)
        frame6.pack(fill=X)
        # 问题
        label6 = Label(frame6, text='6、What is your favoirte Course?   ')
        label6.grid(row=1, column=0)
        # 滚轮 (Scrollbar)
        scrollbar = Scrollbar(frame6)
        scrollbar.grid(row=1, column=2)
        # 列表
        self.listbox2 = Listbox(frame6,height=5, yscrollcommand=scrollbar.set)
        for i in range(99):
            self.listbox2.insert(END, str(i))
        self.listbox2.grid(row=1, column=1)
        scrollbar.config(command=self.listbox2.yview)
        # 确定按钮
        star = Button(frame6, text='Confirm', command=self.getstar)
        star.grid(row=2, column=1)

        # 问题7放在frame7中
        frame7 = Frame(master)
        frame7.pack(fill=X)
        # 问题
        label7 = Label(frame7, text='7、What is your favorite number：   ')
        label7.grid(row=1, column=0)
        # (Spinbox)
        self.number = Spinbox(frame7, from_=0, to=10)
        self.number.grid(row=1, column=1)
        # 确定按钮
        number = Button(frame7, text='Confirm', command=self.getnumber)
        number.grid(row=1, column=2)

        # 空格
        separator = Frame(master, height=30, bg='black', relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        # frame8
        frame8 = Frame(master)
        frame8.pack()
        self.agree = StringVar()
        # 勾择按钮（Checkbutton）
        agree = Checkbutton(frame8, text="I am ready to submit the survey", variable=self.agree, onvalue='Yes', offvalue='No', command=self.getagree)  # 产生选择按钮
        agree.grid()

        # frame9
        frame9 = Frame(master)
        frame9.pack()
        submit = Button(frame9, text='Submit', command=self.allsubmit)
        submit.grid()

        # frame10
        frame10 = Frame(master)
        frame10.pack()
        # 容器框 （LabelFrame）
        self.group = LabelFrame(frame10, text="Course Registration Survey", padx=5, pady=5)
        self.group.grid()
        w = Label(self.group, text='Author: https://github.com/StrikeR2018')
        w.pack()

        master.mainloop()

  # 属性
    # 文件栏
    def newfile(self):
        self.file = open(r'test.txt', 'w')
        self.file.close()
        messagebox.showinfo('New','Succeed to create info')   # 显示对话框
    def openfile(self):
        f = open(r'test.txt', 'r')
        try:
            f_read=f.read()
            #f_read_decode=f_read.decode('utf-8')
            print(f_read)
        finally:
            f.close()
    def savefile(self):
        messagebox.showwarning('Save', 'Remember to submit your survey!')    # 显示对话框

    # 编辑栏
    def red(self):
        self.group['bg'] = 'red'
    def blue(self):
        self.group['bg'] = 'blue'
    def yellow(self):
        self.group['bg'] = 'yellow'
    def nomal(self):
        self.group['bg'] = 'SystemButtonFace'

    # 帮助栏
    def description(self):
        messagebox.showinfo('Description', '1.Build your profile\n2.Fill in the survey\n3.Submit ')   # 显示对话框
    def about(self):
        messagebox.showinfo('about', 'This is a Course Registration System for student \n which you can Add Delete Search Student and courses!\n Lets filled in your information and got the registration done!\n')   # 显示对话框

    # 名字
    def getname(self):
        name = self.name.get()
        print(name)

    # 性别
    def getsex(self):
        sex = self.sex.get()
        print(sex)

    # 年龄
    def getage(self):
        print(self.age.get())

    # 语言
    def getlanguage(self):
        print(self.listbox.get(0, END))

    # 图案
    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")
        self.pattern = '长方形'
    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, tags = "oval", fill = "red")
        self.pattern = '椭圆'
    def displayArc(self):
        self.canvas.create_arc(10, 10, 190, 90, start = 0, extent = 90, width = 8, fill = "red", tags = "arc")
        self.pattern = '圆弧'
    def displayPolygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50, tags = "polygon")
        self.pattern = '多边形'
    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, fill = 'red', tags = "line")
        self.canvas.create_line(10, 90, 190, 10, width = 9, arrow = "last", activefill = "blue", tags = "line")
        self.pattern = '线'
    def displayString(self):
        self.canvas.create_text(60, 40, text = "Nicely done!", font = "Tine 10 bold underline", tags = "string")
        print(self.pattern)
    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")

    # 球星
    def getstar(self):
        print(self.listbox2.get(ACTIVE))

    # 数字
    def getnumber(self):
        print(self.number.get())

    # 同意
    def getagree(self):
        print(self.agree.get())

    # 提交
    def allsubmit(self):
        with open(r'test.txt', 'w') as f:
            f.write('Name：')
            f.write(self.name.get())
            f.write('\nGender:')
            f.write(self.sex.get())
            f.write('\nAge：')
            f.write(str(self.age.get()))
            f.write('\nLiked Course(s)：')
            for i in self.listbox.get(0, END):
                f.write(i)
                f.write(" ,")
            f.write('\nFavorite Shape：')
            f.write(self.pattern)
            f.write('\nFavorite Course：')
            f.write(self.listbox2.get(ACTIVE))
            f.write('\nFavorite Number：')
            f.write(self.number.get())
            f.write('\n')
            f.write(self.agree.get())
            f.write('')
        messagebox.showinfo('Success', 'Successfully Submitted ')   # 显示对话框

TkDemo()

