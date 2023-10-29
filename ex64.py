# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

n = 0
quant_numeros = 0
soma_numeros = 0

while n != 999:
    n = int(input("Digite um número: "))
    soma_numeros += n
    quant_numeros += 1
print(f"Foram digitados um total de {quant_numeros} números, que somados dão {soma_numeros}.")