#%%Bai1 Tạo một giao diện để đổi ngoại tệ
#import thư viện
from tkinter import *

#hàm tính
def calculate():

    try:                                                                    
        b=0
        a=(E1.get())
        a=int(a)
        if color.get()==0:
            L1.configure(text = 'Mời nhập loại ngoại tệ')           
            E1.delete(0,END)
        if color.get()==1:
            b=a*22000
            L1.configure(text = 'GIá trị quy đổi:  {:.1f} vnd'.format(b))           
            E1.delete(0,END)
        if color.get()==2:
            b=a*26000
            L1.configure(text = 'GIá trị quy đổi:  {:.1f} vnd'.format(b))           
            E1.delete(0,END)
        if color.get()==3:
            b=a*200
            L1.configure(text = 'Giá trị quy đổi:  {:.1f} vnd'.format(b))           
            E1.delete(0,END)
    except:
        L1.configure(text = 'Nhập giá trị quy đổi')           
        E1.delete(0,END)
    

root = Tk()
root.geometry('600x300')
root.title('MONEY EXCHANGE')

color = IntVar()
USD_button = Radiobutton(text='USD:22.000', var=color, value=1)
EUR_button = Radiobutton(text='EUR:26000', var=color, value=2)
JYP_button = Radiobutton(text='JYP:200   ', var=color, value=3)
EXCHANGE_button=Button( text='EXCHANGE',width=15,heigh=1,command=calculate)

E1=Entry(text='0',font=('Verdana', 16))
L1 = Label(text='GIá trị quy đổi: vnd',font=('Verdana', 16), fg='blue')

L1.grid(row=3, column=1)
USD_button.grid(row=0, column=0)
EUR_button.grid(row=1, column=0)
JYP_button.grid(row=2, column=0)
EXCHANGE_button.grid(row=1, column=1,columnspan=2)
E1.grid(row=0, column=1)

print(color.get())
mainloop()
#%%Bai2 Tạo một giao diện để tính chỉ số cơ thể BMI
from tkinter import *

def Metric_():
    L1.configure(text='CHIỀU CAO(cm)')
    L2.configure(text='CÂN NẶNG(kg)')

def English_():
    L1.configure(text='HEIGHT (Inches)')
    L2.configure(text='WEIGHT (Pounds)')
def calculate():
    try:
        taget=0
        a=int(E1.get())
        b=int(E2.get())
        if color.get()==0:
            L3.configure(text = 'Chọn đơn vị quy đổi')           
            E1.delete(0,END)
            E2.delete(0,END)
        if color.get()==1:
            taget= b/ ((a/100)*(a/100))
            L3.configure(text = 'BMI= {:.1f} '.format(taget))           
            E1.delete(0,END)
            E2.delete(0,END)
        if color.get()==2:
            taget=(b/(a*a))*703
            L3.configure(text = 'BMI= {:.1f} '.format(taget))           
            E1.delete(0,END)
            E2.delete(0,END)

 
    except:
        L3.configure(text = 'Nhập giá trị quy đổi')           
        E1.delete(0,END)
        E2.delete(0,END)


root = Tk()
root.geometry('600x300')
root.title('BMI CALCULATOR')

color = IntVar()
Metric_button = Radiobutton(text='Metric', var=color, value=1,command=Metric_)
English_button = Radiobutton(text='English', var=color, value=2,command=English_)
CALCULATE_button=Button( text='CALCULATE',width=15,heigh=1,command=calculate)

E1=Entry(text='',font=('Verdana', 16),width=10)
E2=Entry(text='',font=('Verdana', 16),width=10)

L1 = Label(text='CHIỀU CAO(cm)',font=('Verdana', 16))
L2 = Label(text='CÂN NẶNG(kg)',font=('Verdana', 16))
L3 = Label(text='BMI=',font=('Verdana', 16))

L1.grid(row=0, column=0)
L2.grid(row=2, column=0)
L3.grid(row=5, column=2)
Metric_button.grid(row=0, column=3)
English_button.grid(row=1, column=3)
CALCULATE_button.grid(row=4, column=2,columnspan=2)
E1.grid(row=1, column=0,columnspan=2)
E2.grid(row=3, column=0,columnspan=2)



mainloop()