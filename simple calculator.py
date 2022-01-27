from tkinter import *

root = Tk()
root.title('Calculator')

#creating display and placing it on the screen
e = Entry(root, width=20, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=5, pady=2)

#adding functions to the buttons
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_plus():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)

def button_minus():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)

def button_times():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)

def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)

def button_equal():
    second_num = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + int(second_num))
    if math == 'subtraction':
        e.insert(0, f_num - int(second_num))
    if math == 'multiplication':
        e.insert(0, f_num * int(second_num))
    if math == 'division':
        e.insert(0, f_num / int(second_num))

#creating buttons and changing size
myButton1 = Button(root, text='1', padx=20, pady=20, command=lambda: button_click(1))
myButton2 = Button(root, text='2', padx=20, pady=20, command=lambda: button_click(2))
myButton3 = Button(root, text='3', padx=20, pady=20, command=lambda: button_click(3))
myButton4 = Button(root, text='4', padx=20, pady=20, command=lambda: button_click(4))
myButton5 = Button(root, text='5', padx=20, pady=20, command=lambda: button_click(5))
myButton6 = Button(root, text='6', padx=20, pady=20, command=lambda: button_click(6))
myButton7 = Button(root, text='7', padx=20, pady=20, command=lambda: button_click(7))
myButton8 = Button(root, text='8', padx=20, pady=20, command=lambda: button_click(8))
myButton9 = Button(root, text='9', padx=20, pady=20, command=lambda: button_click(9))
myButton0 = Button(root, text='0', padx=20, pady=20, command=lambda: button_click(0))
myButtonplus = Button(root, text='+', padx=20, pady=20, command=button_plus)
myButtonminus = Button(root, text='-', padx=20, pady=20, command=button_minus)
myButtontimes = Button(root, text='x', padx=20, pady=20, command=button_times)
myButtondivide = Button(root, text='÷', padx=20, pady=20, command=button_divide)
myButtonequals = Button(root, text='=', padx=61, pady=20, command=button_equal)
myButtonclear = Button(root, text='C', padx=20, pady=20, command=button_clear)

#placing buttons on screen
myButton1.grid(row=1, column=0)
myButton2.grid(row=1, column=1)
myButton3.grid(row=1, column=2)
myButton4.grid(row=2, column=0)
myButton5.grid(row=2, column=1)
myButton6.grid(row=2, column=2)
myButton7.grid(row=3, column=0)
myButton8.grid(row=3, column=1)
myButton9.grid(row=3, column=2)
myButton0.grid(row=4, column=0)
myButtonplus.grid(row=1, column=3)
myButtonminus.grid(row=2, column=3)
myButtontimes.grid(row=3, column=3)
myButtondivide.grid(row=4, column=3)
myButtonequals.grid(row=4, column=1, columnspan=2)
myButtonclear.grid(row=0, column=3)

root.mainloop()
