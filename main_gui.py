from tkinter import *
import tkinter.messagebox as mbox

def tiepAction():
    string_result.set('')
    string_advise.set('')
    string_weight.set('')
    string_height.set('')
    bmi.set('')

def bmi_index():
    try:
        a = float(string_height.get())
        b = float(string_weight.get())
    except:
        mbox.showerror('Error', 'Cân nặng và chiều cao là những số không âm \n=> Vui lòng nhập đúng dữ liệu')
    if a*b>0:
        c = round(b/(a**2),2)
        bmi.set(c)
    else:
        mbox.showerror('Error','Cân nặng và chiều cao là những số không âm \n=> Vui lòng nhập đúng dữ liệu')
    if c<18.5:
        string_result.set('Gầy')
        string_advise.set('Bạn cần tăng cường bổ sung dưỡng chất trong chế độ ăn uống hàng ngày.')
    elif c<23:
        string_result.set('Bình thường')
        string_advise.set('Bạn hãy tiếp tục chế độ sinh hoạt như hiện tại để duy trì chỉ số này.')
    elif c<25:
        string_result.set('Thừa cân')
        string_advise.set('Bạn cần giảm chất béo, tinh bột. Luyện tập thể thao ít nhất 80 phút hàng ngày.')
    elif c<30:
        string_result.set('Tiền béo phì')
        string_advise.set('Bạn cần ngay lập tức có kế hạch giảm cân khoa học và đến gặp bác sĩ để được tư vấn chuyên môn về nguyên nhân.')
    elif c<35:
        string_result.set('Béo phì cấp độ I')
        string_advise.set('Bạn cần gặp bác sĩ ngay để điều trị kịp thời.')
    elif c<40:
        string_result.set('Béo phì cấp độ II')
        string_advise.set('Bạn cần gặp bác sĩ ngay để điều trị kịp thời.')
    else:
        string_result.set('Béo phì cấp độ III')
        string_advise.set('Bạn cần gặp bác sĩ ngay để điều trị kịp thời.')
color_app='#CDCDB4'
font_app='Courier 13 bold'
root = Tk()

string_height=StringVar()
string_weight=StringVar()
string_result=StringVar()
string_advise=StringVar()
bmi=StringVar()

root.minsize(height=165,width=865)
Label(root,text='🌎 Chỉ số BMI 🌎',fg='black',bg=color_app,font='Courier 20 bold').grid(row=0,column=1)

frameButton=Frame(root)
Button(frameButton,text='Kết quả',font=font_app,bg='black', fg='white' ,command=bmi_index).pack(fill=X)
frameButton.place(x=777,y=37,width=80,height=24)

Label(root,text='Cân nặng (Kg)',bg=color_app,font=font_app).grid(row=1,column=0)
Entry(root,width=105,textvariable=string_weight).grid(row=1,column=1)
Label(root,text='Chiều cao (m)',bg=color_app,font=font_app).grid(row=2,column=0)
Entry(root,width=105,textvariable=string_height).grid(row=2,column=1)
Label(root,text= 'BMI',bg=color_app,font=font_app).grid(row=3,column=0)
Entry(root,width=105, textvariable=bmi).grid(row=3,column=1)
Label(root,text='Kết quả',bg=color_app,font=font_app).grid(row=4,column=0)
Entry(root,width=105,textvariable=string_result).grid(row=4,column=1)
Label(root,text='Lời khuyên',bg=color_app,font=font_app).grid(row=5,column=0)
Entry(root,width=105,textvariable=string_advise).grid(row=5,column=1)

Button(root,text='Tiếp',fg='white',bg='black',font=font_app,command=tiepAction).place(x=777,y=62,width=80,height=24)
Button(root,text='Thoát',fg='white',bg='red',font=font_app,command=root.quit).place(x=777,y=87,width=80,height=24)
root.configure(bg=color_app)
root.mainloop()
