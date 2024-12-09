import tkinter as tk
from tkinter import ttk

#criando a janela e o loop:
window = tk.Tk()
window.geometry('600x4000')
window.title('Molduras e Paternidades')

#Frame:
frame = ttk.Frame(window, width= 200, height= 200, borderwidth= 10,relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='left')

#Configurações master:
label = ttk.Label(frame, text='Róotulo na Moldura definida')
label.pack()

button =  ttk.Button(frame, text= 'Botão na Moldura definida')
button.pack()

#exempo de label fora do frame definido
label2 = ttk.Label(master= window, text='Rótulo fora da Moldura definida')
label2.pack()

#Exercicio
#Crie outro quadro com um rótulo, um botão e uma entrada e coloque-o à direita
#Dos outros widgets

execise_frame = ttk.Frame(window)
execise_frame.pack(side= 'left')
ttk.Label(execise_frame, text='Rótulo na Moldura do exercicio.').pack()
ttk.Button(execise_frame, text='Botão do exercicio.').pack()
ttk.Entry(execise_frame).pack()


#Loop
window.mainloop()