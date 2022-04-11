#Import các thư viện
from tkinter import *
import tkinter.messagebox as mess
import smtplib
from tkinter.scrolledtext import ScrolledText
from turtle import st
from PIL import ImageTk, Image
import data_gui as d

# Tạo giao diện
class Root(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        self.title("BMI's new version")
        self.iconbitmap(".\Picture\logo.ico")
        # self.geometry("960x540")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames ={}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame("StartPage")
    
    # Hiển khung trong Frame
    def show_frame(self, page_name):
        '''Mở khung Frame thông qua tên'''
        frame = self.frames[page_name]
        frame.tkraise()

# Khung chính
class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.img = PhotoImage(file=".\Picture\header.png")
        Label(self,image=self.img).grid(row=0,column=0,columnspan=7)

        # Giới tính
        self.v0=IntVar()
        self.v0.set(1)
        Label(self,text="  Giới tính:",font= d.font_label).grid(row=1,column=0,sticky=W)

        r1=Radiobutton(self, text="Nam",font=d.font_button, variable=self.v0,value=1).grid(row=1,column=1)
        self.img1 = PhotoImage(file=".\Picture\man.png")
        Label(self,image=self.img1).grid(row=1,column=2)
        Label(self,text="   ").grid(row=1,column=3)

        r2=Radiobutton(self, text="Nữ",font=d.font_button, variable=self.v0,value=2).grid(row=1,column=4)
        self.img2 = PhotoImage(file=".\Picture\woman.png")
        Label(self,image=self.img2).grid(row=1,column=5)
        Label(self,text="   ").grid(row=1,column=6)

        # Tuổi
        self.v1=IntVar()
        self.v1.set(2)
        self.age = Spinbox(self, from_= 2, width=43,to=120,textvariable=self.v1)
        self.age.grid(row=2,column=1,columnspan=5)
        Label(self,text="  Độ tuổi:",font=d.font_label).grid(sticky=W,row=2,column=0)
        
        # Chiều cao
        self.v2=StringVar()
        self.v2.set("")
        self.height = Entry(self,width=45,textvariable=self.v2).grid(row=3,column=1,columnspan=5)
        Label(self,text="  Chiều cao(cm): ",font=d.font_label).grid(row=3,column=0,sticky=W)
        
        # Cân nặng
        self.v3=StringVar()
        self.v3.set("")
        self.weight = Entry(self,width=45,textvariable=self.v3).grid(row=4,column=1,columnspan=5)
        Label(self,text="  Cân nặng(kg): ",font=d.font_label).grid(row=4,column=0,sticky=W)
        
        # 
        self.bmi=StringVar()
        self.bmi.set("")
        check = Button(self, text="Kiểm tra", font=d.font_button, command=self.check)
        check.grid(row=5,column=1,columnspan=2,pady=10)
        self.result = Button(self, text="Kết quả", font=d.font_button, command=lambda: controller.show_frame("PageOne")).grid(row=5,column=4,columnspan=3,pady=10)

    # Kiểm tra dữ liệu nhập của người dùng    
    def check(self):
        try:
            age = int(self.v1.get())
            if age>=2 and age<=120:
                try:
                    height = float(self.v2.get())
                    if height<0:
                        mess.showerror("Lỗi","Chiều cao là một số dương")
                    else:
                        try:
                            weight = float(self.v3.get())
                            if weight<0:
                                mess.showerror("Lỗi","Cân nặng là một số dương")
                            else:
                                bmi_index = round(weight/((height/100)**2))
                                self.bmi.set(bmi_index)
                                # self.result.config(state=NORMAL)
                        except:
                            mess.showerror("Lỗi","Cân nặng là một số dương")
                except:
                    mess.showerror("Lỗi","Chiều cao là một số dương")
            elif age<2 and age>0:
                mess.showerror("Lỗi","Công thức chỉ áp dụng cho người từ 2 tuổi trở lên")
            elif age<0:
                mess.showerror("Lỗi","Tuổi là một số dương")
            else:
                mess.showerror("Lỗi","Kỷ lục thế giới về tuổi là 120") 
        except:
            mess.showerror("Lỗi","Tuổi là một số nguyên dương")

# Khung làm việc thứ 2
class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        Label(self, text="KQ", font="Courier 18").grid(row=0, column=0, columnspan=2)
        Label(self, text="   BMI:", font=d.font_label).grid(row=1, column=0, sticky=W)
        Entry(self, textvariable=controller)
        Button(self, text="Trở về", font=d.font_button, command=lambda: controller.show_frame("StartPage")).grid()

class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

# Sử dụng Menu
class MyMenu(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.MainMenu()

    def MainMenu(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)    
        fileMenu = Menu(menubar)    
        submenu = Menu(fileMenu)
        submenu.add_command(label="Thông tin", command=self.infor)
        submenu.add_command(label="Mail")
        submenu.add_command(label="Phiên bản", command=self.ver)
        fileMenu.add_cascade(label="Chi tiết", menu=submenu)
        fileMenu.add_command(label="Thoát", command=self.quit)
        menubar.add_cascade(label="Cài đặt", menu=fileMenu)

    def infor(self):
        mess.showinfo("Thông tin","Đây là sản phẩm của nhóm 4")

    def ver(self):
        mess.showinfo("Phiên bản","Đây là phiên bản 2.0")

if __name__ == "__main__":
    root = Root()
    app = MyMenu(root)
    root.mainloop()