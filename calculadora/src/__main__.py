from meu_pacote import meu_modulo as mm
from meu_pacote import meu_modulo_saudacao as ms

_control_ = False

nome = str(input("Para começar digite o seu nome: "))

while _control_ == False:
    print("-------------------------------------------")
    print("Calculador do Rock!!!")
    print(ms.saudacao(nome))
    _num1_ = float(input("Insira o primeiro numero: "))
    _num2_ = float(input("Insira o segundo numero: "))

    print(ms.escolha(nome))
    print("Escolha uma das opções abaixo: ")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - parar")
    _escolha_ = int(input("Escolha: "))

    if _escolha_ == 1 or _escolha_ == 2 or _escolha_ == 3 or _escolha_ == 4 or _escolha_ == 0:
        match _escolha_:
            case 1:
                print(ms.resposta(nome))
                print(f"A soma de {_num1_} + {_num2_} = {mm.adcionar(_num1_,_num2_)}")
                print("-------------------------------------------")
            case 2:
                print(ms.resposta(nome))
                print(f"A subtração de {_num1_} - {_num2_} = {mm.subtrair(_num1_, _num2_)}")
                print("-------------------------------------------")
            case 3:
                print(ms.resposta(nome))
                print(f"A multiplicação de {_num1_} * {_num2_} = {mm.multiplicacao(_num1_,_num2_)}")
                print("-------------------------------------------")
            case 4:
                print(ms.resposta(nome))
                print(f"A divisão de {_num1_} / {_num2_} = {mm.divisao(_num1_, _num2_)}")
                print("-------------------------------------------")
            case 0:
                print(ms.resposta(nome))
                print("Adeus")
                _control_ = True

    else:
        print("Escolha inválida!")
        print("-------------------------------------------")

    