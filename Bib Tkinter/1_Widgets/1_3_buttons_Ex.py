# create another checkbutton and 2 radiobuttons 
# radio button:
	# values for the buttons are A and B
	# ticking either prints the value of the checkbutton
	# ticking the radio button unchecks the checkbutton
# check button: 
	# ticking the checkbutton prints the value of the radio button value 
	# use tkinter var for Booleans! 

import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.title('Exercise of Radio Buttons')
window.geometry('600x400')
window.iconbitmap('python.ico')

#Functions
def radio_func():
    print(check_bool.get())
    check_bool.set(False)

#variables
radio_string = tk.StringVar()
check_bool = tk.BooleanVar()

#widgets
exercise_radio1 = ttk.Radiobutton(
    window,
    text = 'Radio A',
    value= 'A',
    variable= radio_string,
    command= radio_func
).pack()

exercise_radio2 = ttk.Radiobutton(
    window,
    text = 'Radio B',
    value= 'B',
    variable= radio_string,
    command= radio_func
).pack()

exercise_check = tk.Checkbutton(
    window,
    text= 'Exercise Check',
    variable= check_bool,
    command= lambda: print(radio_string.get())
).pack()


window.mainloop()