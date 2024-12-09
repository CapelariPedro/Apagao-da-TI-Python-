import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and spin')


#ComboBox
items = ('Ice Cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value= items[0])
combo = ttk.Combobox(window, textvariable= food_string)
combo['values'] = items
#combo.configure(values = items)
combo.pack()

#event
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text = 'A label').pack()

#SpinBox

spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(
    window,
    from_ = 3,
    to = 20,
    increment= 3,
    command= lambda: print(spin_int.get()),
    textvariable= spin_int
)

spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('donw'))
spin.pack()


window.mainloop()