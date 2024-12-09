import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')
window.iconbitmap('python.ico')

#Button
def button_func():
    print('Um botão Básico !')
    #print(radio_var.get())

button_string = tk.StringVar(value= ' A button with string var')
button = ttk.Button(window, text= 'Um simples Botão', command= button_func, textvariable= button_string).pack()

#CheckButton
check_var = tk.IntVar(value= 10)

check1 = ttk.Checkbutton(
    window,
    text = 'checkbox1',
    command= lambda: print(check_var.get()),
    variable =check_var,
    onvalue = 10,
    offvalue = 5
).pack()

check2 = ttk.Checkbutton(
    window,
    text = 'Checkbox 2',
    command= lambda: check_var.set(5),
).pack()

#radio buttons
radio_var =tk.StringVar()

radio1 = ttk.Radiobutton(
    window,
    text = 'RadioButton 1',
    value= 1,
    variable= radio_var,
    command= lambda: print(radio_var.get())
).pack()

radio2 = ttk.Radiobutton(
    window,
    text = 'RadioButton 2',
    value= 1,
    variable= radio_var
).pack()


window.mainloop()