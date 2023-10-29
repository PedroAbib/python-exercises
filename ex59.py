# Crie um programa que leia dois valores e mostre um menu na tela:
'''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
'''
# Seu programa deverá realizar a operação solicitada em cada caso.

opcao = None

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

while opcao != 5:
    opcao = int(input("Qual operação deseja: \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Fechar \nDigite a opção: "))
    if opcao == 1:
        somar = n1 + n2
        print(f"A soma entre {n1} e {n2} é {somar}.")
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f"A multiplicação entre {n1} e {n2} é {multiplicar}.")
    elif opcao == 3:
        if n1 > n2:
            print(f"O número maior {n1}.")
        elif n2 > n1:
            print(f"O número maior é {n2}")
        else:
            print("Os números são iguais.")
    elif opcao == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    elif opcao > 5 or opcao < 1:
        print("Opção invalida, tente novamente.")
print("Fim.")