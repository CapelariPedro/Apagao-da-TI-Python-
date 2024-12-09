import tkinter as tk 
from tkinter import ttk

#List of events
#pythontutorial.net/tkinter/tkinter-event-binding

#functions
def get_pos(event):
    print(f' x: {event.x} y: {event.y}')

#setup
window = tk.Tk()
window.geometry('600x500')
window.title('Events Biding')

#widgets
text = tk.Text(window).pack()

entry = tk.Entry(window).pack()

button = tk.Button(
    window,
    text= 'A button'
).pack()

#events
window.bind('<KeyPress>',lambda event: print(f'a button was pressed ({event.char})'))
window.bind('<Motion>', get_pos)

#button.bind('<Alt-Key-Press-a>', lambda event: print(event))

#entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
#entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))


window.mainloop()