'''
class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def saudacao(self):
        return f"Olá, eu sou {self.nome}, tenho {self.idade} anos e venho de {self.cidade}"

pessoa1 = Pessoa("Pedro", 25, "Londrina")
print(pessoa1.saudacao())

class Carro:
    def __init__(self, modelo, ano, marca,cor):
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.cor = cor
    
    def descricao(self):
        return f"{self.marca}, {self.modelo}, {self.ano}, da cor {self.cor}"
    
carro1 = Carro("Mustang", 1978, "Ford", "Preta")
print(carro1.descricao())


class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        return f"{self.nome}, Au Au!!!"

class Gato(Animal):
    def som(self):
        return f"{self.nome}, Miau!!!"

__rex__ = Cachorro("Rex")
print(__rex__.som())

__snowball__ = Gato("Snow Ball")
print(__snowball__.som())
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo = self.__saldo - valor
        else:
            print("Saldo Insuficiente")

    def mostrarSaldo(self):
        return self.__saldo

nome = str(input("Informe o nome do titular da conta: "))
valor_deposito = float(input("Informa o valor a se depositar: "))
valor_saque = float(input("Informe o valor do saque: "))

conta = ContaBancaria(nome, 3000)
print(conta.mostrarSaldo()) 
conta.depositar(valor_deposito)
print(conta.mostrarSaldo())
conta.sacar(valor_saque)
print(conta.mostrarSaldo())


        