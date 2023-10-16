# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

maior = 0
menor = 0

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2

elif n2 > n1 and n2 > n3:
    maior = n2
    if n1 > n3:
        menor = n3
    else:
        menor = n1

elif n3 > n1 and n3 > n2:
    maior = n3
    if n1 > n2:
        menor = n2
    else:
        menor = n1

print(f"Maior: {maior}")
print(f"Menor: {menor}")