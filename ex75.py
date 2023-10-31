# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma Tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))

tupla = (n1, n2, n3, n4)

print(f"Houveram {tupla.count(9)} números 9.")

if 3 in tupla:
    print(f"O número três aparece primeiramente na posição {tupla.index(3)}")
else:
    print("Não houve número 3")

if n1 % 2 == 0 or n2 % 2 == 0 or n3 % 2 == 0 or n4 % 2 == 0:
    print("Pares presentes na tupla: ", end="")
    for pares in tupla:
        if pares % 2 == 0:
            print(f"{pares} ", end="")
else:
    print("Não há pares.")