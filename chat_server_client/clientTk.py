import socket
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

HOST = '127.0.0.1'
PORT = 8080

class ChatClient(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title('Chat Client')
        self.geometry('700x900')

        self.chat_area = scrolledtext.ScrolledText(self, state='disable', wrap='word')
        self.chat_area.pack(padx=10, pady=10, fill='both', expand=True)

        self.msg_entry = ttk.Entry(self)
        self.msg_entry.pack(padx=10, pady=10, fill='x')
        self.msg_entry.bind("<Return>", self.send_message)

        self.send_button = ttk.Button(self, text="Enviar", command=self.send_message)
        self.send_button.pack(pady=5)



        #Conexão com o servidor
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

        threading.Thread(target=self.recive_messages, daemon=True).start()


    def send_message(self, event=None):
        message = self.msg_entry.get()
        if message:
            self.client.send(message.encode())
            self.msg_entry.delete(0, 'end')

    def recive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode()
                if message:
                    self.chat_area.config(state='normal')
                    self.chat_area.insert(tk.END, message + '\n')
                    self.chat_area.config(state='disabled')
                    self.chat_area.yview(tk.END)
            except:
                break

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chat GUI client/server")
        self.geometry("300x200")

        ttk.Button(self, text="Abrir Chat", command=self.open_chat).pack(pady=20)

    def open_chat(self):
        ChatClient(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()