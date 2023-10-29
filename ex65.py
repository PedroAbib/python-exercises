# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

maior = None
menor = None
quant = 0
soma = 0
continua = 1

while continua == 1:
    n = float(input("Digite um número: "))
    soma += n
    quant += 1
    if quant == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    pergunta = input("Deseja continuar[S/N]? ").upper()
    if "N" in pergunta:
        continua = 0
print(f"A média entre todos os valores é igual a {soma / quant}.")
print(f"O maior valor digitado foi {maior}, e o menor foi {menor}.")