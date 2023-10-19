# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.
maior = None
menor = None

for pessoa in range(1, 6):
    peso = float(input(f"Peso da pessoa {pessoa}: "))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f"O menor peso lido é {menor}Kg, e o maior é {maior}Kg. :D")