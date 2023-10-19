# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.
lista_peso = []

for pessoa in range(1, 6):
    peso = float(input(f"Peso da pessoa {pessoa}: "))
    lista_peso.append(peso)
lista_peso.sort()
print(lista_peso)

print(f"O menor peso lido é {lista_peso[0]}Kg, e o maior é {lista_peso[4]}Kg. :D")