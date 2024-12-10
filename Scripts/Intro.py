import tkinter 
import os
import openpyxl
from tkinter import ttk
from tkinter import messagebox


def enter_data():
    accepted = accept_var.get()

    if  accepted == "Accepted":
        nome = first_name_entry.get()
        sobrenome = last_name_entry.get()

        if nome and sobrenome:
            cargo = title_combobox.get()
            idade = age_spinbox.get()
            area_atuacao = area_combobox.get()

            status_registro = reg_status_var.get()
            mes = time_work_combobox.get()
            ano = age_work_spinbox.get()
            
            print("------------------------------------------------------------------------------------------")
            print("Nome: ", nome, "Sobrenome: ", sobrenome)
            print("Cargo: ",cargo, "Idade: ", idade, "Área de atuação: " ,area_atuacao)
            print("Status do Registro: ", status_registro, "# Mês da Contratação: ", mes, "#Ano da Contratação: ",ano)
            print("------------------------------------------------------------------------------------------")

            filepath = "D:\Github\Formulario-Para-Dados-em-Python\Integração Excel_Python/data.xlsx"

            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = ["Nome", "Sobrenome", "Cargo","Idade","Área de Atuação","Mês de Contratação","Ano de Contratação","Status de Registro"]
                sheet.append(heading)
                workbook.save(filepath)

            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append([nome,sobrenome,cargo,idade,area_atuacao,mes,ano,status_registro])
            workbook.save(filepath)

        else:
            tkinter.messagebox.showwarning(title="Erro", message="Nome e Sobrenome são necessarios.")
    
    else:
        tkinter.messagebox.showwarning(title="Erro", message="Você tem que aceitar os termos e condições.")

# Criando a Janela
window = tkinter.Tk()
window.title("Formulario de coleta de dados")

#Criando os Frames
frame = tkinter.Frame(window)
frame.pack()

#1-Frame
# Salva a informação do usuario
user_info_frame = tkinter.LabelFrame(frame, text="Informação do Usuario")
user_info_frame.grid(row= 0 , column= 0, padx= 20, pady= 20) #padx e pady determinam a posição no Frame.

#Entrada do Nome
first_name_label = tkinter.Label(user_info_frame, text="Nome")
first_name_label.grid(row=0 , column=0)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)

#Entrada do Sobrenome
last_name_label = tkinter.Label(user_info_frame, text="Sobrenome")
last_name_label.grid(row=0, column=1)

last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

#Entrada da idade
age_labe = tkinter.Label(user_info_frame, text="Idade")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_labe.grid(row=0,column=2)
age_spinbox.grid(row=1, column=2)

#Entrada do Cargo (Através de uma lista)
title_label = tkinter.Label(user_info_frame, text="Cargo")
title_combobox = ttk.Combobox(user_info_frame, values=["Gerente","Especialista","Técnico","Operador","Estagiario"])
title_label.grid(row=2, column=0)
title_combobox.grid(row=3, column=0)


#Entrada da Area de Atuação (Através de Lista)
area_laebl = tkinter.Label(user_info_frame, text="Área de Atuação")
area_combobox = ttk.Combobox(user_info_frame, values=["Fábrica","Logistica","Administrativo","TI"])
area_laebl.grid(row=2, column=1)
area_combobox.grid(row=3, column=1)

#Configurandos Todos os .grid do 1-Frame (redimensionamento)
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#2-Frame
#Registro
registered_frame = tkinter.LabelFrame(frame, text="Registro")
registered_frame.grid(row=1,column=0, sticky="news", padx=20, pady=20)

#Confirmação de Registro
registered_label = tkinter.Label(registered_frame, text="Status de Registro")
reg_status_var = tkinter.StringVar(value="Não Registrado")
reg_status_check = tkinter.Checkbutton(registered_frame, text="Registrado Corretamente", variable=reg_status_var, onvalue="Registrado", offvalue="Não Registrado")

registered_label.grid(row= 0, column= 0)
reg_status_check.grid(row= 1,column= 0)

#Entrada Mês de Contratação
time_work_label = tkinter.Label(registered_frame, text="Mês de Contratação")
time_work_combobox = ttk.Combobox(registered_frame, values=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"])
time_work_label.grid(row=0,column=1)
time_work_combobox.grid(row=1, column=1)

#Entrada Ano de Contratação
age_work_label = tkinter.Label(registered_frame, text="Ano da Contratação")
age_work_spinbox = tkinter.Spinbox(registered_frame, from_=1950, to=2025)
age_work_label.grid(row=0, column=2)
age_work_spinbox.grid(row=1, column=2)

#Configurandos Todos os .grid do 2-Frame (redimensionamento)
for widget in registered_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#3-Frame
#Termos e Condições
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0,sticky="news", padx=20, pady=10)

#Entrada da Confirmação
accept_var_label = tkinter.Label(terms_frame,)
accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0,column=0)

#Configurandos Todos os .grid do 3-Frame (redimensionamento)
for widget in terms_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Botão
button = tkinter.Button(frame, text="Computar Informação", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


window.mainloop()