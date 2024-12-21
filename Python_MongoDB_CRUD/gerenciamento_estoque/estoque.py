class Estoque:
    def __init__(self, db):
        self.db = db
        self.collection = db['estoque']

    def adicionar_item(self, nome, quantidade):
        #Comando MongoBD que encontra o iem pelo nome
        item = self.collection.find_one({'nome': nome})
        #Verifica se o item existe
        if item:
            nova_quantidade = item['quantidade'] + quantidade
            #Update com comando MongoDB
            self.collection.update_one({
                'nome': nome}, 
                {'$set': {'quantidade': nova_quantidade}
            })
        else:
            #Caso o item não exista, adiciona com comando MongoDB
            self.collection.insert_one({
                'nome': nome, 
                'quantidade': quantidade
            })
    
    def remover_item(self, nome, quantidade):
        item = self.collection.find_one({'nome': nome})
        if item:
            nova_quantidade = item['quantidade'] - quantidade
            if nova_quantidade <= 0:
                #Comando de deletar MongoDB
                self.collection.delete_one({'nome': nome})
            else:
                #Comando de update MongoDB
                self.collection.update_one({
                'nome': nome}, 
                {'$set': {'quantidade': nova_quantidade}
            })
        else:
            print(f'Item {nome} não encontrado no estoque')

    def listar_itens(self):
        return list(self.collection.find())