import tkinter
import os
import openpyxl
from tkinter import ttk
from tkinter import messagebox





# Create a new tkinter window
root = tkinter.Tk()
root.title("Formulário de dados: ")

frame = ttk.Frame(root)
frame.pack()

user_info_frame = ttk.LabelFrame(frame, text="Informação dos Funcionarios")
user_info_frame.grid(row=0, column= 0, padx= 20, pady= 20)

first_name_label = ttk.Label(user_info_frame, text="nome")
first_name_label.grid(row=0, column=0)

first_name_label = ttk.Entry(user_info_frame)
first_name_label.grid(row=1, column=0)

last_name_label = ttk.Label(user_info_frame, text="Sobrenome")
last_name_label.grid(row=0, column=1)

last_name_entry = ttk.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

age_label = ttk.Label(user_info_frame,  text="Idade")
age_label.grid(row=0, column=1)

age_spinbox = ttk.Spinbox(user_info_frame, from_=18, to=110)


root.mainloop()