import tkinter as tk
from tkinter import ttk

#Setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')
window.iconbitmap('python.ico')

#canvas
canvas = tk.Canvas(
    window,
    bg= 'white'
)
canvas.pack()

canvas.create_rectangle(
    (50, 20, 100, 200),
    fill= 'red',
    width= 10,
    dash= (4,2,1,1),
    outline= 'green'
)

canvas.create_oval(
    (200, 0 , 300, 100),
    fill= 'green'
)

canvas.create_arc(
    (200, 0, 300, 100),
    fill= 'red',
    start = 45,
    extent = 140,
    style = tk.CHORD,
    outline = 'red',
    width = 1
)




window.mainloop()