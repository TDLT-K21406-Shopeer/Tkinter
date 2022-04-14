#Import các thư viện
from tkinter import *
import tkinter.messagebox as mess
import data_gui as d

# Tạo giao diện
class Root(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("BMI's new version")
        self.iconbitmap(".\Picture\logo.ico")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.resizable(False,False)

        self.frames ={}
        for F in (StartPage, PageResult):
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

        r2=Radiobutton(self, text="Nữ",font=d.font_button, variable=self.v0,value=2).grid(row=1,column=4)
        self.img2 = PhotoImage(file=".\Picture\woman.png")
        Label(self,image=self.img2).grid(row=1,column=5)
        Label(self,text="      ").grid(row=1,column=6)
        
        # Tuổi
        self.v13=IntVar()
        self.v13.set(0)
        self.age = Spinbox(self, from_= 2, width=29, to=120, font=d.font_button, textvariable=self.v13)
        self.age.grid(row=2,column=1,columnspan=6)
        Label(self,text="  Độ tuổi:",font=d.font_label).grid(sticky=W,row=2,column=0)
        
        # Chiều cao
        self.v2=StringVar()
        self.v2.set("")
        self.height = Entry(self, width=30, font=d.font_button, textvariable=self.v2).grid(row=4,column=1,columnspan=6)
        Label(self,text="  Chiều cao(cm): ",font=d.font_label).grid(row=4,column=0,sticky=W)
        
        # Cân nặng
        self.v3=StringVar()
        self.v3.set("")
        self.weight = Entry(self, width=30, font=d.font_button, textvariable=self.v3).grid(row=5,column=1,columnspan=6)
        Label(self,text="  Cân nặng(kg): ",font=d.font_label).grid(row=5,column=0,sticky=W)
        
        # Nút lệnh
        check = Button(self, text="Kiểm tra", font=d.font_label, fg=d.color_fg, bg=d.color_bg, command=self.check)
        check.grid(row=6,column=1,columnspan=2,pady=10)
        self.result = Button(self, text="Tiếp tục", font=d.font_label, fg=d.color_fg, bg=d.color_bg, state=DISABLED, command=lambda: controller.show_frame("PageResult"))
        self.result.grid(row=6,column=4,columnspan=3,pady=10)

    # Kiểm tra dữ liệu nhập của người dùng    
    def check(self):
        try:
            age = int(self.v13.get())
            if age>=7 and age<=120:
                try:
                    height = float(self.v2.get())
                    if height<=0:
                        mess.showerror("Lỗi","Chiều cao là một số dương")
                    elif height>251:
                        mess.showerror("Lỗi","Kỷ lục chiều cao trên thế giới là 251 cm")
                    else:
                        try:
                            weight = float(self.v3.get())
                            if weight<=0:
                                mess.showerror("Lỗi","Cân nặng là một số dương")
                            elif weight>595:
                                mess.showerror("Lỗi","Kỷ lục về cân nặng trên thế giới là 595 kg")
                            else:
                                # Ghi kết quả vào file txt
                                temp = open("temp.txt","w",encoding="utf-8")
                                temp.write(f"{self.v0.get()}\n")
                                temp.write(f"{age}\n")
                                temp.write(f"{height}\n")
                                temp.write(f"{weight}")
                                temp.close()
                                mess.showinfo("Thông báo","Bạn đã nhập xong dữ liệu, hãy chọn vào Tiếp tục")
                                self.result['state'] = NORMAL
                        except:
                            mess.showerror("Lỗi","Cân nặng là một số dương")
                except:
                    mess.showerror("Lỗi","Chiều cao là một số dương")
            elif age<7 and age>0:
                mess.showerror("Lỗi","Công thức chỉ nên áp dụng cho trẻ từ 7 tuổi trở lên")
            elif age<0:
                mess.showerror("Lỗi","Tuổi là một số dương")
            else:
                mess.showerror("Lỗi","Kỷ lục thế giới về tuổi là 120 tuổi") 
        except:
            mess.showerror("Lỗi","Tuổi là một số nguyên dương")

# Khung làm việc thứ 2
class PageResult(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.label_first = Label(self, text="Đây là chỉ số BMI của bạn", font="Courier 18").grid(row=0, column=0, columnspan=3)
        Label(self, text="   BMI:", font=d.font_label).grid(row=1, column=0, sticky=W)

        self.str_bmi=StringVar()
        self.str_state=StringVar()
        Label(self,text="   Đánh giá:",font=d.font_label).grid(row=2,column=0,sticky=W)
        Button(self, text="Kết quả", fg=d.color_fg, bg=d.color_bg, font=d.font_label, command=self.show_result).grid(row=0,column=4)
        Button(self, text="Xóa kết quả", fg=d.color_bg, bg=d.color_fg, font=d.font_label, command=self.reset).grid(row=4,column=3,columnspan=2)
        Button(self, text="Trở về", fg=d.color_fg, bg=d.color_bg, font=d.font_label, command=lambda: controller.show_frame("StartPage")).grid(row=4,column=2)
    
    def show_result(self):
        pic=0
        with open("temp.txt","r") as f:
            data_list = f.readlines()
        l_strip=[]
        for s in data_list:
            l_strip.append(s.strip())
        bmi=round(float(l_strip[3])/((float(l_strip[2])/100)**2),2)
        self.str_bmi.set(bmi)
        Label(self, text=self.str_bmi.get(), font=d.font_button).grid(row=1,column=1,columnspan=2,pady=5,sticky=W)
        # state="Loading"
        if int(l_strip[1])>18:
            if bmi<d.adult_bmi[0]:
                state = d.adult_state[0]
            elif bmi<d.adult_bmi[1]:
                state = d.adult_state[1]
            elif bmi<d.adult_bmi[2]:
                state = d.adult_state[2]
            elif bmi<d.adult_bmi[3]:
                state = d.adult_state[3]
                pic=1
            elif bmi<d.adult_bmi[4]:
                state = d.adult_state[4]
            elif bmi<d.adult_bmi[5]:
                state = d.adult_state[5]
            elif bmi<d.adult_bmi[6]:
                state = d.adult_state[6]
            else:
                state = d.adult_state[7]
        else:
            idx = d.age_child.index(int(l_strip[1]))
            if int(l_strip[0])==1:
                if bmi<d.child_bmi_male[idx][0]:
                    state = d.child_state[0]
                elif bmi<d.child_bmi_male[idx][1]:
                    state = d.child_state[1]
                    pic=1
                elif bmi<d.child_bmi_male[idx][2]:
                    state = d.child_state[2]
                else:
                    state = d.child_state[3]
            else:
                if bmi<d.child_bmi_female[idx][0]:
                    state = d.child_state[0]
                elif bmi<d.child_bmi_female[idx][1]:
                    state = d.child_state[1]
                    pic=1
                elif bmi<d.child_bmi_female[idx][2]:
                    state = d.child_state[2]
                else:
                    state = d.child_state[3]
        self.str_state.set(state)
        Label(self,text=self.str_state.get(),font=d.font_button).grid(row=2,column=1,columnspan=2,sticky=W)
        if pic==1:
            self.img = PhotoImage(file=".\Picture\healthy.png")
            Label(self,image=self.img).grid(row=3,column=0,columnspan=5)
        else:
            self.img = PhotoImage(file=".\Picture\doctor.png")
            Label(self,image=self.img).grid(row=3,column=0,columnspan=5)

    def reset(self):
        self.str_bmi.set("                                     ")
        self.str_state.set("                                      ")
        Label(self, text=self.str_bmi.get(), font=d.font_button).grid(row=1,column=1,columnspan=2,pady=5,sticky=W)
        Label(self,text=self.str_state.get(),font=d.font_button).grid(row=2,column=1,columnspan=2,sticky=W)
        self.img = PhotoImage(file=".\Picture\delete.png")
        Label(self,image=self.img).grid(row=3,column=0,columnspan=5)

# Sử dụng Menu
class MyMenu(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.MainMenu()

    def MainMenu(self):
        mbar = Menu(self.parent)
        self.parent.config(menu=mbar)    
        settingMenu = Menu(mbar)    
        submenu = Menu(settingMenu)
        submenu.add_command(label="Thông tin", command=self.infor)
        submenu.add_command(label="Mail",command=self.show_mail)
        submenu.add_command(label="Phiên bản", command=self.ver)
        settingMenu.add_cascade(label="Chi tiết", menu=submenu)
        settingMenu.add_command(label="Thoát", command=self.quit)
        mbar.add_cascade(label="Cài đặt", menu=settingMenu)

    def infor(self):
        mess.showinfo("Thông tin","Đây là sản phẩm của nhóm 4")

    def ver(self):
        mess.showinfo("Phiên bản","Đây là phiên bản 2.0")
    
    def show_mail(self):
        mess.showinfo("Thông báo","Chúng tôi sẽ bổ sung tính năng này sau nhằm mục đích để nhận những góp ý của người dùng về chương trình của chúng tôi")