# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salario = int(input("Salário: "))

if salario > 1250:
    print("Aumento de R${:.2f}".format(salario * (10 / 100)))

else:
    print("Aumento de R${:.2f}".format(salario * (15 / 100)))