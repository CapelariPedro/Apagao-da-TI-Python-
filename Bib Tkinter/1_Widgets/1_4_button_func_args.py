import tkinter as tk
from tkinter import ttk

#Functions
def button_func():
    print('a button was pressed')
    print(entry_string.get())
'''
def outer_func(parameter):
    def inner_func():
        print('a button was pressed')
        print(parameter.get())
    return inner_func
'''
#Setup
window = tk.Tk()
window.title('Button Functions and Arguments')
window.geometry('600x400')
window.iconbitmap('python.ico')

#widgets
entry_string = tk.StringVar(value= 'test')

entry = ttk.Entry(
    window,
    textvariable= entry_string
).pack()

button = ttk.Button(
    window,
    text = 'Button',
    command= lambda: button_func(entry_string)
).pack()

window.mainloop()