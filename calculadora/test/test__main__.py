import pytest 
from meu_pacote import meu_modulo, meu_modulo_saudacao

def test_modulo_1():
    assert meu_modulo.adcionar(1,2) == 3
    assert meu_modulo.subtrair(3,1) == 2
    assert meu_modulo.multiplicacao(3,5) == 15
    assert meu_modulo.divisao(10,2) == 5

def test_modulo_2():
    assert meu_modulo_saudacao.escolha("Pedro") == f"Olá, Pedro! Como posso ajudar?"
    assert meu_modulo_saudacao.saudacao("Vitor") == f"Olá, Vitor!"
    assert meu_modulo_saudacao.resposta("Jonatha") == f"A sua resposta Jonatha é: "
 
print(test_modulo_1())
print(test_modulo_2())

