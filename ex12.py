# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input("Preço do produto: "))

print("Com desconto: {}".format(produto - (produto * 5 / 100)))
