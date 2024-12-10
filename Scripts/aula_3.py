user = {
    "nome": "Pedro",
    "senha": "1@234"
}

player = {
    "nickname": "Stonyseven",
    "classe": {
        "principal": "Mago",
        "secundaria": "Guerreiro"
    },
    "armas": ["Cajado", "Espada", "Pantufa"],
    "nivel": 10
}

'''
print(user.keys(), player.keys())
print(user.values(), player.values())
print(user.items())
print(player.items())
'''

print(player.values())


usuario = user.get("nome")
senha = user.get("senha")

__user__ = str(input("Insira seu Usuário: "))
__password__ = str(input("Insira a sua Senha: "))

__classe__ = player.get("classe")
__principal__ = __classe__.get("principal")
__secundaria__ = __classe__.get("secundaria")


if __user__ == usuario and __password__ == senha:
    print("Bem-vindo, " + player.get("nickname") + "!")
    print(f"Você é um(a) {__principal__} / { __secundaria__} nivel: [ {player.get("nivel")} ]")

    armas = player.get("armas")
    item_0 = armas[0]
    item_1 = armas[1]
    item_2 = armas[2]
    __inventario__ = [item_0, item_1, item_2]

    print(f"Inventário: {__inventario__[0]}")
    print(f"            {__inventario__[1]}")
    print(f"            {__inventario__[2]}")

else:
    print("Usuário ou Senha Inválidos!")

