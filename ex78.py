# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
maior = 0
menor = 0
valores = []

for p in range(0, 5):
    valores.append((int(input("Digite um valor: "))))
    if p == 0:
        maior = menor = valores[p]
    elif valores[p] > maior:
        maior = valores[p]
    elif valores[p] < menor:
        menor = valores[p]

print(f"O maior valor foi {maior} que se encontra na posição ", end="")
for p, v in enumerate(valores):
    if v == maior:
        print(f"{p}... ", end="")

print(f"\nO menor valor foi {menor} que se encontra na posição ", end="")
for p, v in enumerate(valores):
    if v == menor:
        print(f"{p}... ", end="")

print(f"\n{valores}")