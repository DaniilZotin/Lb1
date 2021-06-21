import tkinter as tk

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
    
def calculate():
     value = calc.get()
     if value[-1] in '+-*/':
         value = value+value[:-1]
     calc.delete(0,tk.END)
     calc.insert(0,eval(value))

#Функція для кнопки з очисткою Entry
def clear():
    calc.delete(0,tk.END)
    calc.insert(0,0)


#Функція для створення кнопки і ШРИФТ!!! це реальний шрифт який викоритовується для калькулятора Windows   
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

#Ввод з клавіатури приймає усі символи але відображає тільки числа 
def press_key(event):
    print(event.char)
    if event.char.isdigit():
        add_number(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    

win = tk.Tk()
w = 245
h = 270
win.geometry(f"{w}x{h}-10+10")
win['bg'] = '#00CCCC'
win.title('Калькуляор')

#Метод для вводу з клавіатури
win.bind('<Key>', press_key)


#Поле в яке вноситься вся інформація та критерій справа важливо 
calc = tk.Entry(win, justify=tk.RIGHT, font = ('Segoe UI', 15),width=15)
calc.insert(0,'0')
calc.grid(row=0,column=0,columnspan=4, sticky='we')

#Візуалка кнопок 
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

make_equally_button('=').grid(row=4,column=3,sticky='wens',padx=5,pady=5)
make_delete_button('C').grid(row=1,column=3,sticky='wens',padx=5,pady=5)


#Мінімальна ширина стовбця з кнопками (або з іншими елементами)
win.grid_columnconfigure(0,minsize = 60)
win.grid_columnconfigure(1,minsize = 60)
win.grid_columnconfigure(2,minsize = 60)
win.grid_columnconfigure(3,minsize = 60)

#Мінімальна висота рядка з кнопками (або з іншими елементами)
win.grid_rowconfigure(1,minsize = 20)
win.grid_rowconfigure(2,minsize = 60)
win.grid_rowconfigure(3,minsize = 60)
win.grid_rowconfigure(4,minsize = 60)


win.mainloop()

