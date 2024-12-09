import tkinter as tk 
from tkinter import ttk

#funções
def button_func():
    #get the content of the entry
    entry_text = entry.get()

    #update the label
    #labe.configure(text = 'some other text')
    label['text'] = entry_text
    entry['state'] = 'disable'
    #print(label.configure())

def reset_func():
    label['text'] = 'some text'
    entry['state'] = 'enable'


window = tk.Tk()
window.title('Getting and Setting Widgets')
window.geometry('600x400')
window.iconbitmap('python.ico')

#widget
label = ttk.Label(master= window, text= 'Algum Texto').pack()
entry = ttk.Entry(master= window,).pack()
button = ttk.Button(master= window, text = 'The Button', command = button_func).pack()

#Exercicio
#Adicionar outro botão que modifique os textos de 'some text' e cria uma entrada

exercise_button = ttk.Button(master = window, text = 'exercise button', command = reset_func).pack()


window.mainloop()