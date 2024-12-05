#Declarando Váriaveis Tipos Primitivos:

var1 = 1
var2 = 1.5
var3 = "Olá, Mundo!"
var4 = True
var5 = None

#Concatenção e converção de tipo primitivo
print(str(var2)+ " " + str(var1))

#Concatenando Strings
nome = "Pedro"
sobrenome = "Capelari"

print(nome + " " + sobrenome)

#Operações matemáticas:

#Soma +
print(5 + 5)
print(5 + 5.5)
print(5 + 5.5 + 5.5)

#Subtração -
print(5 - 5)
print(5 - 5.5)
print(5 - 5.5 - 5.5)

#Multiplicação *
print(5 * 5)
print(5 * 5.5)
print(5 * 5.5 * 5.5)

#Divisão /
print(5 / 5)
print(5 / 5.5)
print(5 / 5.5 / 5.5)

#Resto %
print(5 % 5)
print(5 % 5.5)

#Condicional

#if simples

media = 6.0
media_aluno = 7.0

if media_aluno > media:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

#if alinhado

print("Qual o ano de criação da linguagem Python")
print("1990")
print("1998")
print("1991")

resp = int(input("Informe a sua resposta"))

if resp == 1991:
    print("Certo! A linguagem Python foi criada em 1991")
elif resp == 1990:
    print("Incorreto!")
elif resp == 1998:
    print("Incorreto!")
else:
    print("Resposta inválida! ")

#While laços de repetição:
count = 1
while count <= 5:
    print("Contando: " + str(count))
    count += 1

for i in range(1, 6):
    print(i)

#Funções:
def soma(a, b):
    return a + b

# Chamando a função e imprimindo o resultado
resultado = soma(5, 3)
print(resultado)


#Estrutura de dados:
#Listas
# Criando uma lista
frutas = ["maçã", "banana", "laranja"]

# Acessando elementos
print(frutas[1])  # Output: banana

# Adicionando elementos
frutas.append("uva")

# Removendo elementos
frutas.remove("laranja")

# Iterando sobre uma lista
for fruta in frutas:
    print(fruta)

#Tuplas
# Criando uma tupla
animais = ("gato", "cachorro", "coelho")

# Acessando elementos
print(animais[0])  # Output: gato

# Iterando sobre uma tupla
for animal in animais:
    print(animal)

#Conjuntos:
# Criando um conjunto
numeros = {1, 2, 3, 4, 5}

# Adicionando elementos
numeros.add(6)

# Removendo elementos
numeros.remove(3)

# Operações de conjunto
pares = {2, 4, 6, 8}
interseccao = numeros.intersection(pares)  # Output: {2, 4, 6}
uniao = numeros.union(pares)  # Output: {1, 2, 4, 5, 6, 8}

# Dicionários
# Criando um dicionário
pessoa = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

# Acessando valores
print(pessoa["nome"])  # Output: Alice

# Adicionando novos pares chave-valor
pessoa["email"] = "alice@example.com"

# Removendo pares chave-valor
del pessoa["cidade"]

# Iterando sobre um dicionário
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
