# Faça um programa que ajude um jogador da MEGASENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai
# sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from time import sleep
from random import randint

lista = []
cont = 1
jogos = int(input("Digite o número de jogos: "))

while jogos != 0:
    for numero in range(0, 6):
        n = randint(1, 60)
        while n in lista:
            n = randint(1, 60)
        lista.append(n)
    sleep(.5)
    print(f"Jogo {cont}: {lista}")
    lista.clear()
    jogos -= 1
    cont += 1