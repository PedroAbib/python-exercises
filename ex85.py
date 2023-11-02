# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os
# valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[],[]]

for numeros in range(0, 7):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

print(f"Pares: {sorted(valores[0])}")
print(f"Ímpares: {sorted(valores[1])}")