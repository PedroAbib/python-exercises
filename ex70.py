# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# a) Qual é o total gasto na compra.
# b) Quantos produtos custam mais de R$1000.
# c) Qual é o nome do produto mais barato.

mais_1000 = total_gasto = 0
mais_barato = ""
menor = 0

while True:
    nome = input("Produto: ")
    preco = float(input("Preço: R$"))
    total_gasto += preco
    if preco > 1000:
        mais_1000 += 1
    if menor == 0:
        mais_barato = nome
        menor = preco
    if preco < menor:
        mais_barato = nome
    continuar = input("Deseja continuar[S / N]? ").upper().strip()
    if "N" in continuar:
        break
print(f"Total de gastos: R${total_gasto:.2f} \nProdutos que custaram mais de R$1000,00: {mais_1000} \nProduto mais barato: {mais_barato}")