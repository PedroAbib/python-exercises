#  Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for pares in range(1, 50):
    if pares % 2 == 0:
        print(pares)
print("Fim.")

"""
Forma mais optimizada:

for pares in range(2, 50, 2):
    print(pares)
"""