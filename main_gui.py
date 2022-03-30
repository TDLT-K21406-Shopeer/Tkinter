from tkinter import *
# class Example(Frame):
#     def __init__(self,height,weight):
#         Frame.__init__(self)
#         self.height=height
#         self.weight=weight
#
#     def bmi_index(self):
#         label_1=Label(wi)
# def make_center(root):
#     root.update_idletasks()
#     width = root.winfo_width()
#     height = root.winfo_height()
#     x = (root.winfo_screenwidth()//2)-(width//2)
#     y = (root.winfo_screenheight()//2)-(height//2)
#     root.geometry(f'{width}x{height} + {x}x{y}')

def bmi_index():
    a = float(string_height.get())
    b = float(string_weight.get())
    c = b/(a**2)
    if c<18.5:
        string_result.set('Gầy')
    elif c<=24.9:
        string_result.set('Bình thường')
    elif c<=29.9:
        string_result.set('Hơi béo')
    elif c<=34.9:
        string_result.set('Béo phì cấp độ I')
    elif c<39.9:
        string_result.set('Béo phì cấp độ II')
    else:
        string_result.set('Béo phì cấp độ III')

root=Tk()
string_height=StringVar()
string_weight=StringVar()
string_result=StringVar()

root.minsize(height=130,width=300)
Label(root,text='Chỉ số BMI',fg='red',bg='yellow',font=('Times New Roman',20),justify=LEFT).grid(row=0,column=1)

frameButton=Frame(root)
Button(frameButton,text='Kết quả',font=('Times New Roman',13),bg='black', fg='yellow' ,command=bmi_index).pack(fill=X)
frameButton.grid(row=3 ,column=0)

Label(root,text='Cân nặng (Kg)',bg='yellow',font=('Times New Roman',13)).grid(row=1,column=0)
Entry(root,width=20,textvariable=string_weight).grid(row=1,column=1)
Label(root,text='Chiều cao (m)',bg='yellow',font=('Times New Roman',13)).grid(row=2,column=0)
Entry(root,width=20,textvariable=string_height).grid(row=2,column=1)
Entry(root,width=20,textvariable=string_result).grid(row=3,column=1)

Button(root,text='Thoát',fg='yellow',bg='black',font=('Times New Roman',13),command=root.quit).grid(row=3, column=2)
root.configure(bg='yellow')
root.mainloop()