import tkinter as tk
from tkinter import ttk

#Fuções
def button_func():
    print(string_var.get())
    string_var.set('button pressed')


window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('600x400')
window.iconbitmap('python.ico')

#Variáveis
string_var = tk.StringVar()

#Widgets
label = ttk.Label(master= window, text = 'label', textvariable= string_var).pack()
entry = ttk.Entry(master= window, textvariable= string_var).pack()
button = ttk.Button(master= window, text= 'Button', command= button_func).pack()

#Exercicio 
#Criar 2 campos de entrada e um Rotulo, onde tudo vai estar conectado via o StringVar
#Colocar um valor de inicio como 'test'
exercise_var = tk.StringVar(value='test')

entry1 = ttk.Entry(master= window, textvariable= exercise_var).pack()
entry2 = ttk.Entry(master= window, textvariable= exercise_var).pack()
exercise_label = ttk.Label(master= window, textvariable= exercise_var).pack()


window.mainloop()