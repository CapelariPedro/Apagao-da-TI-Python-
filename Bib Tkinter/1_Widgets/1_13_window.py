import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.title('Mais sobre Janelas')
#window.geometry('600x400x100x2000')


#Exercicio
#Começar a janela no meio  da tela 
window_width = 1400
window_height = 600
display_width = window.winfo_screenmmwidth()
display_height = window.winfo_screenheight()

left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

#Tamanho da Janela
window.minsize(200,100)
#window.maxsize(800,700)
#window.resizable(True, False)

#Atribultos da Tela
print(window.winfo_screenwidth())
print(window.winfo_screenmmheight())

#Atributos da Janela
window.attributes('-alpha', 1)
#window.attributes('-topmost', True)

#security event
#window.bind('<Escaape>', lambda event: window.quit())

#window.attributes('-disable', True)
#window.attributes('-fullscreen', True)

#Title Bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se')


window.mainloop()