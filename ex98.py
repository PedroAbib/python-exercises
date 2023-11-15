# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}")
    if passo == 0:
        passo = 1
    if inicio > fim and passo > 0 or inicio < fim and passo < 0:
        passo *= -1
    for i in range(inicio, fim, passo):
        print(i, end=" ", flush=True)
        sleep(0.2)
    if fim - passo == i or fim + passo == i:
        print(fim)

contador(1, 10, 1)
contador(10, 0, 2)

print("Personalize a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio, fim, passo)