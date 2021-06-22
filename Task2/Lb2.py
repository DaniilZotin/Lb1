import tkinter as tk
import math 
from tkinter import messagebox
from tkinter.constants import INSERT


#Додавання цифер в Entry, видаленння 0 і запис інших цифер
def add_number(number):
    value = calc.get() 
    if value [0] == '0' and len(value) == 1:
        value = value [1:]
    calc.delete(0,tk.END)
    calc.insert(0,value + number)

#Функція для зміни операції (тобто тепер не можна ввести декілька плюсів підряд) 
def add_operation(oper):
    value = calc.get() 
    if value [-1] in '-+*/':
        value = value [:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get() 
    calc.delete(0,tk.END)
    calc.insert(0,value + oper)
    
#Функція для підрахунку але якщо букви або інші символи повідомлення про помилку    
def calculate():
     value = calc.get()
     if value[-1] in '+-*/':
         value = value+value[:-1]
     calc.delete(0,tk.END)
     try:
         calc.insert(0,eval(value))
     except (NameError, SyntaxError):
         messagebox.showinfo('Увага','Потрібно вводити тільки числа ! Ви ввели інші символи')
         calc.insert(0,0)
     except (ZeroDivisionError):
         messagebox.showinfo('Увага','На нуль ділити не можна')
         calc.insert(0,0)

     


#Функція для кнопки з очисткою Entry
def clear():
    calc.delete(0,tk.END)
    calc.insert(0,0)

def log():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value [:-1] 
    calc.delete(0,tk.END)
    calc.insert(0,math.log10(float(value)))

def ctg():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value [:-1] 
    calc.delete(0,tk.END)
    calc.insert(0,1/math.tan(math.radians(float(value))))

#Іноді в коді бувають моменти за які стидно от це іменно він 
def percent():
    value = calc.get()
    if '*' in value:
        calc.delete(0,tk.END)
        calc.insert(0,eval(value+'/100'))
    elif '/' in value:
        calc.delete(0,tk.END)
        calc.insert(0,eval(value)*100)
    elif '+' in value:
        sr=''
        for i in range(len(value)):
            if value[i]!='+' and value[i]!='-':
                sr=sr+value[i]
            else:
                break
        calc.delete(0,tk.END)
        calc.insert(0,eval(value+'/100*'+sr))
    elif '-' in value:
        sr=''
        for i in range(len(value)):
            if value[i]!='+' and value[i]!='-':
                sr=sr+value[i]
            else:
                break
        calc.delete(0,tk.END)
        calc.insert(0,eval(value+'/100*'+sr))
    else:
        calc.delete(0,tk.END)
        calc.insert(0,'0')

def ln():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value [:-1] 
    calc.delete(0,tk.END)
    calc.insert(0,math.log(float(value)))

def sin():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,math.sin(math.radians(float(value))))

def tan():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,math.tan(math.radians(float(value))))

def cos():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,math.cos(math.radians(float(value))))

def binar():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,bin(int(value)))




#Функція для створення кнопки з числами і ШРИФТ!!! це реальний шрифт який викоритовується для калькулятора Windows   
def make_number_button(number):
    return tk.Button(text=number,bd=5, font = ('Segoe UI',13),command=lambda : add_number(number))

def make_oper_button(oper):
    return tk.Button(text=oper,bd=5, font = ('Segoe UI',13), fg = 'red',
                                            command=lambda : add_operation(oper))
                                        
def make_equally_button(oper):
    return tk.Button(text=oper,bd=5, font = ('Segoe UI',13), fg = 'red',
                                            command=calculate)

def make_delete_button(oper):
    return tk.Button(text=oper,bd=5, font = ('Segoe UI',13), fg = 'red',
                                            command=clear)
def make_log_button(oper):
    return tk.Button(text=oper,bd=5, font = ('Segoe UI',10), fg = 'red',
                                            command=log)

def make_ctg_button(oper):
    return tk.Button(text=oper,bd=5, font = ('Segoe UI',10), fg = 'red',
                                            command=ctg)

def make_percent_button(oper):
    return tk.Button(text=oper,bd=5, font = ('Segoe UI',10), fg = 'red',
                                            command=percent)

def make_ln_button(oper):
    return tk.Button(text=oper,bd=5, font = ('Segoe UI',10), fg = 'red',
                                            command=ln)

