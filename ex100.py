# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear
# 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função
# anterior.
from random import randint

lista = []

def sorteia():
    for i in range(0, 5):
        lista.append(randint(1, 10))
    print(f"Os número sorteados foram {lista}")

def somaPar():
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f"A soma de todos os pares é igual a {soma}")

sorteia()
somaPar()