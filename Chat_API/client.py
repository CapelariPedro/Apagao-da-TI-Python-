import tkinter as tk
from tkinter import ttk
import sv_ttk
import socketio
import requests

#Conexão client-server
sio = socketio.Client()
SERVER_URL = "http://localhost:5000"

#Função para conectar ao servidor
def connect_server():
    sio.connect(SERVER_URL)

    def update_clients(data):
        listbox_clients.delete(0, tk.END)
        for client in data:
            listbox_clients.insert(tk.END, client)

    def recive_message(data):
        chat_history.insert(tk.END, f'{data['username']}: {data['message']}')

    sio.on('update_clients', update_clients)
    sio.on('receive_message', recive_message)

def send_message():
    message = entry_message.get()
    sio.emit('send_message', {'username': username.get(), 'message': message})
    entry_message.delete(0, tk.END)

def set_username():
    sio.emit('set_username', {'username': username.get()})

'''
#API CRUD
def create_user():
    name = entry_name.get()
    age = entry_age.get()

    if name and age:
        response = requests.post(f'{SERVER_URL}/users', json={'name':name, 'age':age})
        if response.status_code == 201:
            lbl_status.config(text='Usuário cadastrado com sucesso', foreground="green")
        else:
            lbl_status.config(text='Erro ao cadastrar usuário', foreground="red")
    
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)

def fetch_users():
    response = requests.get(f'{SERVER_URL}/users')
    if response.status_code == 200:
        users = response.json()
        listbox_users.delete(0, tk.END)
        for user in users:
            listbox_users.insert(tk.END, f'Nome: {user['name']}, Idade: {users['age']}')
'''

#Interface:
root = tk.Tk()
root.title("Chat/Crud")
sv_ttk.use_light_theme()

notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10)

#Aba de chat
frame_chat = tk.Frame(notebook)
notebook.add(frame_chat, text='Chat')

ttk.Label(frame_chat, text='Chat').pack()
chat_history = tk.Listbox(frame_chat, width=50, height=20)
chat_history.pack()
entry_message = ttk.Entry(frame_chat, width=40)
entry_message.pack(side=tk.LEFT)
btn_send = ttk.Button(frame_chat, text='Enviar', command=send_message)
btn_send.pack(side=tk.LEFT)

ttk.Label(frame_chat, text='Usuários Conectados').pack()
listbox_clients = tk.Listbox(frame_chat, width=50, height=10)
listbox_clients.pack()

#Configurando o Usuário
frame_user = ttk.Frame(notebook)
notebook.add(frame_user, text='Configurar Usuário')

ttk.Label(frame_user, text='Seu Nome').pack()
username = tk.StringVar()
entry_username = ttk.Entry(frame_user, textvariable=username)
entry_username.pack()
btn_set_username = ttk.Button(frame_user, text='Entrar no Chat', command=set_username)
btn_set_username.pack()

# Aba do Sistema de Gestão CRUD
frame_crud = ttk.Frame(notebook)
notebook.add(frame_crud, text="Sistema de Gestão")



connect_server()
root.mainloop()