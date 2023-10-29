# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

numero = int(input("Digite um número: "))
n = numero
iteracoes = numero

print(f"{numero}! = {numero}", end="")

while iteracoes > 1:
    n = n * (iteracoes - 1)
    iteracoes -= 1
    print(f"x{iteracoes}", end="")
    if iteracoes == 1:
        print(f" = {n}")