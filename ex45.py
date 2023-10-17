# Crie um programa que faça o computador jogar Jokenpo com você.
import random

escolha = int(input("1 - Pedra \n2 - Papel \n3 - Tesoura \nDigite a opção: "))

pedra = 1
papel = 2
tesoura = 3

escolha_bot = random.randint(1, 3)

if escolha == pedra:
    print("Você escolheu Pedra.")
    if escolha_bot == pedra:
        print("O computador escolheu Pedra.")
        print("Empate!")
    elif escolha_bot == papel:
        print("O computador escolheu Papel.")
        print("Você perdeu!")
    elif escolha_bot == tesoura:
        print("O computador escolheu Tesoura.")
        print("Você venceu!")

elif escolha == papel:
    print("Você escolheu Papel.")
    if escolha_bot == pedra:
        print("O computador escolheu Pedra.")
        print("Você venceu!")
    elif escolha_bot == papel:
        print("O computador escolheu Papel.")
        print("Empate!")
    elif escolha_bot == tesoura:
        print("O computador escolheu Tesoura.")
        print("Você perdeu!")

elif escolha == tesoura:
    print("Você escolheu Tesoura.")
    if escolha_bot == pedra:
        print("O computador escolheu Pedra.")
        print("Você perdeu!")
    elif escolha_bot == papel:
        print("O computador escolheu Papel.")
        print("Você venceu!")
    elif escolha_bot == tesoura:
        print("O computador escolheu Tesoura.")
        print("Empate!")

else:
    print("O número não corresponde a uma das opções.")