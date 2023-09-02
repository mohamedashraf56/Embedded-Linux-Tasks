#!/usr/bin/python3
from math import factorial as fc
from tkinter import *

window = Tk()
window.title('Calc The Factorial')
window.geometry("400x90+400+250")
window.resizable(False,False)

Var = StringVar()
Var.set('')

# Calc the factorial 

def factorial():
    val = int(number.get())
    Var.set(f'The factorial of {val}! = {fc(val)}')
    window.update_idletasks

lb1 = Label(window,text="Enter An Integer NUM : ")
output = Label(window,textvariable=Var)
number = Entry(window)
validateButton = Button(window,text="EQUAL",fg="RED",bg="Purple",command=factorial)

lb1.grid(row=0,column=0)
output.grid(row=1,column=1)
number.grid(row=0,column=1)
validateButton.grid(row=3,column=1)

window.mainloop()
