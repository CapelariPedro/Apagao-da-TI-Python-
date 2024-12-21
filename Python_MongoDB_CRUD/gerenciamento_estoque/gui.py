import tkinter as tk
from tkinter import ttk
from estoque import Estoque
from database import conectar_mongo

class EstoqueApp:
    def __init__(self, root):
        self.db = conectar_mongo()
        self.estoque = Estoque(self.db)

        self.root = root
        self.root.title("Gerenciamento de Estoque")
        self.root.geometry("700x700")

        #Widgets
        self.nome_label = ttk.Label(root, text='Nome do Item: ')
        self.nome_label.grid(row=0, column=0, padx = 5, pady= 5)
        self.nome_entry = ttk.Entry(root)
        self.nome_entry.grid(row=0, column=1, padx = 5, pady=5)

        self.qtd_label = ttk.Label( root , text =" Quantidade :")
        self.qtd_label.grid( row =1 , column =0 , padx =5 , pady =5)
        self.qtd_entry = ttk.Entry( root )
        self.qtd_entry.grid( row =1 , column =1 , padx =5 , pady =5)

        self.adicionar_btn = ttk.Button(root, text='Adicionar Item', command=self.adicionar_item)
        self.adicionar_btn.grid(row=2, column=0, padx=5, pady=5)

        self.remover_btn = ttk.Button(root, text='Remover Item', command=self.remover_item)
        self.remover_btn.grid(row=2, column=1, padx=5, pady=5)

        self.listar_btn = ttk.Button(root, text='Listar Itens', command=self.listar_itens)
        self.listar_btn.grid(row=3, column=0, padx=5, pady=5)

        self.resultado_text = tk.Text(root, height= 10, width= 40)
        self.resultado_text.grid(row=4, column=0, columnspan= 2, padx= 5, pady=  5)


    def adicionar_item(self):
        nome = self.nome_entry.get()
        quantidade = int(self.qtd_entry.get())
        self.estoque.adicionar_item(nome, quantidade)
        self.nome_entry.delete(0, tk.END)
        self.qtd_entry.delete(0, tk.END)
        self.resultado_text.insert(tk.END, f'Item {nome} adicionado com sucesso. \n')
        
    def remover_item(self):
        nome = self.nome_entry.get()
        quantidade = int(self.qtd_entry.get())
        self.estoque.remover_item(nome, quantidade)
        self.nome_entry.delete(0, tk.END)
        self.qtd_entry.delete(0, tk.END)
        self.resultado_text.insert(tk.END, f'Item {nome} removido com sucesso')
    
    def listar_itens(self):
        self.resultado_text.delete(1.0, tk.END)
        itens = self.estoque.listar_itens()
        for item in itens:
            self.resultado_text.insert(tk.END, f'{item['nome']}: {item['quantidade']}\n')


if __name__ == '__main__':
    root = tk.Tk()
    app = EstoqueApp(root)
    root.mainloop()