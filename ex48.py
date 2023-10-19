# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
# no intervalo de 1 até 500.

soma = 0

for multiplos_3 in range(1, 501):
    if multiplos_3 % 3 == 0 and multiplos_3 % 2 != 0:
        soma += multiplos_3

print(f"A soma é {soma}")

# O código "multiplos_3 % 2 != 0" pode ser substituído por um "2" no final de range, para optimizar o código!