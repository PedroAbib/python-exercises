# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e aquantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

percorrido = float(input("Km percorridos: "))
dias = int(input("Quantos dias: "))

total = (dias * 60) + (percorrido * 0.15)

print("Total a pagar: R${:.2f}".format(total))