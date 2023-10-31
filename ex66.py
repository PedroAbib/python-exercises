# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)

n = quant = soma = 0

while True:
    n = int(input("Digite um número(999 para parar): "))
    if n == 999:
        break
    quant += 1
    soma += n
print(f"Você digitou um total de {quant} números que somados resultam em {soma}")