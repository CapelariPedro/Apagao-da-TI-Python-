import tkinter as tk
from tkinter import ttk

#def de funções:
def button_func():
    print('O botão foi prescionado ')

def exercise_button_fun():
    print('hello')

#criando uma janela para a aplicação:
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

#ttk rótulo:
label = ttk.Label(master= window, text = "Isto é um teste")
label.pack()

#tk texto:
text = tk.Text(master= window)
label.pack()

#tk entrada:
entry = ttk.Entry(master= window)
entry.pack()

#exercicio do rótulo:
exercise_label = ttk.Label(master= window, text ='Meu  rotútlo')
exercise_label.pack()

#ttk botão:
button = ttk.Button(master= window, text = 'Um Botão', command= button_func)
button.pack()

#Exercicio 
#Adicionar mais um rótulo de texto e um botão com uma função que imprime 'olá'
#O rótulo deve dizer "meu rótulo" e estar entre o widget de entrada e o botão

#Resolução do exercicio:
exercise_button = ttk.Button(master= window, text='Botão do exercicio', command= exercise_button_fun)
exercise_button.pack()


#mantem a janela aberta em loop:
window.mainloop()