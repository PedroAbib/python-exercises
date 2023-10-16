# Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero = random.randint(0, 5)

escolha = int(input("Digite um número inteiro de 0 a 5: "))

if escolha == numero:
    print("Acertou")

else:
    print("Errou")

