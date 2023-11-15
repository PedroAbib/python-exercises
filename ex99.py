# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* int):
    maior = int[0]
    for i in int:
        if i > maior:
            maior = i
    print(f"O maior número digitado foi {maior}.")
    print(f"Total de números digitados: {len(int)}")

maior(1, 5, 6, 3, 9, 1)