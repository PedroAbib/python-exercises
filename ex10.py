# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1 = R$5.09

carteira = float(input("Quanto de dinheiro possui: "))

print("Pode comprar {:.2f} dólares".format(carteira / 5.09))