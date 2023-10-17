# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o [valor da casa],
# o [salário] do comprador e em [quantos anos] ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Valor da casa: R$"))

salario = float(input("Salário: R$"))

anos = int(input("Anos: "))

prestacao = valor_casa / (anos * 12)

if prestacao <= salario * (30/100):
    print("O valor da prestação será de R${:.2f}".format(prestacao))

else:
    print("Empréstimo negado.")