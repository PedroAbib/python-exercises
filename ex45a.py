# Crie um programa que faça o computador jogar Jokenpo com você.
from random import randint

opcoes = ('', 'Pedra', 'Papel', 'Tesoura')

escolha = int(input("1 - Pedra \n2 - Papel \n3 - Tesoura \nDigite a opção: "))
print(f"Você escolheu {opcoes[escolha]}.")

escolha_bot = randint(1, 3)
print(f"O computador escolheu {opcoes[escolha_bot]}")

if escolha == 1:
    if escolha_bot == 1:
        print("Empate!")
    elif escolha_bot == 2:
        print("Você perdeu!")
    elif escolha_bot == 3:
        print("Você venceu!")

elif escolha == 2:
    if escolha_bot == 1:
        print("Você venceu!")
    elif escolha_bot == 2:
        print("Empate!")
    elif escolha_bot == 3:
        print("Você perdeu!")

elif escolha == 3:
    print("Você escolheu Tesoura.")
    if escolha_bot == 1:
        print("Você perdeu!")
    elif escolha_bot == 2:
        print("Você venceu!")
    elif escolha_bot == 3:
        print("Empate!")

else:
    print("O número não corresponde a uma das opções.")