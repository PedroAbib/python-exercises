# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

lista = [[[],[],[]],
         [[],[],[]],
         [[],[],[]]]

for posicao in range(0, len(lista)):
    for indice in range(0, len(lista[posicao])):
        lista[posicao][indice].append(int(input(f"Digite um número para a posição[{posicao}, {indice}]: ")))
print(f"{lista[0]} \n{lista[1]} \n{lista[2]}")