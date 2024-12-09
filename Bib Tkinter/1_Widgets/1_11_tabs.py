import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Tab widget')

#Notebook widget:
notebook = ttk.Notebook(window)

#tab1:
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text='Texto no tab 1').pack()
button1 = ttk.Button(tab1, text='Botão em tab 1').pack()

#tab2:
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text='Texto em tab 2').pack()
button2 = ttk.Button(tab2, text='Botão em tab 2').pack()
entry2 = ttk.Entry(tab2,).pack()

notebook.add(tab1, text='tab1')
notebook.add(tab2, text='tab2')


#Exercicio
#Adicione outra aba com 2 botões e um rótulo dentro
tab_exercise = ttk.Frame(notebook)
exercise_button1 = ttk.Button(tab_exercise, text='Botão 1').pack()
exercise_button2 = ttk.Button(tab_exercise, text='Botão 2').pack()
exercise_label = ttk.Label(tab_exercise, text='Rótulo').pack()

notebook.add(tab_exercise, text='Tab exercise')
notebook.pack()


window.mainloop()