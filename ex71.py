# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues,
# OBS: Considere que o caixa possui cédulas de 50, 20, 10 e 1.

notas50 = notas20 = notas10 = notas1 = 0

valor = int(input("Quanto deseja sacar? R$"))
while True:
    if valor >= 50:
        notas50 += 1
        valor -= 50
    elif valor < 50 and valor >= 20:
        notas20 += 1
        valor -= 20
    elif valor < 20 and valor >= 10:
        notas10 += 1
        valor -= 10
    elif valor < 10 and valor >= 1:
        notas1 += 1
        valor -= 1
    else:
        break
print(f"Você receberá: \n{notas50} notas de R$50 \n{notas20} notas de R$20 \n{notas10} notas de R$10 \n{notas1} notas de R$1")