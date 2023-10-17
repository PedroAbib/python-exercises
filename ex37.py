# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a [base de conversão]:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

numero = int(input("Digite um número inteiro: "))

base = int(input("Escolha a base de conversão: \n1 para binário \n2 para octal \n3 para hexadecimal \nEscolha:"))

if base == 1:
    print("O número {} em binário é: {}".format(numero, bin(numero)[2:]))

elif base == 2:
    print("O número {} em octal é: {}".format(numero, oct(numero)[2:]))

elif base == 3:
    print("O número {} em hexadecimal é: {}".format(numero, hex(numero)[2:]))

else:
    print("Este número não corresponde a uma das opções.")