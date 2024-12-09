import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Menu')

#Menu
menu = tk.Menu(window)

#Submenu
file_menu = tk.Menu(menu, tearoff= False)
file_menu.add_command(label = 'New', command= lambda: print('New File'))
file_menu.add_command(label= 'Open', command= lambda: print('Open file'))
file_menu.add_separator()
menu.add_cascade(label= 'File', menu = file_menu)

#Outro Submenu
help_menu = tk.Menu(menu, tearoff= False)
help_menu.add_command(label= 'Help Entry', command= lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label= 'check', onvalue= 'on', offvalue= 'off',variable= help_check_string )

menu.add_cascade(label= 'help', menu= help_menu)

#Exercicio
exercise_menu = tk.Menu(menu, tearoff= False)
exercise_menu.add_command(label= 'exercise test 1')
menu.add_cascade(label= 'Exercise', menu = exercise_menu)

exercise_sub_menu = tk.Menu(menu, tearoff= False)
exercise_sub_menu.add_command(label='some more stuff')
exercise_sub_menu.add_cascade(label='More struff', menu= exercise_sub_menu)

window.configure(menu = menu)
#Botão do menu
menu_button = ttk.Menubutton(window, text = 'Menu Button').pack()

button_sub_menu = tk.Menu(menu_button, tearoff= False)
button_sub_menu.add_command(label= 'Entry 1', command = lambda: print('test 1'))
button_sub_menu.add_checkbutton(label= 'check 1')


window.mainloop()