def make_sin_button(oper):
    return tk.Button(text=oper, bd=5,font = ('Segoe UI', 10), fg = 'red',
                                             command=sin)

def make_tan_button(oper):
    return tk.Button(text=oper, bd=5,font = ('Segoe UI', 10), fg = 'red',
                                             command=tan)

def make_cos_button(oper):
    return tk.Button(text=oper, bd=5,font = ('Segoe UI', 10), fg = 'red',
                                             command=cos)

def make_binar_button(oper):
    return tk.Button(text=oper, bd=5,font = ('Segoe UI', 10), fg = 'red',
                                             command=binar)



#Ввод з клавіатури приймає усі символи але відображає тільки числа 
def press_key(event):
    print(event.char)
    if event.char.isdigit():
        add_number(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    
#Налаштування головного вікна
win = tk.Tk()
w = 295
h = 360
win.geometry(f"{w}x{h}-10+10")
win['bg'] = '#00CCCC'
win.title('Калькуляор')

#Метод для вводу з клавіатури
win.bind('<Key>', press_key)


#Поле в яке вноситься вся інформація та критерій справа важливо 
calc = tk.Entry(win, justify=tk.RIGHT, font = ('Segoe UI', 15),width=15)
calc.insert(0,'0')
calc.grid(row=0,column=0,columnspan=5, sticky='we')

#Візуалка кнопок плюс деякі характеристики
make_number_button('1').grid(row=1,column=0,sticky='wens',padx=5,pady=5)
make_number_button('2').grid(row=1,column=1,sticky='wens',padx=5,pady=5)
make_number_button('3').grid(row=1,column=2,sticky='wens',padx=5,pady=5)
make_number_button('4').grid(row=2,column=0,sticky='wens',padx=5,pady=5)
make_number_button('5').grid(row=2,column=1,sticky='wens',padx=5,pady=5)
make_number_button('6').grid(row=2,column=2,sticky='wens',padx=5,pady=5)
make_number_button('7').grid(row=3,column=0,sticky='wens',padx=5,pady=5)
make_number_button('8').grid(row=3,column=1,sticky='wens',padx=5,pady=5)
make_number_button('9').grid(row=3,column=2,sticky='wens',padx=5,pady=5)
make_number_button('0').grid(row=4,column=0,sticky='wens',padx=5,pady=5)

make_oper_button('+').grid(row=4,column=1,sticky='wens',padx=5,pady=5)
make_oper_button('-').grid(row=2,column=3,sticky='wens',padx=5,pady=5)
make_oper_button('*').grid(row=3,column=3,sticky='wens',padx=5,pady=5)
make_oper_button('/').grid(row=4,column=2,sticky='wens',padx=5,pady=5)
make_log_button('log').grid(row=5,column=0,sticky='wens',padx=5,pady=5)
make_ctg_button('ctg').grid(row=5,column=1,sticky='wens',padx=5,pady=5)
make_percent_button('%').grid(row=6,column=4, stick='we', padx=5, pady=5)
make_ln_button('ln').grid(row=5,column=3, stick='wens', padx=5, pady=5)
make_sin_button('sin').grid(row=6,column=0,columnspan=2, stick='we', padx=5, pady=5)
make_tan_button('tan').grid(row=6,column=2,columnspan=2, stick='we', padx=5, pady=5)
make_cos_button('cos').grid(row=5,column=2, stick='we', padx=5, pady=5)

make_binar_button('Bin').grid(row=1,column=4,rowspan=5, stick='wens', padx=5, pady=5)
make_equally_button('=').grid(row=4,column=3,sticky='wens',padx=5,pady=5)
make_delete_button('C').grid(row=1,column=3,sticky='wens',padx=5,pady=5)


#Мінімальна ширина стовбця з кнопками (або з іншими елементами)
win.grid_columnconfigure(0,minsize = 60)
win.grid_columnconfigure(1,minsize = 60)
win.grid_columnconfigure(2,minsize = 60)
win.grid_columnconfigure(3,minsize = 60)
win.grid_columnconfigure(4,minsize = 55)

#Мінімальна висота рядка з кнопками (або з іншими елементами)
win.grid_rowconfigure(1,minsize = 20)
win.grid_rowconfigure(2,minsize = 60)
win.grid_rowconfigure(3,minsize = 60)
win.grid_rowconfigure(4,minsize = 60)
win.grid_rowconfigure(5,minsize = 1)


win.mainloop()

