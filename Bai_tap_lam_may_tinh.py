#%%Bài tập làm máy tính
from tkinter import *
def plus_():
    global operator#khởi tạo biến toàn cục
    dau.configure(text = '+')
    operator=1
def minus_():
    global operator
    dau.configure(text = '-')
    operator=2
def multi_():
    global operator
    dau.configure(text = 'x')
    operator=3
def divid_():
    global operator
    dau.configure(text = '/')
    operator=4
def calculate():
    global operator
    a=int(value_No1.get())
    b=int(value_No2.get())
    result.delete(0,END)
    if operator==1:
        result.insert(0,a+b)
    if operator==2:
        result.insert(0,a-b)
    if operator==3:
        result.insert(0,a*b)
    if operator==4:
        result.insert(0,a/b)


root = Tk()
root.geometry('300x300')
root.title('caculate')

number1 = Label(text='No.1', font=('Verdana', 16, 'bold'))
number2 = Label(text='No.2', font=('Verdana', 16, 'bold'))
dau=Label(text=' ')

value_No1= Entry(font=('Verdana', 16), width=4)
value_No2= Entry(font=('Verdana', 16), width=4)
result   = Entry(font=('Verdana', 16), width=4)

plus_button  = Button(text='+', font=('Verdana', 16),command=plus_)
minus_button = Button(text='-', font=('Verdana', 16),command=minus_)
multi_button = Button(text='x', font=('Verdana', 16),command=multi_)
divid_button = Button(text='/', font=('Verdana', 16),command=divid_)
equal_button = Button(text='=', font=('Verdana', 16),command=calculate)

number1.grid(row=0, column=0)
number2.grid(row=0, column=3)
dau.grid(row=1, column=2)
value_No1.grid(row=1, column=0,columnspan=2)
value_No2.grid(row=1, column=3,columnspan=2)
result.grid(row=4, column=1,columnspan=3)
plus_button.grid(row=2, column=0)
minus_button.grid(row=2, column=1)
multi_button.grid(row=2, column=3)
divid_button.grid(row=2, column=4)
equal_button.grid(row=3, column=2)

mainloop()