# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número inteiro: "))

e_primo = True

for primo in range(2, numero):
    if numero % primo == 0:
        e_primo = False

if e_primo == False:
    print("O número não é primo.")
else:
    print("O número é primo.")