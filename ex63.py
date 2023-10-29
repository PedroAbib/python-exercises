# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

n = int(input("Digite um número: "))
iteracao = n
termo = 0
termo2 = 1

print(f"{termo}", end="")
while iteracao > 0:
    print(f" - {termo2}", end="")
    termo2 = termo + termo2
    termo = termo2 - termo
    iteracao -= 1