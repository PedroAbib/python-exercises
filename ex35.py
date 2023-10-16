# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("É possível formar um triâgulo.")

else:
    print("Não é possível formar um triângulo.")